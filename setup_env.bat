@echo off

echo Changing one directory up
cd ..

echo.

echo Saving location as environment variable...
setx mathstrogamedev1 "%cd%"
echo %mathstrogamedev1%

echo.

echo ************************************************
echo ALL SET!...SEE YOU AT MATHSTRONAUTS :)
echo ************************************************
echo !PS...you can close this window!

cmd /k