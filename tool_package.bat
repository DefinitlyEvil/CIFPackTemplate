@ECHO OFF
DEL *.zip

ECHO Generating sound list... 
PUSHD resources\assets\minecraft
python auto_generate.py
POPD

ECHO Bundling... 
python create_bundle.py

ECHO Cleaning up... 
DEL resources\assets\minecraft\sounds.json

ECHO Done! 
PAUSE > nul
