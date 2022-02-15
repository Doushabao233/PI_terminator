@echo off
:: pack file
pyinstaller -F -D -w -i="favicon.ico" main.py

rem delete files
rd /s /q __pycache__
rd /s /q build
xcopy /e /y languages dist\main\languages
xcopy /e /y settings.json dist\main
del main.spec

rem ok
pause