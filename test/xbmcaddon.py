# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
''' This file implements the Kodi xbmcaddon module, either using stubs or alternative functionality '''

# pylint: disable=invalid-name,too-few-public-methods

from __future__ import absolute_import, division, print_function, unicode_literals

ADDON_ID = 'plugin.video.foobar'


class Addon:
    ''' A reimplementation of the xbmcaddon Addon class '''

    def __init__(self, id=ADDON_ID):  # pylint: disable=redefined-builtin
        ''' A stub constructor for the xbmcaddon Addon class '''
        self.id = id

    def getAddonInfo(self, key):
        ''' A working implementation for the xbmcaddon Addon class getAddonInfo() method '''
        addon_info = dict(id=self.id, name='Foobar', version='1.2.3', type='kodi.video', profile='special://userdata', path='special://userdata')
        return addon_info.get(key)
