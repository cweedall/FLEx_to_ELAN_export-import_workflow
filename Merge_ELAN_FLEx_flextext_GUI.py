# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import datetime
import difflib
import os
os.system('') #enable VT100 Escape Sequence for WINDOWS 10 Ver. 1607
import pathlib
import pyautogui
import pyperclip
import re
import shutil
import subprocess
import sys
import tempfile
import time
#######################
from tkinter import *
from TkinterDnD2 import *
#######################
#######################

def output_remove_FLEx_flextext_punct_xsl():
	#
	_remove_FLEx_flextext_punct_xsl_data_ =b'<?xml version="1.0" encoding="UTF-8"?>\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\txmlns:xs="http://www.w3.org/2001/XMLSchema"\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\txmlns:math="http://www.w3.org/2005/xpath-functions/math"\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\texclude-result-prefixes="xs math"\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\tversion="3.0">\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<xsl:output indent="yes" media-type="xml"/>\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<xsl:preserve-space elements="*"/>\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<!-- Do nothing with these elements (from FLEX file) -->\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<xsl:template match="//word[descendant::item[@type=\'punct\']]"/><!-- FLEx separates punctuation into their own "words" -->\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<xsl:template match="//word/item[@type=\'gls\']"/><!-- Don\'t want the word gloss (only morpheme gloss) - PERHAPS MAKE THIS AN OPTION?? -->\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<xsl:template match="//word/item[@type=\'pos\']"/><!-- Don\'t want the word part of speech (only morpheme PoS - the \'msa\') - PERHAPS MAKE THIS AN OPTION?? -->\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<xsl:template match="//item[@type=\'cf\']"/><!-- Don\'t want the citation form - PERHAPS MAKE THIS AN OPTION?? -->\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<!--<xsl:template match="morph/@type"/>-->\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<xsl:template match="//item[@type = \'hn\' or @type = \'variantTypes\']"/><!-- Don\'t want the number or variant type -->\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<xsl:template match="//word/item[@type=\'txt\']"/><!-- Don\'t want word/item of \'txt\' type -->\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<xsl:template match="//morph/item[@type=\'txt\']"/><!-- Don\'t want morph/item of \'txt\' type -->\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<!-- Copy all nodes from input (ELAN) file to use as the default structure.\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t\t\tThis approach is preferred because all we want to do is add the new morpheme glosses and parts of speech from FLEx -->\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t<xsl:template match="@*|node()">\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t\t<xsl:copy>\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t\t\t<xsl:apply-templates select="@*|node()"/>\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t\t</xsl:copy>\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'\t</xsl:template>\n'
	_remove_FLEx_flextext_punct_xsl_data_ +=b'</xsl:stylesheet>\n'
	#
	with open(_XSL_REMOVE_FLEX_FLEXTEXT_PUNCT_PATH_, 'wb') as _remove_FLEx_flextext_punct_xsl_:
		_remove_FLEx_flextext_punct_xsl_.write(_remove_FLEx_flextext_punct_xsl_data_)
	#

def output_merge_flextext_xsl():
	#
	_merge_flextext_xsl_data_ =b'<?xml version="1.0" encoding="UTF-8"?>\n'
	_merge_flextext_xsl_data_ +=b'<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"\n'
	_merge_flextext_xsl_data_ +=b'\txmlns:xs="http://www.w3.org/2001/XMLSchema"\n'
	_merge_flextext_xsl_data_ +=b'\txmlns:math="http://www.w3.org/2005/xpath-functions/math"\n'
	_merge_flextext_xsl_data_ +=b'\texclude-result-prefixes="xs math"\n'
	_merge_flextext_xsl_data_ +=b'\tversion="3.0">\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t<xsl:output indent="yes" media-type="xml"/>\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t<xsl:preserve-space elements="*"/>\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t<!-- Verify the input file (the ELAN .flextext file) exists -->\n'
	_merge_flextext_xsl_data_ +=b'\t<xsl:variable name="ELANDocCheck" select="if (doc-available(\'input:request\')) then doc(\'input:request\') else ()"/>\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t<!-- Path to the second input file (the FLEx .flextext file) -->\n'
	_merge_flextext_xsl_data_ +=b'\t<xsl:param name="FLEx"/>\n'
	_merge_flextext_xsl_data_ +=b'\t<!-- Verify the second input file (the FLEx .flextext file) exists -->\n'
	_merge_flextext_xsl_data_ +=b'\t<xsl:variable name="FLExDocCheck" select="if (doc-available(\'$FLEx\')) then doc(\'$FLEx\') else ()"/>\n'
	_merge_flextext_xsl_data_ +=b'\t<!-- Store the second (FLEx) input file as a variable -->\n'
	_merge_flextext_xsl_data_ +=b'\t<xsl:variable name="FLExfile" select="document($FLEx)" />\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t<!-- Copy all nodes from input (ELAN) file to use as the default structure.\n'
	_merge_flextext_xsl_data_ +=b'\t\t\tThis approach is preferred because all we want to do is add the new morpheme glosses and parts of speech from FLEx -->\n'
	_merge_flextext_xsl_data_ +=b'\t<xsl:template match="@*|node()">\n'
	_merge_flextext_xsl_data_ +=b'\t<xsl:copy>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t<xsl:apply-templates select="@*|node()"/>\n'
	_merge_flextext_xsl_data_ +=b'\t\t</xsl:copy>\n'
	_merge_flextext_xsl_data_ +=b'\t</xsl:template>\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t<!-- Merge the phrase from the original (ELAN) .flextext and the (FLEx) .flextext -->\n'
	_merge_flextext_xsl_data_ +=b'\t<xsl:template match="morph">\n'
	_merge_flextext_xsl_data_ +=b'\t\t<!-- If a line (in FLEx) is too long... it breaks each line into a phrase - even if the line is a single sentence.\n'
	_merge_flextext_xsl_data_ +=b'\t\t\tThis might apply sometimes to certain punctuation, as well.\n'
	_merge_flextext_xsl_data_ +=b'\t\t\tFortunately, multiple phrase will have the same common <paragraph> ancestor. (i.e. they share the same paragraph @guid)\n'
	_merge_flextext_xsl_data_ +=b'\t\t\tTherefore, we need to keep track of the paragraph and *not* the phrase to merge ELAN and FLEx files. -->\n'
	_merge_flextext_xsl_data_ +=b'\t\t<xsl:variable name="curphrase-guid" select="ancestor::phrase/@guid"></xsl:variable>\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t\t<!-- Keep track of the current morph(eme) within the phrase -->\n'
	_merge_flextext_xsl_data_ +=b'\t\t<xsl:variable name="curmorph"><xsl:number level="any" count="morph" from="phrase"/></xsl:variable>\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t\t<!-- Copy original elements.  Also overwrite \'type\' attribute and copy the applicable \'item\' elements from FLEx -->\n'
	_merge_flextext_xsl_data_ +=b'\t\t<xsl:copy>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t<!-- Copy the <phrase> and its attributes -->\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t<xsl:copy-of select="@*"/>\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t<!-- Overwrite \'type\' attribute from FLEx -->\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t<xsl:choose>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t<xsl:when test="not($FLExfile//phrase[@guid=$curphrase-guid]/ancestor::paragraph/descendant::morph[position()=$curmorph]/@type)">\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t\t<xsl:attribute name="type">stem</xsl:attribute>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t</xsl:when>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t<xsl:otherwise>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t\t<xsl:attribute name="type">\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t\t\t<xsl:value-of select="$FLExfile//phrase[@guid=$curphrase-guid]/ancestor::paragraph/descendant::morph[position()=$curmorph]/@type" />\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t\t</xsl:attribute>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t</xsl:otherwise>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t</xsl:choose>\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t<!-- Within the phrase, grab transription, translation, and comments (and whatever else) from original.\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t\tFLEx seems to jumbling these things...so prefer not to use from FLEx .flextext -->\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t<xsl:copy-of select="item"/>\n'
	_merge_flextext_xsl_data_ +=b'\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t<!-- Copy the applicable \'item\' elements from FLEx.  Add a blank one if there isn\'t one. -->\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t<xsl:choose>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t<xsl:when test="not($FLExfile//phrase[@guid=$curphrase-guid]/ancestor::paragraph/descendant::morph[position()=$curmorph]/item[@type=\'gls\'])">\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t\t<item type="gls" lang="en"/>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t</xsl:when>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t<xsl:otherwise>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t\t<xsl:copy-of select="$FLExfile//phrase[@guid=$curphrase-guid]/ancestor::paragraph/descendant::morph[position()=$curmorph]/item[@type=\'gls\']"/>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t</xsl:otherwise>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t</xsl:choose>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t<xsl:choose>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t<xsl:when test="not($FLExfile//phrase[@guid=$curphrase-guid]/ancestor::paragraph/descendant::morph[position()=$curmorph]/item[@type=\'msa\'])">\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t\t<item type="msa" lang="en"/>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t</xsl:when>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t<xsl:otherwise>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t\t<xsl:copy-of select="$FLExfile//phrase[@guid=$curphrase-guid]/ancestor::paragraph/descendant::morph[position()=$curmorph]/item[@type=\'msa\']"/>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t\t</xsl:otherwise>\n'
	_merge_flextext_xsl_data_ +=b'\t\t\t</xsl:choose>\n'
	_merge_flextext_xsl_data_ +=b'\t\t</xsl:copy>\n'
	_merge_flextext_xsl_data_ +=b'\t</xsl:template>\n'
	_merge_flextext_xsl_data_ +=b'</xsl:stylesheet>\n'
	#
	with open(_XSL_FLEXTEXT_MERGE_PATH_, 'wb') as _merge_flextext_xsl_:
		_merge_flextext_xsl_.write(_merge_flextext_xsl_data_)
	#

def output_merge_pfsx_xsl():
	_merge_pfsx_xsl_data_ =b'<?xml version="1.0" encoding="UTF-8"?>\n'
	_merge_pfsx_xsl_data_ +=b'<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"\n'
	_merge_pfsx_xsl_data_ +=b'\txmlns:xs="http://www.w3.org/2001/XMLSchema"\n'
	_merge_pfsx_xsl_data_ +=b'\txmlns:math="http://www.w3.org/2005/xpath-functions/math"\n'
	_merge_pfsx_xsl_data_ +=b'\texclude-result-prefixes="xs math"\n'
	_merge_pfsx_xsl_data_ +=b'\tversion="3.0">\n'
	_merge_pfsx_xsl_data_ +=b'\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:variable name="paramsDoc" select="if (doc-available(\'input:request\')) then doc(\'input:request\') else ()"/>\n'
	_merge_pfsx_xsl_data_ +=b'\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:output indent="yes" media-type="xml"/>\n'
	_merge_pfsx_xsl_data_ +=b'\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:preserve-space elements="*"/>\n'
	_merge_pfsx_xsl_data_ +=b'\n'
	_merge_pfsx_xsl_data_ +=b'\t<!-- command line parameter for giving the name of the interlinearised file  -->\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:param name="mergepfsx"/>\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:variable name="mergepfsxfile" select="document($mergepfsx)" />\n'
	_merge_pfsx_xsl_data_ +=b'\n'
	_merge_pfsx_xsl_data_ +=b'\t<!-- And maybe let\'s add a parameter to say whether you want to overwrite previous transcript/translation tiers (default value set to "yes"). Because sometimes the interlin process will lead to editing of these. -->\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:param name="overwrite" select="no"/>\n'
	_merge_pfsx_xsl_data_ +=b'\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:template match="@*|node()">\n'
	_merge_pfsx_xsl_data_ +=b'\t\t<xsl:copy>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t<xsl:apply-templates select="@*|node()"/>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t</xsl:copy>\n'
	_merge_pfsx_xsl_data_ +=b'\t</xsl:template>\n'
	_merge_pfsx_xsl_data_ +=b'\n'
	_merge_pfsx_xsl_data_ +=b'\t<!-- Do nothing with these elements (from FLEX file) -->\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:template match="preferences/pref[not(@key=\'MultiTierViewer.ActiveTierName\')]"/>\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:template match="preferences/prefList[not(@key=\'MultiTierViewer.TierOrder\')]"/>\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:template match="preferences/prefGroup[not(@key=\'TierColors\')]"/>\n'
	_merge_pfsx_xsl_data_ +=b'\n'
	_merge_pfsx_xsl_data_ +=b'\t<!-- Merge the preferences from pre-FLEx and post-merge-FLEx -->\n'
	_merge_pfsx_xsl_data_ +=b'\t<xsl:template match="preferences">\n'
	_merge_pfsx_xsl_data_ +=b'\t\t<!--  -->\n'
	_merge_pfsx_xsl_data_ +=b'\t\t<xsl:copy>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t<xsl:copy-of select="pref[not(@key=\'MultiTierViewer.ActiveTierName\')]"/>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t<xsl:copy-of select="prefList[not(@key=\'MultiTierViewer.TierOrder\')]"/>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t<xsl:copy-of select="prefGroup[not(@key=\'TierColors\')]"/>\n'
	_merge_pfsx_xsl_data_ +=b'\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t<!-- Apply template to FLEx file to get all the morphemes!! -->\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t<xsl:apply-templates select="$mergepfsxfile/preferences/node()"/>\n'
	_merge_pfsx_xsl_data_ +=b'\n'	
	_merge_pfsx_xsl_data_ +=b'\t\t\t<!-- Can\'t directly copy the original (pre-FLEx) fonts (if they exist) -->\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t<!-- because the tier names changed.  So, copying the TierColors (post-FLEx) -->\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t<!-- and copying the TierFonts (pre-FLEx) into them -->\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t<prefGroup key="TierFonts">\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t<xsl:for-each select="$mergepfsxfile/preferences/prefGroup[@key=\'TierColors\']/pref">\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t\t<xsl:variable name="key_value" select="current()/@key"></xsl:variable>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t\t<xsl:variable name="curtierfont"><xsl:number select="current()"/></xsl:variable>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t\t<xsl:element name="pref">\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t\t\t<!-- Copy the new (post-FLEx) key attribute -->\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t\t\t<xsl:attribute name="key">\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t\t\t\t<xsl:value-of select="$key_value" />\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t\t\t</xsl:attribute>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t\t\t<!-- Copy the original (pre-FLEx) Font details for this tier -->\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t\t\t<xsl:copy-of select="//prefGroup[@key=\'TierFonts\']/pref[number($curtierfont)]/Object"/>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t\t</xsl:element>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t</xsl:for-each>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t\t</prefGroup>\n'
	_merge_pfsx_xsl_data_ +=b'\t\t</xsl:copy>\n'
	_merge_pfsx_xsl_data_ +=b'\t</xsl:template>\n'
	_merge_pfsx_xsl_data_ +=b'</xsl:stylesheet>\n'
	#
	with open(_XSL_PFSX_MERGE_PATH_, 'wb') as _merge_pfsx_xsl_:
		_merge_pfsx_xsl_.write(_merge_pfsx_xsl_data_)
	#
#
_BACKUP_DIR_ = '_ELAN-FLEx_flextext+pfsx_BACKUP_'
_CURRENT_BACKUP_DIR_ = '_DEFAULT_'
#
_SAXON9HE_PATH_ = 'E:\\SAJOLANG_recordings_from_SD_card\\copied+backed_up\\SaxonHE9-9-1-5J\\saxon9he.jar'
_ELAN_EXE_PATH_ = 'C:\\Program Files\\ELAN_5.9\\ELAN.exe'
#
_ELAN_EAF_PATH_ = ''
_ELAN_PATH_ = ''
_FLEX_PATH_ = ''
#
############################################
# CREATE TEMP DIRECTORY
############################################
tmp = os.path.join(tempfile.gettempdir(), 'ELAN-FLEx-interlinear-import+export.tmp', '.{}'.format(hash(os.times())))
if os.path.isdir(tmp):
	tmp_sequence = 2
	while os.path.isdir(tmp + str(tmp_sequence)):
		tmp_sequence = tmp_sequence + 1
	os.makedirs(tmp + str(tmp_sequence))
else:
	os.makedirs(tmp)
#
_REMOVE_FLEX_FLEXTEXT_PUNCT_XSL_FILENAME_ = 'remove_FLEx_flextext_punct.xsl'
_MERGE_ELAN_FLEX_FLEXTEXT_XSL_FILENAME_ = 'merge_ELAN_FLEx_flextext.xsl'
_MERGE_ELAN_PFSX_XSL_FILENAME_ = 'merge_pfsx.xsl'
#
_XSL_REMOVE_FLEX_FLEXTEXT_PUNCT_PATH_ = os.path.join(tmp, _REMOVE_FLEX_FLEXTEXT_PUNCT_XSL_FILENAME_)
_XSL_FLEXTEXT_MERGE_PATH_ = os.path.join(tmp, _MERGE_ELAN_FLEX_FLEXTEXT_XSL_FILENAME_)
_XSL_PFSX_MERGE_PATH_ = os.path.join(tmp, _MERGE_ELAN_PFSX_XSL_FILENAME_)
#
output_remove_FLEx_flextext_punct_xsl()
time.sleep(1)
output_merge_flextext_xsl()
time.sleep(1)
output_merge_pfsx_xsl()
time.sleep(1)
############################################
#
def get_str_overlap(s1, s2):
	s = difflib.SequenceMatcher(None, s1, s2)
	pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2)) 
	return s1[pos_a:pos_a+size]

##ORIGINAL BEFORE THE EAF drag-n-drop
#window_height = 600
#window_width = 725
##NEW AFTER THE EAF drag-n-drop
window_height = 725
#window_width = 725
window_width = 700
#center_window(725, 600)

def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


def handle(event):
    files = root.tk.splitlist(event.data)
    for filename in files:
        event.widget.insert('end', filename)

def callback(event):
	root.focus()

def valid_eaf(filename):
	return pathlib.Path(filename).suffix == '.eaf'

def valid_flextext(filename):
	return pathlib.Path(filename).suffix == '.flextext'

def clear_display():
	cmd_prompt.delete('1.0', END)

def append_to_display(text, fontfamily='', fontsize=12, weight='', color='White', justify='left'):
	#tag_name = "color-" + color
	tag_name = 'fontfamily-' + fontfamily + ';fontsize-' + str(fontsize) + ';weight-' + weight + ';color-' + color + ';justify-' + justify
	cmd_prompt.tag_configure(tag_name, foreground=color, font=(fontfamily, fontsize, weight), justify=justify)
	cmd_prompt.insert(END, text + "\n", tag_name)

def drop(event, stringvar):
	global _CURRENT_BACKUP_DIR_
	global _ELAN_EAF_PATH_
	global _ELAN_PATH_
	global _FLEX_PATH_
	if event.data[0] == '{' and event.data[-1] == '}':
		dragged_file_data = event.data[1:-1]
	else:
		dragged_file_data = event.data
	FILE_DIR_PATH, FILENAME = os.path.split(dragged_file_data)
	
	if valid_eaf(FILENAME) or valid_flextext(FILENAME):
		if valid_eaf(FILENAME) and event.widget.grid_info()["row"] == 1:
			elan_eaf_entry_filename.config(text=FILENAME)
			elan_eaf_entry_filename.config(padx=0,pady=0)
			elan_eaf_entry_filename.config(height=10)
			elan_eaf_entry_filename.config(width=10)
			elan_eaf_entry_filename.grid(row=1,column=0,columnspan=2,padx=150,pady=5,sticky=W+E+N+S)
			#
			append_to_display('ELAN .eaf linked', fontsize=12, color='Green')
			_ELAN_EAF_PATH_ = FILE_DIR_PATH + '/' + FILENAME
		elif valid_flextext(FILENAME):
			if event.widget.grid_info()["column"] == 0:
				elan_entry_filename.config(text=FILENAME)
				elan_entry_filename.config(padx=0,pady=0)
				elan_entry_filename.config(height=10)
				elan_entry_filename.config(width=10)
				elan_entry_filename.grid(row=2,column=0,padx=5,pady=5,sticky=W+E+N+S)
				#
				append_to_display('ELAN .flextext linked', fontsize=12, color='Green')
				_ELAN_PATH_ = FILE_DIR_PATH + '/' + FILENAME
			else:
				flex_entry_filename.config(text=FILENAME)
				flex_entry_filename.config(padx=0,pady=0)
				flex_entry_filename.config(height=10)
				flex_entry_filename.config(width=10)
				flex_entry_filename.grid(row=2,column=1,padx=5,pady=5,sticky=W+E+N+S)
				#
				append_to_display('FLEx .flextext linked', fontsize=12, color='Green')
				_FLEX_PATH_ = FILE_DIR_PATH + '/' + FILENAME
		
		if elan_eaf_entry_filename['text'] is not None and \
				elan_eaf_entry_filename['text'] is not '' and \
				elan_entry_filename['text'] is not None and \
				elan_entry_filename['text'] is not '' and \
				flex_entry_filename['text'] is not None and \
				flex_entry_filename['text'] is not '':
			############################################
			# CREATE BACKUP DIRECTORY
			############################################
			elan_ear_dir, elan_eaf_filename = os.path.split(_ELAN_EAF_PATH_)
			elan_flextext_dir, elan_flextext_filename = os.path.split(_ELAN_PATH_)
			flex_flextex_dir, flex_flextex_filename = os.path.split(_FLEX_PATH_)
			if elan_ear_dir == elan_flextext_dir and elan_flextext_dir == flex_flextex_dir:
				_CURRENT_BACKUP_DIR_ = os.path.join(elan_flextext_dir, _BACKUP_DIR_, '_BACKUP_{}_'.format(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())))
				os.makedirs(_CURRENT_BACKUP_DIR_)
				merge_button.config({'background':'chartreuse3'})
				#
				shutil.copy(_ELAN_EAF_PATH_, os.path.join(_CURRENT_BACKUP_DIR_, elan_eaf_filename))
				shutil.copy(os.path.splitext(_ELAN_EAF_PATH_)[0]+'.pfsx', os.path.join(_CURRENT_BACKUP_DIR_, os.path.splitext(elan_eaf_filename)[0]+'.pfsx'))
				#
				shutil.copy(_ELAN_PATH_, os.path.join(_CURRENT_BACKUP_DIR_, elan_flextext_filename))
				shutil.copy(_FLEX_PATH_, os.path.join(_CURRENT_BACKUP_DIR_, flex_flextex_filename))
				#
				append_to_display('\nWARNING:  When you press MERGE button,', color='Yellow', justify='center')
				append_to_display('!!! Wait until ELAN closes before using mouse or keyboard !!!', color='Yellow', justify='center')
			else:
				append_to_display('\n\tWARNING:  .eaf/.flextext files are in different directories.\n', color='Yellow')
				append_to_display('\t!!This is probably going to cause unexpected behavior!!\n', color='Yellow')
			############################################
	else:
		append_to_display('Invalid .flextext:\t'+FILE_DIR_PATH+'\\'+FILENAME+'\n', color='Red')
		append_to_display('Please try again.\n\n', color='Red')

def merge_button_pressed():
	if merge_button['text'] == 'Quit':
		root.destroy()
		
	## When button is pressed, the ELAN and FLEx files may not have been identified yet
	## If not, just ignore the button push
	elif _ELAN_PATH_ is not None and _FLEX_PATH_ is not None and\
			_ELAN_PATH_ != r'' and _FLEX_PATH_ != r'' and\
			_ELAN_PATH_ != '' and _FLEX_PATH_ != '':
		#
		_flex_flextext_nopunct_dir_, _flex_flextext_nopunct_filename_= remove_FLEx_flextext_punct(_FLEX_PATH_)
		#_FLEX_NOPUNCT_PATH_ = os.path.join(_flex_flextext_nopunct_dir_, _flex_flextext_nopunct_filename_)
		_FLEX_NOPUNCT_PATH_ = _flex_flextext_nopunct_dir_ +'/'+ _flex_flextext_nopunct_filename_
		#print(_ELAN_PATH_)
		#print(_FLEX_PATH_)
		#print(_FLEX_NOPUNCT_PATH_)
		shutil.copy(os.path.join(_flex_flextext_nopunct_dir_, _flex_flextext_nopunct_filename_), os.path.join(_CURRENT_BACKUP_DIR_, _flex_flextext_nopunct_filename_))
		#
		#_merge_flextext_dir_, _merge_flextext_filename_ = merge_flextext_files(_ELAN_PATH_, _FLEX_PATH_)
		_merge_flextext_dir_, _merge_flextext_filename_ = merge_flextext_files(_ELAN_PATH_, _FLEX_NOPUNCT_PATH_)
		#
		#print('Finished something1.')
		#append_to_display('Finished something1.\n', fontsize=16, color='White')
		#
		shutil.copy(os.path.join(_merge_flextext_dir_, _merge_flextext_filename_), os.path.join(_CURRENT_BACKUP_DIR_, _merge_flextext_filename_))
		#
		#print('Finished something2.')
		#append_to_display('Finished something2.\n', fontsize=16, color='White')
		#
		_merge_eaf_path_, _merge_pfsx_path_ = save_flextext_as_eaf(_merge_flextext_dir_, _merge_flextext_filename_)
		#
		#print('Finished creating MERGED .eaf and .pfsx files (in temp directory).')
		#append_to_display('Finished creating MERGED .eaf and .pfsx files (in temp directory).\n', fontsize=16, color='White')
		#
		shutil.copy(_merge_eaf_path_, os.path.join(_CURRENT_BACKUP_DIR_, os.path.split(_merge_eaf_path_)[1]))
		shutil.copy(_merge_pfsx_path_, os.path.join(_CURRENT_BACKUP_DIR_, os.path.split(_merge_pfsx_path_)[1]))
		#
		#print('Copied MERGED .eaf and .pfsx files to original directory.')
		#append_to_display('Copied MERGED .eaf and .pfsx files to original directory.\n', fontsize=16, color='White')
		#
		time.sleep(2)
		#
		merge_pfsx(os.path.splitext(_ELAN_EAF_PATH_)[0] + '.pfsx', _merge_pfsx_path_)
		#
		#print('Updated MERGED .eaf and .pfsx files to correct tier labels.')
		#append_to_display('Updated MERGED .eaf and .pfsx files to correct tier labels.\n', fontsize=16, color='White')
		#
		## RENAME TIERS
		_merge_renamed_eaf_path_, _merge_renamed_pfsx_path_ = rename_merged_flextext_pfsx_tiers(_merge_eaf_path_, _merge_pfsx_path_)
		#
		time.sleep(2)
		#
		## Backup the tier-renamed merge EAF and PFSX files
		shutil.copy(_merge_renamed_eaf_path_, os.path.join(_CURRENT_BACKUP_DIR_, os.path.split(_merge_renamed_eaf_path_)[1]))
		shutil.copy(_merge_renamed_pfsx_path_, os.path.join(_CURRENT_BACKUP_DIR_, os.path.split(_merge_renamed_pfsx_path_)[1]))
		#
		time.sleep(2)
		#
		os.remove(_FLEX_NOPUNCT_PATH_)
		#
		## Now, delete the original merge files and replace them with the tier-renamed ones
		os.remove(_merge_eaf_path_)
		os.remove(_merge_pfsx_path_)
		#
		time.sleep(2)
		#
		shutil.move(_merge_renamed_eaf_path_, _merge_eaf_path_)
		shutil.move(_merge_renamed_pfsx_path_, _merge_pfsx_path_)
		#########################
		#
		clear_display()
		#
		print('Congratulations!  You finished merging!')
		append_to_display('Merging complete!\n', fontsize=16, color='Green')
		append_to_display('\tDirectory:  ', fontsize=14, color='Green')
		append_to_display(os.path.split(_merge_eaf_path_)[0]+'\n', fontsize=12, color='White')
		append_to_display('\tEAF:  ', fontsize=14, color='Green')
		append_to_display(os.path.split(_merge_eaf_path_)[1]+'\n', fontsize=12, color='White')
		append_to_display('\tPFSX:  ', fontsize=14, color='Green')
		append_to_display(os.path.split(_merge_pfsx_path_)[1]+'\n', fontsize=12, color='White')
		#
		merge_button.config(text='Quit')
		#
	else:
		append_to_display('Please drag and drop your files first!\n', fontsize=16, color='Yellow')
	#

def remove_FLEx_flextext_punct(_flex_path_):
	## Get the filename separated from the directory path
	_flex_flextext_dir_, _flex_flextext_filename_ = os.path.split(_flex_path_)
	
	_flex_flextext_filename_ = os.path.splitext(_flex_flextext_filename_)[0]
	
	## If the intended output file already exists, then put a number at the end
	if os.path.isfile(os.path.join(_flex_flextext_dir_, _flex_flextext_filename_) + '_NOPUNCT.flextext'):
		#
		_flex_flextext_nopunct_path_pre_ = _flex_flextext_filename_ + '_NOPUNCT('
		#
		_flex_flextext_nopunct_path_post_ = ').flextext'
		sequence = 2
		#
		while os.path.isfile(_flex_flextext_nopunct_path_pre_ + str(sequence) + _flex_flextext_nopunct_path_post_):
			sequence = int(sequence or 0) + 1
		#
		_flex_flextext_nopunct_path_ = _flex_flextext_nopunct_path_pre_ + str(sequence) + _flex_flextext_nopunct_path_post_
	else:
		_flex_flextext_nopunct_path_ = _flex_flextext_filename_ + '_NOPUNCT.flextext'
	#
	_flex_flextext_nopunct_path_ = os.path.join(_flex_flextext_dir_,_flex_flextext_nopunct_path_)
	#
	command = ['java',
				'-jar',
				'-Xmx1024m',
				_SAXON9HE_PATH_,#
				'-t',
				'-xsl:'+_XSL_REMOVE_FLEX_FLEXTEXT_PUNCT_PATH_,## XSL transformation stylesheet
				'overwrite=no',
				'-s:' + _flex_path_,# ELAN .flextext
				#pathlib.Path(_flex_path_).as_uri()
				'-o:' + _flex_flextext_nopunct_path_]# MERGED .flextext file
	#
	p = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	return_code, output, errors = p.returncode, p.stdout, p.stderr
	#print(return_code)
	#print(output)
	#print(_flex_flextext_nopunct_path_)
	#
	return os.path.split(_flex_flextext_nopunct_path_)
	#

def merge_flextext_files(_elan_path_, _flex_path_):
	## We are assuming that the filenames are nearly identical (including the directory location)
	## Get the overlapping portion
	_merge_flextext_overlap_ = get_str_overlap(_elan_path_, _flex_path_)
	
	## Get the overlapping filename separated from the directory path
	_merge_flextext_dir_, _merge_flextext_filename_ = os.path.split(_merge_flextext_overlap_)
	
	## If the filename is very short... the filenames may be very different??
	if len(_merge_flextext_filename_) < 5:
		#
		_merge_flextext_path_ = os.path.join(_merge_flextext_dir_, 'ELAN-FLEx_interlinear_MERGED.flextext')
	else:
		## If the intended output file already exists, then put a number at the end
		if os.path.isfile(os.path.join(_merge_flextext_dir_, _merge_flextext_filename_) + '_MERGED.flextext'):
			#
			_merge_flextext_path_pre_ = _merge_flextext_overlap_ + '_MERGED('
			#
			_merge_flextext_path_post_ = ').flextext'
			sequence = 2
			#
			while os.path.isfile(_merge_flextext_path_pre_ + str(sequence) + _merge_flextext_path_post_):
				sequence = int(sequence or 0) + 1
			#
			_merge_flextext_path_ = _merge_flextext_path_pre_ + str(sequence) + _merge_flextext_path_post_
		else:
			_merge_flextext_path_ = _merge_flextext_overlap_ + '_MERGED.flextext'
	#
	#print(_elan_path_)
	#print(pathlib.Path(_flex_path_))
	#print(_merge_flextext_path_)
	#
	command = ['java',
				'-jar',
				'-Xmx1024m',
				_SAXON9HE_PATH_,#
				'-t',
				'-xsl:'+_XSL_FLEXTEXT_MERGE_PATH_,## XSL transformation stylesheet
				'overwrite=no',
				'-s:' + _elan_path_,# ELAN .flextext
				'FLEx=' + pathlib.Path(_flex_path_).as_uri(),# FLEx .flextext (as URI because it is stored as XSL variable)
				'-o:' + _merge_flextext_path_]# MERGED .flextext file
	#
	p = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	return_code, output, errors = p.returncode, p.stdout, p.stderr
	#print(return_code)
	#print(output)
	#print(errors)
	#
	return os.path.split(_merge_flextext_path_)
	#

def save_flextext_as_eaf(merge_flextext_dir, merge_filename):
	#
	#global tmp
	#
	_merge_flextext_filename_no_ext_ = os.path.splitext(merge_filename)[0]
	#MERGE_FILENAME_TEMP = merge_filename.replace('[', '+').replace(']', '+') # There is a bug in ELAN if filename or path has [ or ] for .flextext files
	_merge_flextext_filename_temp_ = merge_filename.replace('[', '+').replace(']', '+') # There is a bug in ELAN if filename or path has [ or ] for .flextext files
	#
	_merge_flextext_path_temp_ = os.path.join(tmp, _merge_flextext_filename_temp_)
	#temp_dir, temp_filename = os.path.split(_merge_flextext_path_temp_)
	#
	shutil.copy(os.path.join(merge_flextext_dir, merge_filename), _merge_flextext_path_temp_)
	#
	subprocess.Popen(_ELAN_EXE_PATH_)
	#
	while (not pyautogui.getWindowsWithTitle('ELAN ')):
		time.sleep(2)
	win = pyautogui.getWindowsWithTitle('ELAN ')[0]#
	win.activate()
	#
	############################################
	# IMPORT .flextext
	############################################
	pyautogui.press("alt")
	pyautogui.press("f")
	pyautogui.press("i")
	pyautogui.press("f")
	#time.sleep(2)
	####
	while (not pyautogui.getWindowsWithTitle('Import FLEx')):
		time.sleep(1)
	win = pyautogui.getWindowsWithTitle('Import FLEx')[0]#
	win.activate()
	#time.sleep(1)
	####
	pyautogui.press("tab")
	pyautogui.press("space")
	####
	while (not pyautogui.getWindowsWithTitle('Select')):
		time.sleep(1)
	win = pyautogui.getWindowsWithTitle('Select')[0]#
	win.activate()
	time.sleep(3)
	####
	pyautogui.hotkey("alt","n")
	time.sleep(1)
	pyautogui.hotkey("alt","n")
	pyautogui.hotkey("alt","n")
	time.sleep(1)
	pyperclip.copy(_merge_flextext_path_temp_)
	pyautogui.typewrite(pyperclip.paste())
	#
	time.sleep(1)
	pyautogui.press("tab")
	pyautogui.press("tab")
	pyautogui.press("space")
	#time.sleep(3)
	#time.sleep(100)
	#
	####
	while (pyautogui.getWindowsWithTitle('Select')):
		time.sleep(1)
	win = pyautogui.getWindowsWithTitle('Import FLEx')[0]#
	win.activate()
	#time.sleep(1)
	####
	#YES 3x
	pyautogui.hotkey("shift","tab")
	pyautogui.hotkey("shift","tab")
	pyautogui.hotkey("shift","tab")
	#
	pyautogui.press("space")
	####
	#time.sleep(18)
	while (pyautogui.getWindowsWithTitle('Initializaing...')):
		time.sleep(2)
	win = pyautogui.getWindowsWithTitle('ELAN ')[0]#
	win.activate()
	#time.sleep(1)
	####
	############################################

	############################################
	# SAVE .eaf
	############################################
	pyautogui.press("alt")
	pyautogui.press("f")
	pyautogui.press("s")
	####
	while (not pyautogui.getWindowsWithTitle('Save As')):
		time.sleep(2)
	win = pyautogui.getWindowsWithTitle('Save As')[0]#
	win.activate()
	#time.sleep(1)
	####
	pyautogui.hotkey("ctrl","a")
	pyautogui.press("delete")
	#
	pyperclip.copy(os.path.join(tmp, _merge_flextext_filename_no_ext_ + '.eaf'))
	pyautogui.typewrite(pyperclip.paste())
	#pyautogui.typewrite(os.path.join(tmp, _merge_flextext_filename_no_ext_ + '.eaf'))
	#MERGE_FILENAME_NO_EXT
	pyautogui.hotkey("ctrl","enter")
	############################################
	####
	#time.sleep(4)
	while (pyautogui.getWindowsWithTitle('Save As')):
		time.sleep(2)
	win = pyautogui.getWindowsWithTitle('ELAN ')[0]#
	win.activate()
	#time.sleep(1)
	####
	pyautogui.press("alt")
	pyautogui.press("f")
	pyautogui.press("x")
	#
	## Determine the full path for the EAF and PFSX files
	## (i.e. where they *should* exist - not the temporary directory versions)
	_merge_eaf_path_ = os.path.join(merge_flextext_dir, _merge_flextext_filename_no_ext_ + '.eaf')
	_merge_pfsx_path_ = os.path.join(merge_flextext_dir, _merge_flextext_filename_no_ext_ + '.pfsx')
	#
	print('Finished something3.')
	append_to_display('Finished something3.\n', fontsize=16, color='White')
	#
	#
	print(str(os.path.join(tmp, _merge_flextext_filename_no_ext_ + '.eaf')))
	append_to_display(str(os.path.join(tmp, _merge_flextext_filename_no_ext_ + '.eaf'))+'.\n', fontsize=16, color='White')
	#
	time.sleep(5)
	#
	## Copy the temporary EAF and PFSX back to the directory where original FLEXTEXT file is
	shutil.copy(os.path.join(tmp, _merge_flextext_filename_no_ext_ + '.eaf'), _merge_eaf_path_)
	shutil.copy(os.path.join(tmp, _merge_flextext_filename_no_ext_ + '.pfsx'), _merge_pfsx_path_)
	#
	print('Finished something4.')
	append_to_display('Finished something4.\n', fontsize=16, color='White')
	#
	return _merge_eaf_path_, _merge_pfsx_path_
	#

def merge_pfsx(elan_pfsx_path, merge_pfsx_path):
	#
	_merge_pfsx_dir_, _merge_pfsx_filename_ = os.path.split(merge_pfsx_path)
	_merge_pfsx_filename_no_ext = os.path.splitext(_merge_pfsx_filename_)[0]
	#
	_merged_w_orig_pfsx_path_ = os.path.join(_merge_pfsx_dir_, _merge_pfsx_filename_no_ext + '_[merged].pfsx')
	#
	command = ['java',
				'-jar',
				'-Xmx1024m',
				_SAXON9HE_PATH_,
				'-t',
				'-xsl:'+_XSL_PFSX_MERGE_PATH_,# XSL transformation stylesheet
				'overwrite=no',
				'-s:'+elan_pfsx_path.replace('_from_ELAN',''),# ELAN .flextext
				'mergepfsx='+pathlib.Path(merge_pfsx_path).as_uri(),# .flextext TO MERGE
				'-o:'+_merged_w_orig_pfsx_path_]# MERGED .flext file
	p = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	return_code, output, errors = p.returncode, p.stdout, p.stderr
	#print(return_code)
	#print(output)
	#print(errors)
	#
	os.remove(merge_pfsx_path)
	#
	shutil.move(_merged_w_orig_pfsx_path_, merge_pfsx_path)
#################################################################################
def rename_merged_flextext_pfsx_tiers(merge_eaf_path, merge_pfsx_path):
	#
	input_filenames = [merge_eaf_path]
	input_filenames.append(merge_pfsx_path)
	#
	renamed_filenames = [os.path.splitext(input_filenames[0])[0]+'_[tiers_renamed]'+os.path.splitext(input_filenames[0])[1]]
	renamed_filenames.append(os.path.splitext(input_filenames[1])[0]+'_[tiers_renamed]'+os.path.splitext(input_filenames[1])[1])

	# Keep track all the tier IDs which are replaced and what the new ID is
	# -- This is necessary because the pfsx (preference file) does not have PARTICIPANT information
	tiers = {}

	# Loop through each file
	for filename in input_filenames:
		# Tell user which file is being processed
		#print ("doing file... " + filename)
		
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
						
						#print(line)
						#print(not all_initials or (not tier_prefix in all_initials and not participant_initials in all_initials.values()))
						#print(not all_initials)
						#print(not tier_prefix in all_initials)
						#print(not participant_initials in all_initials.values())
						
						# If the all_initials dictionary has not been updated, then this tier_ID prefix-initials (key-value) pair must be added
						# Also, if the tier_ID prefix-initials (key-value) pair doesn't exist in the dictionary, we must add it
						#if not all_initials and not tier_prefix in all_initials and not participant_initials in all_initials.values():
						if not all_initials or (not tier_prefix in all_initials and not participant_initials in all_initials.values()):
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
						#print(line)
						#print(tier_prefix)
						#print(all_initials)
						#print(all_initials.get(tier_prefix))
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
						############################################################
						# Replace "...morph-type-..." with "ZZ_morph-type"
						line = re.sub(b'([^"]*)morph-type', b'%s_morph-type'%(all_initials.get(tier_prefix)), line)
						############################################################
						
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
			#
	#
	return renamed_filenames[0], renamed_filenames[1]

############################################################################################################################################
## GUI Setup
############################################################################################################################################
root = TkinterDnD.Tk()

cmd_prompt = Text(root, height=20)
cmd_prompt.config({"background":"Black","foreground":"White"})
append_to_display('\n Please drag and drop the following files:\n', fontsize=14, weight='bold')
append_to_display('\t (1)  (original) ELAN .eaf file\n', weight='bold')
append_to_display('\t (2)  ELAN .flextext file\n', weight='bold')
append_to_display('\t (3)  FLEx .flextext file\n\n', weight='bold')
################
################
elan_eaf_entry_sv = StringVar()
elan_eaf_entry_sv.set('Drop ELAN .eaf Here...')
elan_eaf_entry = Entry(root, textvar=elan_eaf_entry_sv, justify='center', font='bold')
elan_eaf_entry.config({'disabledbackground':'Light Gray', 'disabledforeground':'Black', 'relief':'groove', 'state':'disabled'})
elan_eaf_entry.drop_target_register(DND_FILES)
#elan_eaf_entry.dnd_bind('<<Drop>>', drop)
elan_eaf_entry.dnd_bind('<<Drop>>', lambda event, stringvar=elan_eaf_entry_sv: drop(event, stringvar))
elan_eaf_entry.bind('<1>', callback)
elan_eaf_entry.bind('<2>', callback)
################
################
elan_entry_sv = StringVar()
elan_entry_sv.set('Drop ELAN .flextext Here...')
elan_entry = Entry(root, textvar=elan_entry_sv, justify='center', font='bold')
elan_entry.config({'disabledbackground':'Light Gray', 'disabledforeground':'Black', 'relief':'groove', 'state':'disabled'})
elan_entry.drop_target_register(DND_FILES)
#elan_entry.dnd_bind('<<Drop>>', drop)
elan_entry.dnd_bind('<<Drop>>', lambda event, stringvar=elan_entry_sv: drop(event, stringvar))
elan_entry.bind('<1>', callback)
elan_entry.bind('<2>', callback)
################
################
flex_entry_sv = StringVar()
flex_entry_sv.set('Drop FLEx .flextext Here...')
flex_entry = Entry(root, textvar=flex_entry_sv, justify='center', font='bold')
flex_entry.config({'disabledbackground':'Light Gray', 'disabledforeground':'Black', 'relief':'groove', 'state':'disabled'})
flex_entry.drop_target_register(DND_FILES)
#flex_entry.dnd_bind('<<Drop>>', drop)
flex_entry.dnd_bind('<<Drop>>', lambda event, stringvar=flex_entry_sv: drop(event, stringvar))
flex_entry.bind('<1>', callback)
flex_entry.bind('<2>', callback)


cmd_prompt.grid(row=0,column=0,columnspan=2,sticky=W+E+N+S)

elan_eaf_entry.grid(row=1,column=0,columnspan=2,padx=150,pady=5,sticky=W+E+N+S)

elan_entry.grid(row=2,column=0,padx=5,pady=5,sticky=W+E+N+S)
flex_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W+E+N+S)

merge_button = Button(root, text='Merge .flextext files', justify='center', font=(None, 14, 'bold'), command=merge_button_pressed)
merge_button.config({'background':'Indian Red'})
merge_button.grid(row=3,column=0,columnspan=2,sticky=W+E+N+S)


#font=("Helvetica", 16)
filename_font_size = 10
file_attached_image = PhotoImage(file='file_checkmark_4.gif')
elan_eaf_entry_filename = Label(root, text='', image=file_attached_image, justify='center', compound=TOP, font=(None, filename_font_size, 'bold'))
elan_eaf_entry_filename.config({'background':'Light Gray'})
elan_entry_filename = Label(root, text='', image=file_attached_image, justify='center', compound=TOP, font=(None, filename_font_size, 'bold'))
elan_entry_filename.config({'background':'Light Gray'})
flex_entry_filename = Label(root, text='', image=file_attached_image, justify='center', compound=TOP, font=(None, filename_font_size, 'bold'))
flex_entry_filename.config({'background':'Light Gray'})


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=20)
root.grid_rowconfigure(2, weight=20)
root.grid_rowconfigure(3, weight=1)
'''
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=6)
root.grid_rowconfigure(2, weight=1)
'''

root.config({"background":"Gray"})

#Explanation: ('width x height + X coordinate + Y coordinate')
#root.geometry("500x500+150+150")
center_window(window_width, window_height)

root.mainloop()
