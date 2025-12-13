import vgkit
from PIL import Image
import os

vgkit.set_appearance_mode("dark")


class App(vgkit.Window):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("vgkit example_background_image.py")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = vgkit.CTkImage(
            Image.open(current_path + "/test_images/bg_gradient.jpg"),
            size=(self.width, self.height),
        )
        self.bg_image_label = vgkit.Label(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = vgkit.Frame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = vgkit.Label(
            self.login_frame,
            text="vgkit\nLogin Page",
            font=vgkit.Font(size=20, weight="bold"),
        )
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = vgkit.Entry(
            self.login_frame, width=200, placeholder_text="username"
        )
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = vgkit.Entry(
            self.login_frame, width=200, show="*", placeholder_text="password"
        )
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = vgkit.Button(
            self.login_frame, text="Login", command=self.login_event, width=200
        )
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        # create main frame
        self.main_frame = vgkit.Frame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = vgkit.Label(
            self.main_frame,
            text="vgkit\nMain Page",
            font=vgkit.Font(size=20, weight="bold"),
        )
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.back_button = vgkit.Button(
            self.main_frame, text="Back", command=self.back_event, width=200
        )
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        print(
            "Login pressed - username:",
            self.username_entry.get(),
            "password:",
            self.password_entry.get(),
        )

        self.login_frame.grid_forget()  # remove login frame
        self.main_frame.grid(
            row=0, column=0, sticky="nsew", padx=100
        )  # show main frame

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame


if __name__ == "__main__":
    app = App()
    app.mainloop()
