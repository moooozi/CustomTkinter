
![PyPI](https://img.shields.io/pypi/v/vgkit)



# VGKit
VGKit is a fork of [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) by Tom Schimansky. It has simpler and performance oriented widgets, Treeview implementation and improved DPI change handling.

*Note: This is a fork tailored to my specific needs. It's not well documented or maintained for everyone else.*

## Installation
Install the module with pip:
```
pip3 install vgkit
```
**Update existing installation:** ```pip3 install vgkit --upgrade```

## Usage
```python
import vgkit as vgk

# Create a window
app = vgk.Window()

# Add widgets
button = vgk.Button(app, text="Click me!")
label = vgk.Label(app, text="Hello, VGKit!")

# Run the app
app.mainloop()
```

