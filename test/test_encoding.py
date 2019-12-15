# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v2.0 (see COPYING or https://www.gnu.org/licenses/gpl-2.0.txt)

# pylint: disable=invalid-name,missing-docstring

from __future__ import absolute_import, division, print_function, unicode_literals
import unittest
import AddonSignals

xbmc = __import__('xbmc')
xbmcaddon = __import__('xbmcaddon')


class TestEncoding(unittest.TestCase):

    def test_addon_signals(self):
        data = 'Fòöbàr'
        base64_encoded_data = 'IkZcdTAwZjJcdTAwZjZiXHUwMGUwciI='
        base64_encoded_fmtjson = '\\"[\\"%s\\"]\\"' % base64_encoded_data
        base64_encoded_json = '["%s"]' % base64_encoded_data

        encoded_data = AddonSignals._encodeData(data)  # pylint: disable=protected-access
        self.assertEqual(encoded_data, base64_encoded_fmtjson)

        decoded_data = AddonSignals._decodeData(base64_encoded_json)  # pylint: disable=protected-access
        self.assertEqual(decoded_data, data)
