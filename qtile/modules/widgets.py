from libqtile import widget
from libqtile import qtile
from .colors import ColorZ, ColorG


widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    fontsize=14,
    padding=3,
)

extension_defaults = widget_defaults.copy()


class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()

        if self.volume < 0:
            self.text = "Volume: mute"
        else:
            self.text = f"Volume: {str(self.volume)}%"

    def _update_drawer(self, wob=False):
        if self.volume < 0:
            self.text = "Volume: mute"
        else:
            self.text = f"Volume: {str(self.volume)}%"

        self.draw()

        if wob:
            with open(self.wob, "a") as f:
                f.write(str(self.volume) + "\n")


volume = MyVolume(
    background=ColorZ,
    foreground=ColorG,
    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("pavucontrol")},
)
