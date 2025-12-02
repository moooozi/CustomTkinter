from typing import Union, Tuple, Any

from .ctk_frame import CTkFrame


class CTkContainer(CTkFrame):
    """
    A simple container widget based on CTkFrame, optimized for performance by skipping canvas creation.
    Predefined settings: corner_radius=0, border_width=0, fg_color="transparent" to ensure no custom drawing.
    """

    def __init__(
        self,
        master: Any,
        bg_color: Union[str, Tuple[str, str]] = "transparent",
        **kwargs
    ):

        # Call parent __init__ with fixed settings to skip canvas
        super().__init__(
            master=master,
            corner_radius=0,
            border_width=0,
            bg_color=bg_color,
            fg_color="transparent",
            border_color=None,
            background_corner_colors=None,
            overwrite_preferred_drawing_method=None,
            **kwargs
        )
