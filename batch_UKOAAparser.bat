@echo off

REM Savind date and time of Batch execution for log files control ++++++++++++++++++++++++++++++++++++++
REM Taken from https://stackoverflow.com/questions/203090/how-do-i-get-current-date-time-on-the-windows-command-line-in-a-suitable-format
REM echo %mydate%_%mytime%
REM ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

REM Saving the Rooth Path (rootPath)
REM Taken from https://stackoverflow.com/questions/9252980/how-to-split-the-filename-from-a-full-path-in-batch
REM ECHO %0
REM ECHO %1

C:\Users\pablo.crespo-carri\AppData\Local\anaconda3\python.exe "C:\Users\pablo.crespo-carri\Documents\GitHub\UKO_PARSER\UKOAA_parser_v2.py" %1


ECHO CODE RUN TO COMPLETION
ECHO REVIEW OUTPUT
PAUSE

