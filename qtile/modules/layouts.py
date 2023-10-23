from libqtile import layout
from libqtile.config import Match


layouts = [
    layout.MonadTall(margin=10, border_focus='#D08579',
                     border_normal='#312B29'),
    layout.Max(),
]

floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], border_focus='#D08579', border_normal='#312B29', border_width=2)