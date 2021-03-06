#! /usr/bin/python

"""
Slot for each sound effecto to play
"""

import pyforms
from pyforms                import BaseWidget
from pyforms.controls       import ControlList
from pyforms.controls       import ControlText
from pyforms.controls       import ControlButton
from pyforms.controls       import ControlEmptyWidget


class SoundSlot(BaseWidget, ControlEmptyWidget):
    """
    docstring for SoundSlot.
    """
    def __init__(self):
        super(SoundSlot, self).__init__('SoundSlot_1')
        self._panel         = ControlEmptyWidget('Song title')
        self._playbutton    = ControlButton('Play/Pause')
        self._stopbutton    = ControlButton('Stop')


if __name__ == "__main__":   pyforms.start_app( SoundSlot )
