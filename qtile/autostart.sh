#!/bin/sh

nitrogen --restore &
picom & disown --experimental-backends

# start polkit agent
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown
