from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
from modules.colors import colors
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
import os

decor = {
    "decorations": [
        RectDecoration(colour=colors[2], radius=5, filled=True, padding_y=5)
    ],
    "padding": 5,
}

decor_left = {
    "decorations": [
        RectDecoration(colour=colors[2], radius=[5,0,0,5], filled=True, padding_y=5)
    ],
    "padding": 5,
}

decor_right = {
    "decorations": [
        RectDecoration(colour=colors[2], radius=[0,5,5,0], filled=True, padding_y=5)
    ],
    "padding": 5,
}

decor_group = {
    "decorations": [
        RectDecoration(colour=colors[2], radius=5, filled=True, padding_y=5, group = True)
    ],
    "padding": 5,
}

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=10, linewidth=0, background=colors[16]),
                widget.Image(filename='~/.config/qtile/python.png', margin=3, background=colors[16], mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(os.path.expanduser('rofi -show drun'))}),
                widget.Sep(padding=4, linewidth=0, background=colors[16]), 
                widget.GroupBox(
                        **decor,
                        font = 'Font Awesome Bold',
                        fontsize = 16,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors[8],
                        inactive = colors[17],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[10],
                        foreground = colors[2],
                        background = colors[16]
                        ),
                widget.Prompt(
                        foreground = colors[5],
                        background = colors[16]
                        ),
                widget.Spacer(length=5),
                widget.WindowName(foreground=colors[17],fmt='{}'),
                widget.Spacer (
                        background = colors[16]
                        ),
                widget.Systray(
                        background=colors[16],
                        icon_size=20,
                        padding = 5
                        ),
                widget.Spacer (
                        background = colors[16]
                        ),               
                widget.CurrentLayoutIcon(
                        **decor_group,
                        font = "CaskaydiaCove Nerd Font Bold",
                        scale = .5,
                        foreground = colors[5],
                        background = colors[16]
                        ),
                widget.CurrentLayout(
                        **decor_group,
                        font = "CaskaydiaCove Nerd Font Bold",
                        fontsize = 16,
                        foreground = colors[4],
                        background = colors[16]
                        ),
                widget.Spacer(length=5),               
                widget.CheckUpdates(
                        **decor_group,
                        font="CaskaydiaCove Nerd Font",
                        fontsize=16,
                        distro='Arch_checkupdates',
                        update_interval=60,
                        display_format='  Updates: {updates}',
                        no_update_string='  No Updates',
                        foreground=colors[10],
                        background=colors[16],
                        colour_have_updates=colors[9],
                        colour_no_updates=colors[10],
                        #padding = 0,
                        ), 
                  widget.Spacer(length=5),
                  widget.Wttr(
                        **decor_group,
                        font = "CaskaydiaCove Nerd Font",
                        fontsize = 14,
                        lang = 'en',
                        format='   %l: %c%m 🌡%t/%f',
                        location = {'Miami': 'Miami'},
                        units = 's',
                        update_interval = 300,
                        foreground = colors[11],
                        background = colors[16],
                        #padding = 0,
                        ),
                widget.Spacer(length=5),
                widget.Volume(
                        **decor_group,
                        font="CaskaydiaCove Nerd Font",
                        volume_app='pamixer',
                        emoji=True,
                        foreground=colors[10],
                        background=colors[16],
                        fontsize=16
                        ),
                widget.Spacer(length=5),
                widget.Clock(
                        **decor_group,
                        font="CaskaydiaCove Nerd Font",
                        foreground = colors[14],
                        background = colors[16],
                        fontsize = 16,
                        format="  %Y-%m-%d %I:%M%P"
                        ),
                widget.Spacer(length=5),
                widget.TextBox(
                    text=' ',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('archlinux-logout'))
                    },
                    foreground=colors[9]
                    ),
                widget.Spacer(length=8)               
            ],
            30,  # height in px
            background=colors[16]  # background color
        ), ),
]
