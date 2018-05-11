@set distdir=dist\terrain_viewer\
@compile_all -d %CD% -o %CD%\c 
pyinstaller terrain_viewer.spec --upx-dir=C:\ -i=icon.ico
@echo.>> logfile.log
@echo.>> logfile.log
@echo ---------------------------------------------------------------------------------------------------------->>logfile.log
@mkdir %distdir%terrains %distdir%data
@xcopy /s terrains %distdir%terrains
@xcopy /s  data %distdir%data
@pause