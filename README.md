# Animated DropDown Arrow CustomWidget for PyQt5
a small graphical widget rendered by QPainter with animated transition on a state-change. its transformation can be customised using math equation(s). this widget is render-only. in other words, it cannot be interacted directly with a user. take a look at the example gif below to see how it resemble.

![Alt Text](https://github.com/maxoja/pyqt-animated-drop-down-arrow/blob/master/md-resource/example.gif)

<br/>

## Methods Extended From QWidget
| Method                       | Return | Details   |
|------------------------------|--------|-----------|
**toggle()**                   | -      | toggle between the two selection states
**setSelected(bool selected)** | -      | set widget selection state
**setHideVisual(bool hide)**   | -      | won't be drawn if true (widget area still does exist)
**isSelected()**               | bool   | get widget selection state
**isHidingVisual()**           | bool   | get widget is not drawing or opposite
**setColor()**                 | -      | set drawing color
**getColor()**                 | QColor | get drawing color

<br/>

## Constructor Parameters
| Attribute       | Type    | Details |
------------------|---------|---------|
**parent**        |QtWidget |parent widget
**size**          |float    |size of this widget ( will be fixed )
**speed**         |float    |speed of animation
**color**         |QtColor  |color of the shape drawn
**selected**      |boolean  |start state
**updateEquation**|str      |an equation used by eval() to push animation play-head forth
**kernel**        |str      |an equation used by eval() to transform movement curve
**onDown**        |func     |a callback, will be triggered when finished head-down animation
**onUp**          |func     |a callback, will be triggered when finished head-right animation

please note that all params are optional, non-positional and have default values set

<br/>

### what I did learn and thanks
Thanks to this [thread](https://stackoverflow.com/questions/34341808/is-there-a-way-to-add-a-gif-to-a-markdown-file) 
for letting me know how to put gif in this markdown, and 
[ezgif](https://ezgif.com/video-to-gif) as well for providing a pretty useful converter.

###### README.md last update : 31 March 2018 09:24am
