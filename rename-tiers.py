# -*- coding: utf-8 -*-
# This tells python that parts of the script are utf-8

"""
rename-tiers.py
This is just a series of regex replacements, renaming all tiers in an ELAN file using a single command. It is designed to replace the default post-Flex tier names, which are awkward.
... Seems to need something more to rename the linguistic types???

"""

import sys, re, os, shutil, time, datetime

ts = time.time()
datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_')

def usage():
	print """
#################################################
# USAGE INSTRUCTIONS: process-postflex.py
#################################################

You can optionally give it a file name to use as source. Otherwise it will go through entire current dir and subdirs (but not /old-versions)

"""

def main():
	
	if not len(sys.argv)>1:
		print "No target file specified, so entire current dir will be processed"
		# Get set of all input files; for the moment just everything in current directory
		inputfiles = get_inputs('.')
	else:
		inputfiles = [sys.argv[1]]
	print inputfiles

	for infile in inputfiles:
		print "reading file... "+infile

		inputFile = open(infile, 'r')
		lines = inputFile.readlines()

		#now make output without .merge bit of extension
		outFileName = infile
		outFileName = re.sub('merge.eaf', 'eaf', outFileName)
		outFileName = re.sub('merge.pfsx', 'pfsx', outFileName)
		outputFile = open(outFileName, 'w')
		print "writing file... "+outFileName
		
		for line in lines:
			newLine = line
			newLine = re.sub('phrase-txt-mwf', 'phrase', newLine)
			newLine = re.sub('phrase-gls-en', 'trans', newLine)
			newLine = re.sub('phrase-comment-en', 'comment', newLine)
			newLine = re.sub('word-txt-mwf', 'word', newLine)
			newLine = re.sub('morph-txt-mwf', 'morph', newLine)
			newLine = re.sub('morph-cf-mwf', 'citeMorph', newLine)
			newLine = re.sub('morph-gls-en', 'gls', newLine)
			newLine = re.sub('morph-msa-en', 'partSpeech', newLine)
			#newLine = re.sub('', '', newLine)
			outputFile.write(newLine)

def get_inputs (source):

	inputfiles = []
	if os.path.isdir(source):
		#multiple files from directory
		for dirname, dirnames, filenames in os.walk(source):
			for filename in filenames:
				path = os.path.join(dirname, filename)
				if (re.search(r'\.merge\.eaf$', path) or re.search(r'\.merge\.pfsx$', path)) and not re.search('old-versions', path): 
					#print path
					inputfiles.append(path)
	else:
		#just one file
		inputfiles.append(source)
		
	return inputfiles

if __name__ == "__main__":
    main()