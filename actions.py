# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Thomas Amland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

_actions = [
  ["Navigation actions", [
    "left"              , "Move Left",
    "right"             , "Move Right",
    "up"                , "Move Up",
    "down"              , "Move Down",
    "pageup"            , "Page Up",
    "pagedown"          , "Page Down",
    "select"            , "Select Item",
    "highlight"         , "Highlight Item",
    #"parentdir"         , "NAV_BACK",       # backward compatibility
    #"close"             , "NAV_BACK", # backwards compatibility
    "parentfolder"      , "Parent Directory",
    "back"              , "Back",
    "previousmenu"      , "Previous Menu",
    "info"              , "Show Info",
    "contextmenu"       , "Context Menu",
    "firstpage"         , "First Page",
    "lastpage"          , "Last Page",
    "nextletter"        , "Next Letter",
    "prevletter"        , "Previous Letter",
    "jumpsms2"          , "JUMP_SMS2",
    "jumpsms3"          , "JUMP_SMS3",
    "jumpsms4"          , "JUMP_SMS4",
    "jumpsms5"          , "JUMP_SMS5",
    "jumpsms6"          , "JUMP_SMS6",
    "jumpsms7"          , "JUMP_SMS7",
    "jumpsms8"          , "JUMP_SMS8",
    "jumpsms9"          , "JUMP_SMS9",
  ]],

  ["Playback actions", [
    "play"              , "Play",
    "pause"             , "Pause",
    "playpause"         , "Play/Pause",
    "stop"              , "Stop",
    "skipnext"          , "Next",
    "skipprevious"      , "Previous",
    "fastforward"       , "Fast Forward",
    "rewind"            , "Rewind",
    "playercontrol(tempoup)", "Increase Playback Speed (v18+)",
    "playercontrol(tempodown)", "Decrease Playback Speed (v18+)",
    "smallstepback"     , "Small Step Back",
    "stepforward"       , "Step Forward",
    "stepback"          , "Step Back",
    "bigstepforward"    , "Big Step Forward",
    "bigstepback"       , "Big Step Back",
    "chapterorbigstepforward", "Next Chapter or Big Step Forward",
    "chapterorbigstepBack"   , "Previous Chapter or Big Step Back",
    "videonextstream"   , "Toggle Video Tracks (v18+)",
    "osd"               , "Show OSD",
    "codecinfo"         , "Show codec info (up to v16)",
    "playerprocessinfo" , "Player Process info (v17+)",
    "playerdebug"       , "Player Debug (v17+)",
    "showtime"          , "Show current play time",
    "playlist"          , "Show Playlist",
    "fullscreen"        , "Toggle Fullscreen",
    "aspectratio"       , "Change Aspect Ratio",
    "showvideomenu"     , "Go to DVD Video Menu",
    "playercontrol(repeat)"   , "Toggle Repeat",
    "playercontrol(repeatone)", "Repeat One",
    "playercontrol(repeatall)", "Repeat All",
    "playercontrol(repeatoff)", "Repeat Off",
    "playercontrol(random)"   , "Toggle Random",
    "playercontrol(randomon)" , "Random On",
    "playercontrol(randomoff)", "Random Off",
    "createbookmark"          , "Create Bookmark",
    "createepisodebookmark"   , "Create Episode Bookmark",
    "togglestereomode"        , "Toggle 3D/Stereoscopic mode",
    "switchplayer"            , "Switch Player",
  ]],

  ["Audio actions", [
    "mute"              , "Mute",
    "volumeup"          , "Volume Up",
    "volumedown"        , "Volume Down",
    "audionextlanguage" , "Next Language",
    "audiodelay"        , "Delay",
    "audiodelayminus"   , "Delay Minus",
    "audiodelayplus"    , "Delay Plus",
    "audiotoggledigital", "Toggle Digital/Analog",
  ]],

  ["Pictures actions", [
    "nextpicture"       , "Next Picture",
    "previouspicture"   , "Previous Picture",
    "rotate"            , "Rotate Picture",
    "rotateccw"         , "Rotate Picture CCW",
    "zoomout"           , "Zoom Out",
    "zoomin"            , "Zoom In ",
    "zoomnormal"        , "Zoom level Normal",
    "zoomlevel1"        , "Zoom level 1",
    "zoomlevel2"        , "Zoom level 2",
    "zoomlevel3"        , "Zoom level 3",
    "zoomlevel4"        , "Zoom level 4",
    "zoomlevel5"        , "Zoom level 5",
    "zoomlevel6"        , "Zoom level 6",
    "zoomlevel7"        , "Zoom level 7",
    "zoomlevel8"        , "Zoom level 8",
    "zoomlevel9"        , "Zoom level 9",
  ]],

  ["Subtitles actions", [
    "showsubtitles"     , "Show Subtitles",
    "nextsubtitle"      , "Next Subtitle",
    "browsesubtitle"    , "Browse Subtitle",
    "subtitledelay"     , "Delay",
    "subtitledelayminus", "Delay Minus",
    "subtitledelayplus" , "Delay Plus",
    "subtitlealign"     , "Align",
    "subtitleshiftup"   , "Move Subtitles Up",
    "subtitleshiftdown" , "Move Subtitles Down",
  ]],

  ["PVR actions", [
    "channelup"             , "Channel Up",
    "channeldown"           , "Channel Down",
    "previouschannelgroup"  , "Previous channel group",
    "nextchannelgroup"      , "Next channel group",
    "record"                , "Record",
    "playpvr"               , "PVR Play",
    "playpvrtv"             , "PVR Play TV",
    "playpvrradio"          , "PVR Play Radio",
    "togglecommskip"        , "Toggle Commskip",
    "showtimerrule"         , "PVR Show Timer Rule",
    "channelnumberseparator", "Channel Number Separator",
  ]],

  ["Item actions", [
    "queue"             , "Queue item",
    "delete"            , "Delete item",
    "copy"              , "Copy item",
    "move"              , "Move item",
    "moveitemup"        , "Move item up",
    "moveitemdown"      , "Move item down",
    "rename"            , "Rename item",
    "scanitem"          , "Scan item",
    "togglewatched"     , "Toggle watched status",
    #"increaserating"    , "INCREASE_RATING", #unused
    #"decreaserating"    , "DECREASE_RATING", #unused
  ]],

  ["System actions", [
    "togglefullscreen"  , "Toggle Kodi Fullscreen",
    "minimize"          , "Minimize",
    "shutdown"          , "Shutdown",
    "reboot"            , "Reboot",
    "hibernate"         , "Hibernate",
    "suspend"           , "Suspend",
    "restartapp"        , "Restart XBMC",
    "system.logoff"     , "Log off",
    "quit"              , "Quit XBMC",
  ]],

  ["Virtual Keyboard actions", [
    "enter"             , "Enter",
    "shift"             , "Shift",
    "symbols"           , "Symbols",
    "backspace"         , "Backspace ",
    "number0"           , "0",
    "number1"           , "1",
    "number2"           , "2",
    "number3"           , "3",
    "number4"           , "4",
    "number5"           , "5",
    "number6"           , "6",
    "number7"           , "7",
    "number8"           , "8",
    "number9"           , "9",
    "red"               , "Teletext Red",
    "green"             , "Teletext Green",
    "yellow"            , "Teletext Yellow",
    "blue"              , "Teletext Blue",
  ]],

  ["Other actions", [
    "updatelibrary(video)", "Update Video Library",
    "updatelibrary(music)", "Update Music Library",
    "cleanlibrary(video)", "Clean Video Library",
    "cleanlibrary(music)", "Clean Music Library",
    "screenshot"        , "Take screenshot",
    "reloadkeymaps"     , "Reload keymaps",
    "increasepar"       , "Increase PAR",
    "decreasepar"       , "Decrease PAR",
    "nextresolution"    , "Change resolution",
    "nextcalibration"   , "Next calibration",
    "resetcalibration"  , "Reset calibration",
    "showpreset"        , "Show current visualisation preset",
    "presetlist"        , "Show visualisation preset list",
    "nextpreset"        , "Next visualisation preset",
    "previouspreset"    , "Previous visualisation preset",
    "lockpreset"        , "Lock current visualisation preset ",
    "randompreset"      , "Switch to a new random preset",
  ]],

  #["Analog", [
  #  "scrollup"          , "SCROLL_UP",
  #  "scrolldown"        , "SCROLL_DOWN",
  #  "cursorleft"        , "CURSOR_LEFT",
  #  "cursorright"       , "CURSOR_RIGHT",
  #  "analogmove"        , "ANALOG_MOVE",
  #  "analogfastforward" , "ANALOG_FORWARD",
  #  "analogrewind"      , "ANALOG_REWIND",
  #  "analogseekforward" , "ANALOG_SEEK_FORWARD",
  #  "analogseekback"    , "ANALOG_SEEK_BACK",
  #  "leftclick"         , "MOUSE_LEFT_CLICK",
  #  "rightclick"        , "MOUSE_RIGHT_CLICK",
  #  "middleclick"       , "MOUSE_MIDDLE_CLICK",
  #  "doubleclick"       , "MOUSE_DOUBLE_CLICK",
  #  "wheelup"           , "MOUSE_WHEEL_UP",
  #  "wheeldown"         , "MOUSE_WHEEL_DOWN",
  #  "mousedrag"         , "MOUSE_DRAG",
  #  "mousemove"         , "MOUSE_MOVE",
  #]]

  #"verticalshiftup"   , "VSHIFT_UP",
  #"verticalshiftdown" , "VSHIFT_DOWN",
  #"increasevisrating" , "VIS_RATE_PRESET_PLUS",
  #"decreasevisrating" , "VIS_RATE_PRESET_MINUS",
  #"nextscene"         , "NEXT_SCENE",
  #"previousscene"     , "PREV_SCENE",
  #"filter"            , "FILTER",
  #"filterclear"       , "FILTER_CLEAR",
  #"filtersms2"        , "FILTER_SMS2",
  #"filtersms3"        , "FILTER_SMS3",
  #"filtersms4"        , "FILTER_SMS4",
  #"filtersms5"        , "FILTER_SMS5",
  #"filtersms6"        , "FILTER_SMS6",
  #"filtersms7"        , "FILTER_SMS7",
  #"filtersms8"        , "FILTER_SMS8",
  #"filtersms9"        , "FILTER_SMS9",
  #"guiprofile"        , "GUIPROFILE_BEGIN",
  #"volampup"          , "VOLAMP_UP",
  #"volampdown"        , "VOLAMP_DOWN",
  #"mplayerosd"        , "SHOW_MPLAYER_OSD", #?
  #"hidesubmenu"       , "OSD_HIDESUBMENU", #depricated
  #"osdleft"           , "OSD_SHOW_LEFT",
  #"osdright"          , "OSD_SHOW_RIGHT",
  #"osdup"             , "OSD_SHOW_UP",
  #"osddown"           , "OSD_SHOW_DOWN",
  #"osdselect"         , "OSD_SHOW_SELECT",
  #"osdvalueplus"      , "OSD_SHOW_VALUE_PLUS",
  #"osdvalueminus"     , "OSD_SHOW_VALUE_MIN",
]


_activate_window = [
  "accesspoints"             , "Access Points",
  "addonbrowser"             , "Addon Browser",
  "addoninformation"         , "Addon Info",
  "addonsettings"            , "Addon Settings",
  "appearancesettings"       , "Appearance Settings",
  "contentsettings"          , "Content Settings",
  "contextmenu"              , "Context Menu",
  "favourites"               , "Favourites",
  "filebrowser"              , "Filebrowser",
  "filestackingdialog"       , "Filestacking Dialog",
  "fullscreeninfo"           , "Fullscreen Info",
  "karaoke"                  , "Karaoke Lyrics",
  "karaokelargeselector"     , "Karaoke Selector",
  "karaokeselector"          , "Karaoke Song Selector",
  "locksettings"             , "Lock Settings",
  "loginscreen"              , "Login Screen",
  "mediafilter"              , "Media filter",
  "mediasource"              , "Mediasource Dialog",
  "movieinformation"         , "Video Info",
  "musicfiles"               , "Music Files",
  "musicinformation"         , "Music Info",
  "musiclibrary"             , "Music Library",
  "musicoverlay"             , "Music Overlay",
  "musicplaylist"            , "Music Playlist",
  "musicplaylisteditor"      , "Music Playlist Editor",
  "musicsettings"            , "Music Settings",
  "networksetup"             , "Networksetup",
  "peripherals"              , "Peripheral manager",
  "peripheralsettings"       , "Peripherals settings",
  "pictureinfo"              , "Picture Info",
  "picturessettings"         , "Pictures Settings",
  "profiles"                 , "Profiles",
  "profilesettings"          , "Profile Settings",
  "programssettings"         , "Programs Settings",
  "pvrchannelguide"          , "PVR Channel Guide",
  "pvrchannelmanager"        , "PVR Channel Manager",
  "pvrchannelscan"           , "PVR Channel Scan",
  "pvrgroupmanager"          , "PVR Group Manager",
  "pvrguideinfo"             , "PVR Guide Info",
  "pvrguidesearch"           , "PVR Guide Search",
  "pvrosdchannels"           , "PVR OSD Channels",
  "pvrosdcutter"             , "PVR OSD Cutter",
  "pvrosddirector"           , "PVR OSD Director",
  "pvrosdguide"              , "PVR OSD Guide",
  "pvrrecordinginfo"         , "PVR Recording Info",
  "pvrsettings"              , "PVR Settings",
  "pvrtimersetting"          , "PVR Timer Setting",
  "pvrupdateprogress"        , "PVR Update Progress",
  "radiochannels"            , "Radio Channels",
  "radioguide"               , "Radio Guide",
  "radiorecordings"          , "Radio Recordings",
  "radiosearch"              , "Radio Search",
  "radiotimers "             , "Radio Timers",
  "screencalibration"        , "Screen Calibration",
  "screensaver"              , "Screensaver",
  "servicesettings"          , "Service Settings",
  "settings"                 , "Settings",
  "shutdownmenu"             , "Shutdown Menu",
  "skinsettings"             , "Skin Settings",
  "smartplaylisteditor"      , "Smart Playlist Editor",
  "smartplaylistrule"        , "Smart Playlist Rule",
  "songinformation"          , "Song Info",
  "startwindow"              , "Start",
  "subtitlesearch"           , "Subtitle Search",
  "systeminfo"               , "System info",
  "systemsettings"           , "System Settings",
  "testpattern"              , "Test Pattern",
  "tvchannels"               , "TV Channels",
  "tvguide"                  , "TV Guide",
  "tvrecordings"             , "TV Recordings",
  "tvsearch"                 , "TV Search",
  "tvtimers"                 , "TV Timers",
  "videobookmarks"           , "Video Bookmarks",
  "videofiles"               , "Video Files",
  "videomenu"                , "Video Menu",
  "videooverlay"             , "Video Overlay",
  "videoplaylist"            , "Video Playlist",
  "videos,movies"            , "Movies",
  "videos,movietitles"       , "Movie Titles",
  "videos,musicvideos"       , "Music Videos",
  "videos,recentlyaddedepisodes"    , "Recently Added Episodes",
  "videos,recentlyaddedmovies"      , "Recently Added Movies",
  "videos,recentlyaddedmusicvideos" , "Recently Added Music Videos",
  "videos,tvshows "          , "TV Shows",
  "videos,tvshowtitles "     , "TV Show Titles",
  "videossettings"           , "Videos Settings",
  "videotimeseek"            , "Video Time Seek",
  "visualisationpresetlist"  , "Vis. Preset List",
  "weathersettings"          , "Weather Settings"
]

_windows = [
  "global"                   , "Global",
  "fullscreenvideo"          , "FullscreenVideo",
  "visualisation"            , "Visualisation",
  "fullscreenlivetv"         , "FullscreenLiveTV",
  "fullscreenradio"          , "FullscreenRadio",
  "slideshow"                , "Slideshow",
  "fullscreengame"           , "FullscreenGame",
  "videomenu"                , "VideoMenu",
  "playerprocessinfo"        , "PlayerProcessInfo",
  "home"                     , "Home",
  "programs"                 , "Programs",
  "videos"                   , "Videos",
  "music"                    , "Music",
  "pictures"                 , "Pictures",
  "weather"                  , "Weather",
  "filemanager"              , "FileManager",
  "tvchannels"               , "TVChannels",
  "radiochannels"            , "RadioChannels",
  "tvguide"                  , "TVGuide",
  "radioguide"               , "RadioGuide",
  "teletext"                 , "Teletext",
  "pvrosdteletext"           , "PVROSDTeletext (deprecated)",
  "pvr"                      , "PVR (deprecated)",
  "virtualkeyboard"          , "VirtualKeyboard",
  "numericinput"             , "NumericInput",
  "playercontrols"           , "PlayerControls",
  "seekbar"                  , "Seekbar",
  "videoosd"                 , "OSD-Video",
  "musicosd"                 , "OSD-Music",
  "osdvideosettings"         , "OSD-VideoSettings",
  "osdaudiosettings"         , "OSD-AudioSettings",
  "osdsubtitlesettings"      , "OSD-SubtitleSettings",
  "gameosd"                  , "OSD-Game"
]

from collections import OrderedDict
from utils import rpc


def action_dict(actions, action_names):
    """Create dict of action->name sorted by name"""
    return OrderedDict(sorted(zip(actions, action_names), key=lambda t: t[1]))


def _get_run_addon_actions():
    addons = []
    addon_types = ['xbmc.python.pluginsource', 'xbmc.python.script', 'xbmc.python.lyrics']
    for addon_type in addon_types:
        response = rpc('Addons.GetAddons', type=addon_type, properties=['name', 'enabled'])
        res = response['result']
        if 'addons' in res:
            addons.extend([a for a in res['addons'] if a['enabled']])
    actions = ['runaddon(%s)' % a['addonid'] for a in addons]
    names = ['Launch %s' % a['name'] for a in addons]
    return action_dict(actions, names)


def _get_activate_window_actions():
    all_windows = _activate_window + _windows[2:] #don't include "global"
    actions = ["activatewindow(%s)" % w_id for w_id in all_windows[0::2]]
    names = ["Open %s" % w for w in all_windows[1::2]]
    return action_dict(actions, names)


def _get_action_dict():
    """ Map actions to 'category name'->'action id'->'action name' dict"""
    d = OrderedDict()
    for elem in _actions:
        category = elem[0]
        actions = elem[1][0::2]
        names = elem[1][1::2]
        d[category] = OrderedDict(zip(actions, names))

    d["Windows"] = _get_activate_window_actions()
    d["Add-ons"] = _get_run_addon_actions()
    return d


ACTIONS = _get_action_dict()
WINDOWS = OrderedDict(zip(_windows[0::2], _windows[1::2]))
