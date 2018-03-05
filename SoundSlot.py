#! /usr/bin/python

import pyforms
from pyforms                import BaseWidget
from pyforms.controls       import ControlText
from pyforms.controls       import ControlList
from pyforms.controls       import ControlButton
from pyforms.controls       import ControlEmptyWidget


class SoundSlot(ControlEmptyWidget):
    
    def __init__(self):
        BaseWidget.__init__(self, 'SoundSlot')
        self._panel         = ControlEmptyWidget('songtitle')
        ControlText('SoundSlot')
        self._button        = ControlButton('Add sound')
        

if __name__ == "__main__":   pyforms.start_app( SoundSlot )
            