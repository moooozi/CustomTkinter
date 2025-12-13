import vgkit as vgk

vgk.set_appearance_mode("dark")
vgk.set_default_color_theme("blue")
vgk.set_window_scaling(0.8)
vgk.set_widget_scaling(0.8)

app = vgk.Window()
app.geometry("400x300")
app.title("CTkDialog Test")


def change_mode():
    if c1.get() == 0:
        vgk.set_appearance_mode("light")
    else:
        vgk.set_appearance_mode("dark")


def button_1_click_event():
    dialog = vgk.InputDialog(text="Type in a number:", title="Test")
    print("Number:", dialog.get_input())


def button_2_click_event():
    dialog = vgk.InputDialog(text="long text " * 100, title="Test")
    print("Number:", dialog.get_input())


button_1 = vgk.Button(app, text="Open Dialog", command=button_1_click_event)
button_1.pack(pady=20)
button_2 = vgk.Button(app, text="Open Dialog", command=button_2_click_event)
button_2.pack(pady=20)
c1 = vgk.CheckBox(app, text="dark mode", command=change_mode)
c1.pack(pady=20)

app.mainloop()
