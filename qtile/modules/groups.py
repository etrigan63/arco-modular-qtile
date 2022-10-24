from libqtile import hook
from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import keys, mod

#groups = [Group(i) for i in "1234567890"]

#for i in groups:
#    keys.extend([
        # mod1 + letter of group = switch to group
#        Key([mod],
#            i.name,
#            lazy.group[i.name].toscreen(),
#            desc="Switch to group {}".format(i.name)),

#        Key([mod], "Right", lazy.screen.next_group(),
#            desc="Switch to next group"),

#        Key([mod], "Left", lazy.screen.prev_group(),
#            desc="Switch to previous group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
#        Key([mod, "shift"],
#            i.name,
#            lazy.window.togroup(i.name, switch_group=True),
#            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
#    ])


groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

group_labels = ["㊀", "㊁", "㊂", "㊃", "㊄", "㊅", "㊆", "㊇", "㊈", "㊉",]

group_layouts = ["monadthreecol", "monadthreecol", "monadthreecol", "monadthreecol", "monadthreecol", "monadthreecol", "monadthreecol", "monadthreecol", "monadthreecol", "monadthreecol",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

#
# assign apps to groups/workspace
#
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}

    # assign deez apps
    d[group_names[0][0]] = ['Alacritty', 'xfce4-terminal', 'kitty', 'Navigator', 'brave-browser', 'midori', 'qutebrowser']
    d[group_names[1][0]] = ['wavebox', 'telegram-desktop', 'discord', 'fractal', 'element']
    d[group_names[2][0]] = ['org.remmina.Remmina']
    d[group_names[3][0]] = ['darktable', 'ART']
    d[group_names[4][0]] = ['vlc', 'obs', 'mpv', 'mplayer', 'lxmusic', 'jellyfinmediaplayer']
    d[group_names[5][0]] = ['']
    d[group_names[6][0]] = ['lxappearance', 'gpartedbin', 'lxtask', 'lxrandr', 'arandr', 'pavucontrol', 'xfce4-settings-manager']
    d[group_names[7][0]] = ['VirtualBox Manager']
    d[group_names[8][0]] = ['']
    d[group_names[9][0]] = ['']

    wm_class = client.window.get_wm_class()[0]
    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)

