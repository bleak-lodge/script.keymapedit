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

import os
import sys
import shutil
import traceback
import xbmc
import utils
from editor import Editor


default = utils.transPath('special://xbmc/system/keymaps/keyboard.xml')
userdata = utils.transPath('special://userdata/keymaps')
gen_file = os.path.join(userdata, 'gen.xml')


def main():
    ## load mappings ##
    try:
        if not os.path.exists(userdata):
            os.makedirs(userdata)
    except Exception:
        traceback.print_exc()
        utils.rpc('GUI.ShowNotification', title="Keymap Editor",
            message="Failed to remove old keymap file", image='error')
        return

    defaultkeymap = utils.read_keymap(default)
    userkeymap = []
    if os.path.exists(gen_file):
        try:
            userkeymap = utils.read_keymap(gen_file)
        except Exception:
            traceback.print_exc()
            utils.rpc('GUI.ShowNotification', title="Keymap Editor",
                      message="Failed to load keymap file", image='error')
            return

    ## main loop ##
    confirm_discard = False
    while True:
        idx = utils.Dialog().select(utils.tr(30000), [utils.tr(30003), utils.tr(30004), utils.tr(30005)])
        if idx == 0:
            # edit
            editor = Editor(defaultkeymap, userkeymap)
            editor.start()
            confirm_discard = editor.dirty
        elif idx == 1:
            # reset
            confirm_discard = bool(userkeymap)
            userkeymap = []
        elif idx == 2:
            #make sure there are no user defined keymaps
            for name in os.listdir(userdata):
                if name.endswith('.xml') and name != os.path.basename(gen_file):
                    src = os.path.join(userdata, name)
                    for i in range(100):
                        dst = os.path.join(userdata, "%s.bak.%d" % (name, i))
                        if os.path.exists(dst):
                            continue
                        shutil.move(src, dst)
                        #successfully renamed
                        break
            # save
            if os.path.exists(gen_file):
                shutil.copyfile(gen_file, gen_file + ".old")
            utils.write_keymap(userkeymap, gen_file)
            xbmc.executebuiltin("Action(reloadkeymaps)")
            break
        elif idx == -1 and confirm_discard:
            if utils.Dialog().yesno(utils.tr(30000), utils.tr(30006)) == 1:
                break
        else:
            break

    sys.modules.clear()

if __name__ == "__main__":
    main()
