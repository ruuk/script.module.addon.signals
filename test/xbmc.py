# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
''' This file implements the Kodi xbmc module, either using stubs or alternative functionality '''

# pylint: disable=invalid-name,super-init-not-called,unused-argument

from __future__ import absolute_import, division, print_function, unicode_literals

import json
import time

LOGLEVELS = ['Debug', 'Info', 'Notice', 'Warning', 'Error', 'Severe', 'Fatal', 'None']
LOGDEBUG = 0
LOGINFO = 1
LOGNOTICE = 2
LOGWARNING = 3
LOGERROR = 4
LOGSEVERE = 5
LOGFATAL = 6
LOGNONE = 7


class Monitor:
    ''' A stub implementation of the xbmc Monitor class '''
    def __init__(self, line='', heading=''):
        ''' A stub constructor for the xbmc Monitor class '''

    @staticmethod
    def abortRequested():
        ''' A stub implementation for the xbmc Keyboard class abortRequested() method '''
        return False

    @staticmethod
    def waitForAbort():
        ''' A stub implementation for the xbmc Keyboard class waitForAbort() method '''
        return


def executebuiltin(string, wait=False):  # pylint: disable=unused-argument
    ''' A stub implementation of the xbmc executebuiltin() function '''
    return


def executeJSONRPC(jsonrpccommand):
    ''' A reimplementation of the xbmc executeJSONRPC() function '''
    command = json.loads(jsonrpccommand)
    log("executeJSONRPC does not implement method '{method}'".format(**command), 'Error')
    return json.dumps(dict(error=dict(code=-1, message='Not implemented'), id=1, jsonrpc='2.0'))


def log(msg, level=0):
    ''' A reimplementation of the xbmc log() function '''
    color1 = '\033[32;1m'
    color2 = '\033[32;0m'
    name = LOGLEVELS[level]
    if level in (4, 5, 6, 7):
        color1 = '\033[31;1m'
        if level in (6, 7):
            raise Exception(msg)
    elif level in (2, 3):
        color1 = '\033[33;1m'
    elif level == 0:
        color2 = '\033[30;1m'
    print('{color1}{name}: {color2}{msg}\033[39;0m'.format(name=name, color1=color1, color2=color2, msg=msg))


def sleep(timemillis):
    ''' A reimplementation of the xbmc sleep() function '''
    time.sleep(timemillis / 1000)
