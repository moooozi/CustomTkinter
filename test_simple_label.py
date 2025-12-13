import vgkit as ctk

# Create the main window
root = ctk.CTk()
root.title("CTkSimpleLabel Complex Test")
root.geometry("800x600")

# Create 4 frames
frames = []
for i in range(4):
    frame = ctk.CTkFrame(root)
    frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")
    frames.append(frame)

# Configure grid weights
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Long text for testing
long_text = "This is a very long text that should wrap to the width of the parent element, accounting for scaling changes. Let's see if it works properly with multiple labels in frames."

# Create labels in each frame
for i, frame in enumerate(frames):
    wraplength = "self" if i == 0 else "master"  # Test both
    label = ctk.CTkSimpleLabel(
        master=frame, text=f"Label {i+1}: {long_text}", wraplength=wraplength
    )
    label.grid(row=0, column=0)  # Grid without sticky="ew" to test

# Run the application
root.mainloop()



