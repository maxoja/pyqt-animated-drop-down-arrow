# Animated DropDown Arrow CustomWidget for PyQt5
![Alt Text](https://github.com/maxoja/pyqt-animated-drop-down-arrow/blob/master/md-resource/example.gif)

**current accepted paremeters**
[ note : all are non-positional and default set ]

| Parameter | Type    | Details |
------------|---------|---------|
parent      |QtWidget |parent widget
size        |float    |size of this widget ( will be fixed )
speed       |float    |speed of animation
color       |QtColor  |color of the shape drawn
selected    |boolean  |start state 
updateEquation|str    |an equation used by eval() to push animation playhead forth
kernel      |str      |an equation used by eval() to transform movement curve
onDown      |func     |a callback, will be triggered when finished head-down animation
onUp        |func     |a callback, will be triggered when finished head-right animation


## what i did learn and thanks
thanks to this thread for letting me know how to put gif in this markdown
https://stackoverflow.com/questions/34341808/is-there-a-way-to-add-a-gif-to-a-markdown-file
and the online converter site as well
https://ezgif.com/video-to-gif

README.md last update : 29 March 2018
