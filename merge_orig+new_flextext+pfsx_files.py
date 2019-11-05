# -*- coding: utf-8 -*-
# This tells python that parts of the script are utf-8
"""
merge_orig+new_flextext+pfsx_files.py

###############
AUTHORS:
	John Mansfield
	Christopher Weedall

###############
DATE:
	05 NOV 2019 (current version)

###############
DESCRIPTION:

Following the Fieldworks (FLEx) .flextext export and merging it with the original ELAN .flextext file (accomplished by merge_ELAN_FLEx_flextext.xsl),
we have a new MERGED.flextext file.  This file, however, still has incorrect labels.  (Each tier is prefixed by "A_", "B_", "C_", etc.)
To fix this requires TWO steps!!

1) Open ELAN and import the MERGED.flextext file.
	-- Save this ELAN project to MERGED.eaf (use whatever name you desire, we just use MERGED.ear for example here)
2) Run *this* Python script
 

This is just a series of regex replacements, renaming all tiers in an ELAN .eaf file.
We also replace the clunky "A_", "B_", "C_", etc. at the beginning of tier names (from FLEx) with the Participant's initials.
	-- Assuming multiple speakers (or PARTICIPANTS) have the same initials, this file will append a counter to the initials
	-- for example, if there is a "John Smith" (who has tier labels beginning with "A_") 
					and "Joe Something" (who has tier labels beginning with "B_"), 
					the updated tier labels will be "JS" (for John Smith) and "JS2" (for Joe Something)

###############
REQUIREMENTS:
	Python must be installed.
		- See https://www.python.org/downloads/ (for standard Python installation)
		- See https://www.anaconda.com/distribution/ (for Anaconda Python installation)
		- See https://www.activestate.com/products/python/ (for ActiveState installation)
		- See https://wiki.python.org/moin/PythonDistributions (for a list of other Python distributions)
		
	Python 3+ is assumed.  Pre-Python 3 versions will eventually be deprecated.
	This *might* work in Python 2.7 (for example)... but we haven't tested it.

########################
HOW TO RUN THIS SCRIPT:
########################

1) Open a command prompt / terminal -> in the directory where the MERGED.eaf and MERGED.pfsx files are located.
2) Follow the usage/examples below for your operating system.
=============================================================================================================================
::NOTE::
	We assume that *this* Python file (merge_orig+new_flextext+pfsx_files.py) is *also* located in the same directory
	as MERGED.eaf and MERGED.pfsx.  If you wish to run it from elsewhere, these usage examples will need to be modified 
	to reflect that!
=============================================================================================================================

###############
USAGE:
###############

python merge_orig+new_flextext+pfsx_files.py MERGED.eaf

"""

import datetime
import os
import re
import shutil
import sys
import time

# Get the first argument from the command line - if it is blank/unspecified, we have no idea what to do...
if not len(sys.argv) > 1:
	print ("No target file specified")
	sys.exit()
else:
	input_filenames = [sys.argv[1]]

# Also give the same treatment to the associated pfsx (formatting) file
pfsxFile = re.sub('.eaf', '.pfsx', input_filenames[0])
input_filenames.append(pfsxFile)

# Keep track all the tier IDs which are replaced and what the new ID is
# -- This is necessary because the pfsx (preference file) does not have PARTICIPANT information
tiers = {}

# Loop through each file
for filename in input_filenames:
	# Tell user which file is being processed
	print ("doing file... " + filename)
	
	# Open the file for reading
	with open(filename, 'rb', 0) as file:
		# Keep track of the entire file contents, line-by-line
		_output_line_data_ = b''
		# Keep track of each tier's participant (specifically their initials)
		participant_initials = b'@'#This is the letter with an ASCII value 1 less than A
		# Keep track of the initials we encountered on top-level tiers.
		# -- Necessary because if multiple users have the same initials, we have problems/confusion!
		all_initials = {}
		
		# If the file is the .eaf file
		if '.eaf' in filename:
			# Loop through each line of the file
			for line in file:
				# Keep track of the modified TIER_IDs and PARENT_REFs
				# -- need to *also* update them exactly the same way in the ELAN preferences (.pfsx) file!!
				if not re.findall(rb'TIER_ID="([^"]*)"', line):
					orig_tier = None
				else:
					orig_tier = re.findall(rb'TIER_ID="([^"]*)"', line)[0]#
					# Check if there's also a parent tier reference
					if not re.findall(rb'PARENT_REF="([^"]*)"', line):
						orig_parent_tier = None
					else:
						orig_parent_tier = re.findall(rb'PARENT_REF="([^"]*)"', line)[0]
				
				# Not all the lines of the file contain the <TIER> nodes.
				# 	If the current line is NOT a tier node, lets ignore it
				# 	If the current line IS a tier node, lets process it and replace the tier names
				if re.findall(rb'<TIER', line):
					tier_prefix = re.findall(rb'TIER_ID="([^"]*)_', line)[0]
					
					# Check if there's a PARTICIPANT attribute.
					# 	If so, get the initials.
					# 	If not, get use the generic "A", "B", etc.
					if b'PARTICIPANT=' in line:
						participant_initials = b''.join([x[0:1].upper() for x in re.findall(rb'PARTICIPANT="([^"]*)"', line)[0].split(b' ')])
					else:
						participant_initials = participant_initials[0]+1
					
					# If the all_initials dictionary has not bee updated, then this tier_ID prefix-initials (key-value) pair must be added
					# Also, if the tier_ID prefix-initials (key-value) pair doesn't exist in the dictionary, we must add it
					if not all_initials and not tier_prefix in all_initials and not participant_initials in all_initials.values():
						# Add the new tier_ID prefix-initials (key-value) pair to the dictionary
						all_initials.update({tier_prefix : participant_initials})#
					elif not tier_prefix in all_initials and participant_initials in all_initials.values():
						# Start the initials counter at 2 (because this is *at least* the second PARTICIPANT with these initials)
						initials_count = 2
						# Increment the initials counter until the initials + counter combination is *NOT* found in the dictionary
						while participant_initials + bytes((initials_count,)) in all_initials:
							initials_count += 1
						# Add the new prefix(with counter)-initials (key-value) pair to the dictionary
						all_initials.update({tier_prefix : participant_initials + str(initials_count).encode('utf-8')})
					
					## In all text replacement below,  the directions represent participant's initials as ZZ
					# Replace "...phrase-txt-..." with "ZZ_phrase"
					line = re.sub(b'="([^"]*)phrase-txt-', b'="%s_phrase-'%(all_initials.get(tier_prefix)), line)
					# Replace "...phrase-lit-..." with "ZZ_ortho"
					# 	"ortho" represents the standard orthography for the language (including capitalization and punctuation)
					line = re.sub(b'([^"]*)phrase-lit-', b'%s_ortho-'%(all_initials.get(tier_prefix)), line)
					# Replace "...phrase-gls-..." with "ZZ_trans"
					line = re.sub(b'([^"]*)phrase-gls-', b'%s_trans-'%(all_initials.get(tier_prefix)), line)
					# Replace "...phrase-comment-..." with "ZZ_comment"
					line = re.sub(b'([^"]*)phrase-comment-', b'%s_comment-'%(all_initials.get(tier_prefix)), line)
					# Replace "...word-txt-..." with "ZZ_word"
					line = re.sub(b'([^"]*)word-txt-', b'%s_word-'%(all_initials.get(tier_prefix)), line)
					# Replace "...morph-txt-..." with "ZZ_morph"
					line = re.sub(b'([^"]*)morph-txt-', b'%s_morph-'%(all_initials.get(tier_prefix)), line)
					# Replace "...word-cf-..." with "ZZ_citeMorph"
					line = re.sub(b'([^"]*)morph-cf-', b'%s_citeMorph-'%(all_initials.get(tier_prefix)), line)
					# Replace "...morph-gls-..." with "ZZ_gls"
					line = re.sub(b'([^"]*)morph-gls-', b'%s_gls-'%(all_initials.get(tier_prefix)), line)
					# Replace "...morph-msa-..." with "ZZ_partSpeech"
					line = re.sub(b'([^"]*)morph-msa-', b'%s_partSpeech-'%(all_initials.get(tier_prefix)), line)
					
					# If there is a parent tier reference, add/update the key
					if orig_parent_tier is not None:#
						tiers.update({orig_parent_tier:re.findall(rb'PARENT_REF="([^"]*)"', line)[0]})
					# If there is a tier ID, add/update the key
					if orig_tier is not None:#
						tiers.update({orig_tier:re.findall(rb'TIER_ID="([^"]*)"', line)[0]})
				
				# Store the line data (whether or not it has been changed!)
				_output_line_data_ += line
		elif '.pfsx' in filename:
			# Loop through each line of the file
			for line in file:
				# Loop through all the keys and update the line accordingly
				for key in tiers.keys():
					# Update the line if any of the original tier IDs was found
					line = re.sub(key, tiers[key], line)
				# Store the line data (whether or not it has been changed!)
				_output_line_data_ += line
		
		# Now output the new file!
		with open(os.path.splitext(filename)[0]+'_[tiers_renamed]'+os.path.splitext(filename)[1], 'wb') as outfile:
			outfile.write(_output_line_data_)
