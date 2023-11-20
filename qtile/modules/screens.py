from libqtile import bar
from .widgets import *
from .colors import *
from libqtile.config import Screen

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(padding=10, linewidth=0, background=ColorZ),
                widget.Image(
                    filename="~/.config/qtile/icons/python-white.png",
                    margin=3,
                    background=ColorZ,
                ),
                widget.Sep(padding=5, linewidth=0, background=ColorZ),
                widget.GroupBox(
                    highlight_method="text",
                    this_screen_border=ColorF,
                    this_current_screen_border=ColorF,
                    active=ColorF,
                    inactive=ColorG,
                    background=ColorZ,
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground=ColorD,
                    background=ColorZ,
                ),
                widget.Sep(padding=10, linewidth=0, background=ColorZ),
                widget.WindowName(foreground=ColorG, background=ColorZ, fmt="{}"),
                widget.Sep(padding=10, linewidth=0, background=ColorZ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground=ColorD,
                    background=ColorZ,
                ),
                volume,
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground=ColorD,
                    background=ColorZ,
                ),
                widget.Battery(
                    update_interval=5,
                    foreground=ColorG,
                    low_foreground=ColorF,
                    background=ColorZ,
                    charge_char="",
                    discharge_char="",
                    format="Battery: {char} {percent:2.0%} ({hour:d}:{min:02d})",
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground=ColorD,
                    background=ColorZ,
                ),
                widget.Wlan(
                    interface="wlan0",
                    format="{essid} {percent:2.0%}",
                    foreground=ColorG,
                    background=ColorZ,
                    update_interval=10,
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground=ColorD,
                    background=ColorZ,
                ),
                widget.Clock(
                    format="%d/%m/%y %H:%M",
                    foreground=ColorG,
                    background=ColorZ,
                ),
                widget.Sep(padding=10, linewidth=0, background=ColorZ),
            ],
            25,  # height in px
            background=ColorZ,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Sep(padding=10, linewidth=0, background=ColorZ),
                widget.Image(
                    filename="~/.config/qtile/icons/python-white.png",
                    margin=3,
                    background=ColorZ,
                ),
                widget.Sep(padding=5, linewidth=0, background=ColorZ),
                widget.GroupBox(
                    highlight_method="text",
                    this_screen_border=ColorF,
                    this_current_screen_border=ColorF,
                    active=ColorF,
                    inactive=ColorG,
                    background=ColorZ,
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground=ColorD,
                    background=ColorZ,
                ),
                widget.Sep(padding=10, linewidth=0, background=ColorZ),
                widget.WindowName(foreground=ColorG, background=ColorZ, fmt="{}"),
                widget.Sep(padding=10, linewidth=0, background=ColorZ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground=ColorD,
                    background=ColorZ,
                ),
                volume,
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground=ColorD,
                    background=ColorZ,
                ),
                widget.Battery(
                    update_interval=5,
                    foreground=ColorG,
                    low_foreground=ColorF,
                    background=ColorZ,
                    charge_char="",
                    discharge_char="",
                    format="Battery: {char} {percent:2.0%} ({hour:d}:{min:02d})",
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground=ColorD,
                    background=ColorZ,
                ),
                widget.Wlan(
                    interface="wlan0",
                    format="{essid} {percent:2.0%}",
                    foreground=ColorG,
                    background=ColorZ,
                    update_interval=10,
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground=ColorD,
                    background=ColorZ,
                ),
                widget.Clock(
                    format="%d/%m/%y %H:%M",
                    foreground=ColorG,
                    background=ColorZ,
                ),
                widget.Sep(padding=10, linewidth=0, background=ColorZ),
            ],
            25,  # height in px
            background=ColorZ,
        ),
    ),
]
