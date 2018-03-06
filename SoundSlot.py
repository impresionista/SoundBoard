#! /usr/bin/python

import pyforms
from pyforms                import BaseWidget
from pyforms.controls       import ControlList
from pyforms.controls       import ControlText
from pyforms.controls       import ControlButton
from pyforms.controls       import ControlEmptyWidget


class SoundSlot(ControlEmptyWidget):
    """docstring for SoundSlot."""
    def __init__(self, arg):
        super(SoundSlot, self).__init__()
        self._panel         = ControlEmptyWidget('Song title')
        self._playbutton    = ControlButton('Play/Pause')
        self._stopbutton    = ControlButton('Stop')


if __name__ == "__main__":   pyforms.start_app( SoundSlot )
