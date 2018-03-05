#! /usr/bin/python

import pyforms
from pyforms                import BaseWidget
from pyforms.controls       import ControlText
from pyforms.controls       import ControlList
from pyforms.controls       import ControlButton
from pyforms.controls       import ControlEmptyWidget
from SoundSlot              import SoundSlot
from AddMenuFuntionality    import AddMenuFuntionality



#Main window
class MainWindow(AddMenuFuntionality, BaseWidget, SoundSlot):
                     
    def __init__(self):
        BaseWidget.__init__(self, 'SoundBoard')
        self._panel         = ControlEmptyWidget()
        self._button        = ControlButton('botoncito')
        self._button.value  = self.__buttonAction

    
    def __buttonAction(self):
        """
        Button action event
        """
        win                 = SoundSlot()
        win.parent          = self
        self._panel.value   = win
        win.show()
        

if __name__ == "__main__":   pyforms.start_app( MainWindow )