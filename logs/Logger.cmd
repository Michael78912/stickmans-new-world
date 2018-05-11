@ECHO OFF
@SETLOCAL ENABLEEXTENSIONS
@CD /D "%~dp0"

SET FILE=stickmanranger.log

:A
    SET /P "INPUT=>> "
    ECHO %DATE% %TIME% %INPUT% >> %FILE%
    GOTO A