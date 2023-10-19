from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from .keys import mod


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
