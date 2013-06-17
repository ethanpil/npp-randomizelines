# RandomizeLines.py for Notepad++ Python Scripting plugin
# https://github.com/ethanpil/npp-randomizelines
#
# A Notepad++ Python Scriping Plugin to randomize lines in the editor
#
# Version 1.0
#
## Installation
#  1. Copy **RandomizeLines.py** to **\plugins\PythonScript\scripts\** in your NPP folder
#  2. Restart NPP. It will now appear as a menu item under Plugins...Python Script...Scripts
#
## Usage
#  1. Select the lines to randomize, or select nothing.
#  2. Go to the NPP menu, Plugins...Python Script...Scripts...RandomizeLines and click!
#  3. If selected text is detected, it reorders the lines and replaces the selected text, otherwise the entire contents of current document.
#  4. Undo is available if you dont like the results
#
## Notes
# The plugin attempts to detect your EOL setting and replicate it when replacing with the randomized lines
#

import random

#Preserve Undo Capability
editor.beginUndoAction()

#Get any selected text
seltext = editor.getSelText()
seltextlen = len(seltext)

#Preserve EOL Mode when we send back the reordered lines
EOLMode = editor.getEOLMode()

if EOLMode==0:
  EOLchar = '\r\n'
elif EOLMode==1:
	EOLchar = '\r'
elif EOLMode==2:
    EOLchar = '\n'


if seltextlen >= 1 :
	rawtext = str(seltext)
	rawtextlines = rawtext.splitlines()
	random.shuffle(rawtextlines)
	randomizedtext = EOLchar.join(rawtextlines)
	editor.replaceSel(randomizedtext)
else:
	rawtext = str(editor.getText())
	rawtextlines = rawtext.splitlines()
	random.shuffle(rawtextlines)
	randomizedtext = EOLchar.join(rawtextlines)
	editor.setText(randomizedtext)	
