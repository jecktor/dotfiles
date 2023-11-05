from libqtile import bar
from .widgets import *
from libqtile.config import Screen


screens = [
    Screen(
        top=bar.Bar(
            [widget.Sep(padding=10, linewidth=0, background="#212121"),
                widget.Image(
                    filename='~/.config/qtile/icons/python-white.png', margin=3, background="#212121"),
                widget.Sep(padding=5, linewidth=0, background="#212121"),
                widget.GroupBox(
                highlight_method='text',
                this_screen_border="#D08579",
                this_current_screen_border="#D08579",
                active="#D08579",
                inactive="#D8D8D8",
                background="#212121"),
                widget.TextBox(
                text='',
                padding=0,
                fontsize=28,
                foreground='#212121',
                background='#171717'
            ),
                widget.Sep(padding=10, linewidth=0, background="#171717"),
                widget.WindowName(foreground='#D8D8D8',
                                  background='#171717', fmt='{}'),
                widget.Sep(padding=10, linewidth=0, background="#171717"),
                widget.TextBox(
                text='',
                padding=0,
                fontsize=28,
                foreground='#212121',
                background='#171717'
            ),
                volume,
                widget.TextBox(
                text='',
                padding=5,
                fontsize=20,
                foreground='#8C8C8C',
                background='#212121',
            ),
                widget.Battery(
                update_interval=5,
                background="#212121",
                low_foreground="#D08579",
                charge_char="",
                discharge_char="",
                format="Battery: {char} {percent:2.0%} ({hour:d}:{min:02d})",
            ),
                widget.TextBox(
                text='',
                padding=5,
                fontsize=20,
                foreground='#8C8C8C',
                background='#212121',
            ),
                widget.Wlan(
                interface="wlan0",
                format="{essid} {percent:2.0%}",
                background="#212121",
                update_interval=10
             ),
                widget.TextBox(
                text='',
                padding=5,
                fontsize=20,
                foreground='#8C8C8C',
                background='#212121',
            ),
                widget.Clock(format='%d/%m/%y %H:%M',
                             background="#212121",
                             ),
                widget.Sep(padding=10, linewidth=0, background="#212121"),
            ],
            25,  # height in px
            background="#212121"
        ), ),
    Screen(
        top=bar.Bar(
            [widget.Sep(padding=10, linewidth=0, background="#212121"),
                widget.Image(
                    filename='~/.config/qtile/icons/python-white.png', margin=3, background="#212121"),
                widget.Sep(padding=5, linewidth=0, background="#212121"),
                widget.GroupBox(
                highlight_method='text',
                this_screen_border="#D08579",
                this_current_screen_border="#D08579",
                active="#D08579",
                inactive="#D8D8D8",
                background="#212121"),
                widget.TextBox(
                text='',
                padding=0,
                fontsize=28,
                foreground='#212121',
                background='#171717'
            ),
                widget.Sep(padding=10, linewidth=0, background="#171717"),
                widget.WindowName(foreground='#D8D8D8',
                                  background='#171717', fmt='{}'),
                widget.Sep(padding=10, linewidth=0, background="#171717"),
                widget.TextBox(
                text='',
                padding=0,
                fontsize=28,
                foreground='#212121',
                background='#171717'
            ),
                volume,
                widget.TextBox(
                text='',
                padding=5,
                fontsize=20,
                foreground='#8C8C8C',
                background='#212121',
            ),
                widget.Battery(
                update_interval=5,
                background="#212121",
                low_foreground="#D08579",
                charge_char="",
                discharge_char="",
                format="Battery: {char} {percent:2.0%} ({hour:d}:{min:02d})",
            ),
                widget.TextBox(
                text='',
                padding=5,
                fontsize=20,
                foreground='#8C8C8C',
                background='#212121',
            ),
                widget.Wlan(
                interface="wlan0",
                format="{essid} {percent:2.0%}",
                background="#212121",
                update_interval=10
             ),
                widget.TextBox(
                text='',
                padding=5,
                fontsize=20,
                foreground='#8C8C8C',
                background='#212121',
            ),
                widget.Clock(format='%d/%m/%y %H:%M',
                             background="#212121",
                             ),
                widget.Sep(padding=10, linewidth=0, background="#212121"),
            ],
            25,  # height in px
            background="#212121"
        ), ),
]
