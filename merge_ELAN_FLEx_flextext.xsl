<?xml version="1.0" encoding="UTF-8"?>
<!-- merge_ELAN_FLEx_flextext.xsl

###############
AUTHORS:
	John Mansfield
	Christopher Weedall

###############
DATE:
	01 NOV 2019 (current version)

###############
DESCRIPTION:

This takes an ELAN .flextext transcription file (export FLExtext from ELAN), and combines it with the interlinear morphological analysis of the same transcript, produced in Flex. This is necessary because not all ELAN tiers survive the import-interlinearise-export journey through Flex. Custom tiers are simply removed by FLEx. So we recombine FLEx's morphological analysis with the origianl .flextxt file exported from ELAN.  The FLEx .flextext file also has a different structure and sometimes creates multiple top-level tiers (from FLEx) for a single top-level tier (in ELAN).

###############
REQUIREMENTS:
	JAVA must be installed.
		- See this https://java.com/en/download/help/download_options.xml
		
	SAXON must be installed.
		- Can be downloaded (as of 01 NOV 2019) at:
			http://www.saxonica.com/download/java.xml ===> Click "Download Latest Version"
			
			- You can download the .zip version and extract to a directory of your choosing
			- Lets assume the root directory (on Windows) or in the user's home (on POSIX)
			- In other words, we assume:
				C:\saxon (Windows)
				~/saxon (Windows)
				
		- From installation directory, we need to call Java to run the Saxon .jar file

########################
HOW TO RUN THIS SCRIPT:
########################

1) Open a command prompt / terminal -> in the directory where the .flextext files are located.
2) Follow the usage/examples below for your operating system.
=============================================================================================================================
::NOTE::
	Windows installation directory:		C:\saxon\
	Mac/Linux installation directory:	~/saxon (where ~ means "user's home directory")
=============================================================================================================================

###############
WINDOWS USAGE:
###############

java -jar -Xmx1024m "PATH\TO\saxon9he.jar" -t -xsl:merge_ELAN_FLEx_flextext.xsl overwrite=no -s:[ELAN_FILENAME].flextext FLEx=[FLEx_FILENAME].flextext -o:[MERGED_FILENAME].flextext 

#################
WINDOWS EXAMPLE:
#################

java -jar -Xmx1024m "C:\saxon\saxon9he.jar" -t -xsl:merge_ELAN_FLEx_flextext.xsl overwrite=no -s:LangName_ELAN.flextext FLEx=LangName_FLEx.flextext -o:LangName_MERGED.flextext

####################################
POSIX USAGE: (Mac OSX, Unix, Linux)
####################################

java -jar -Xmx1024m "PATH/TO/saxon9he.jar" -t -xsl:merge_ELAN_FLEx_flextext.xsl overwrite=no -s:[ELAN_FILENAME].flextext FLEx=[FLEx_FILENAME].flextext -o:[MERGED_FILENAME].flextext 

######################################
POSIX EXAMPLE: (Mac OSX, Unix, Linux)
######################################

java -jar -Xmx1024m "~/saxon/saxon9he.jar" -t -xsl:merge_ELAN_FLEx_flextext.xsl overwrite=no -xsl:merge_ELAN_FLEx_flextext.xsl overwrite=no -s:LangName_ELAN.flextext FLEx=LangName_FLEx.flextext -o:LangName_MERGED.flextext

-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
	
	<xsl:output indent="yes" media-type="xml"/>

	<xsl:preserve-space elements="*"/>
	
	<!-- Verify the input file (the ELAN .flextext file) exists -->
	<xsl:variable name="ELANDocCheck" select="if (doc-available('input:request')) then doc('input:request') else ()"/>

	<!-- Path to the second input file (the FLEx .flextext file) -->
	<xsl:param name="FLEx"/>
	<!-- Verify the second input file (the FLEx .flextext file) exists -->
	<xsl:variable name="FLExDocCheck" select="if (doc-available('$FLEx')) then doc('$FLEx') else ()"/>
	<!-- Store the second (FLEx) input file as a variable -->
	<xsl:variable name="FLExfile" select="document($FLEx)" />
	
	<!-- Copy all nodes from input (ELAN) file to use as the default structure.
			This approach is preferred because all we want to do is add the new morpheme glosses and parts of speech from FLEx -->
	<xsl:template match="@*|node()">
		<xsl:copy>
			<xsl:apply-templates select="@*|node()"/>
		</xsl:copy>
	</xsl:template>

	<!-- Do nothing with these elements (from FLEX file) -->
	<xsl:template match="word[descendant::item[@type='punct']]"/><!-- FLEx separates punctuation into their own "words" -->
	<xsl:template match="word/item[@type='gls']"/><!-- Don't want the word gloss (only morpheme gloss) - PERHAPS MAKE THIS AN OPTION?? -->
	<xsl:template match="word/item[@type='pos']"/><!-- Don't want the word part of speech (only morpheme PoS - the 'msa') - PERHAPS MAKE THIS AN OPTION?? -->
	<xsl:template match="item[@type='cf']"/><!-- Don't want the citation form - PERHAPS MAKE THIS AN OPTION?? -->
	<!--<xsl:template match="morph/@type"/>-->
	<xsl:template match="item[@type = 'hn' or @type = 'variantTypes']"/><!-- Don't want the number or variant type -->
	
	<!-- Merge the phrase from the original (ELAN) .flextext and the (FLEx) .flextext -->
	<xsl:template match="phrase">
		<!-- The original (ELAN) <phrase> IDs -->
		<xsl:variable name="id" select="@guid"></xsl:variable>
		<!-- If a line (in FLEx) is too long... it breaks each line into a phrase - even if the line is a single sentence.
				This might apply sometimes to certain punctuation, as well.
				Fortunately, multiple phrase will have the same common <paragraph> ancestor. (i.e. they share the same paragraph @guid)
				Therefore, we need to keep track of the paragraph and *not* the phrase to merge ELAN and FLEx files. -->
		<xsl:variable name="curpara"><xsl:number select="ancestor::paragraph"/></xsl:variable>
		<xsl:copy>
			<!-- Copy the <phrase> and its attributes -->
			<xsl:copy-of select="@*"/>
			<!-- Within the phrase, grab transription, translation, and comments (and whatever else) from original.
					FLEx seems to jumbling these things...so prefer not to use from FLEx .flextext -->
			<xsl:copy-of select="item"/>
			
			<!-- Apply template to FLEx file to get all the morphemes!! (i.e. basically copying the morpheme nodes) -->
			<xsl:apply-templates select="$FLExfile//paragraph[number($curpara)]//words/node()"/>
		</xsl:copy>
	</xsl:template>
</xsl:stylesheet>
