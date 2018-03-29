# Animated DropDown Arrow CustomWidget for PyQt5
a graphical widget with animated transition on a state-change. this widget is render-only. it cannot be interacted by a user.

![Alt Text](https://github.com/maxoja/pyqt-animated-drop-down-arrow/blob/master/md-resource/example.gif)

<br/>

## Methods Extended From QWidget
| Method                       | Return | Details   |
|------------------------------|--------|-----------|
**setSelected(bool selected)** | -      | set widget selection state
**isSelected()**               | bool   | get widget selection state
**toggle()**                   | -      | toggle between the two selection states

<br/>

## Attributes Extended From QWidget
| Attribute       | Type    | Details |
------------------|---------|---------|
**parent**        |QtWidget |parent widget
**size**          |float    |size of this widget ( will be fixed )
**speed**         |float    |speed of animation
**color**         |QtColor  |color of the shape drawn
**selected**      |boolean  |start state 
**updateEquation**|str|an equation used by eval() to push animation playhead forth
**kernel**        |str      |an equation used by eval() to transform movement curve
**onDown**        |func     |a callback, will be triggered when finished head-down animation
**onUp**          |func     |a callback, will be triggered when finished head-right animation

note that all params are non-positional and have default values set

<br/>

### what I did learn and thanks
Thanks to this [thread](https://stackoverflow.com/questions/34341808/is-there-a-way-to-add-a-gif-to-a-markdown-file) 
for letting me know how to put gif in this markdown, and 
[ezgif](https://ezgif.com/video-to-gif) as well for providing a pretty useful converter.

###### README.md last update : 29 March 2018
