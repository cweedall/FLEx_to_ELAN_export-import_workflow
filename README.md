# FLEx to ELAN export-import workflow (and scripts)
FLEx to ELAN {compatibility, roundtrip, import, export, transfer, workflow}

Fieldworks Language Explorer (FLEx) is a database to manage lexical and text items for a language.  It is especially helpful for the creation of dictionaries.  Website: <https://software.sil.org/fieldworks/>

ELAN is a tool to aid in annotation and transcription of audio/video recordings.  Website: <https://tla.mpi.nl/tools/tla-tools/elan/>

Both tools have their strengths and their functionality overlaps to some degree.  For this reason, many researchers wish to transfer an ELAN project or FLEx text to the opposite software application.  Although we can export a .FLExtext file from ELAN to FLEx with little problem, an interlinearized text from FLEx has some differences.  These include different tier names and some underlying structural changes which do not "play well" with ELAN.  This project provides some tools to return data to ELAN "as expected" from an end-user perspective.

##DISCLAIMER:

The authors of this project probaby have not tested every possible scenario.
**ALWAYS BACKUP YOUR DATA/FILES FIRST**
If you encounter unexpected results, contact us and let us know!  Lastly, although we attempt to automate this process as much as possible, there are several manual steps required - sorry, it's the nature of "the beast" (i.e. FLEx and ELAN).

##Exporting from ELAN to FLEx

(although focusing on FLEx-to-ELAN - we will assume some tier structures from ELAN.  Also a workfloww that we use with screenshots.  Details coming soon!!)

##Exporting from ELAN to FLEx

(This will be separated into several steps.  Exporting from FLEx.  Running XSL script to merge old/new .FLExtext.  Opening ELAN to import the merged data.  Save a new ELAN project (.eaf file).  Close ELAN.  Run a Python script and XSL script to merge the old and new (merged) ELAN preferences.  Open the ELAN project again and verify!  Details coming soon!!)


**ALWAYS BACKUP YOUR DATA/FILES FIRST**

**KEEP BACKUPS IN A "BACKUP" FOLDER FOR ALL FILES IN THIS WORKFLOW**
