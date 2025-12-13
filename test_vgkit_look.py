import vgkit as vgk

# Create main window
app = vgk.Window()
app.title("VGKit Look Test")
app.geometry("400x300")

# Create a frame (VGkFrame)
frame = vgk.Frame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add a label (VGkLabel)
label = vgk.Label(frame, text="Hello, VGKit!")
label.pack(pady=10)

# Add a button
button = vgk.Button(frame, text="Click Me!")
button.pack(pady=10)

# Run the app
app.mainloop()
