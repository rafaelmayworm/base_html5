Sublime AS3 - Actionscript Sublime Package
===========================

Installation
--------

`cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/`  
`git clone git://github.com/jrmoretti/SublimeAS3.git ActionScript3`

You'll need to remove the old AS Package, to do so, execute:  
`rm -rf ActionScript`

Using Falcon (or other SDK's)
on your build.yaml file, add
`sdk-path:
    - "{SDK_PATH}"`
    
for more tips on how to create and run a project, please check [the sample project](https://github.com/jrmoretti/SAS3DefaultProject)

Updating
--------
`cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/ActionScript3`  
`git pull`

About
-----

This is a port from the AS3 TextMate bundle.  
Work in progress and still very alpha.  
Use at your own risk!


TODO
-----
Contextual autocomplete  
Sort imports by name  
Create project script  
Dump SWCs in a regular interval

CREDITS
-----
[Lucas Dupin](http://github.com/lucasdupin)
[Jay Moretti](http://github.com/jrmoretti)
