#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

try:
    from .JSONFile import JSONFile
    from . import Paths
except:
    import Paths
    from libs.JSONFile import JSONFile


class Preferences(JSONFile):
    '''
    Class to handle the preferences of the plugin

    Extends: JSONFile
    '''

    def __init__(self):
        '''
        Path loads the file where the preferences are stored,
        Doing that you avoid to pass the path every time you
        need to get or set any preference.
        '''
        path = Paths.getPreferencesFile()
        super(Preferences, self).__init__(path)

    def set(self, key, value):
        '''
        Save a value in the preferences file using a list and
        dictionaries.

        Arguments: key {string} -- identifier of the preference
                   value {[type]} -- value of the preference
        '''
        self.data[key] = value
        self.saveData()

    def get(self, key, default_value=False):
        '''
        Get a value in the preferences file stored as a list and
        dictionaries format.

        Arguments:
        key {string} -- identifier of the preference
        default_value {string} -- if there is none value stored
                    you can set a default value (default: False)

        Returns: {string} -- Value of the preference
        '''
        value = self.data.get(key, default_value)
        return value

    def boardSelected(self, board_id):
        '''
        Add or delete the board selected from the preferences
        files. The boards are formated in a dictionary in the
        the list 'board id'

        Arguments: board_id {string} -- identifier if the board selected
        '''
        remove = False
        type = 'board_id'
        native = self.get('native', False)
        if(native):
            type = 'found_ini'

        file_data = self.get(type, '')
        if(file_data):
            if board_id in file_data:
                remove = True
                self.data.setdefault(type, []).remove(board_id)
                try:
                    self.set('env_selected', '')
                except:
                    pass
            else:
                self.data.setdefault(type, []).append(board_id)
            self.saveData()
        else:
            self.set(type, [board_id])
        return remove

    def checkBoard(self, board_id):
        '''
        Check if is necessary to mark or unmark the board selected

        Arguments: board_id {string} -- identifier of the board selected
        '''
        native = self.get('native', False)
        check = False
        key = 'board_id'

        if(native):
            key = 'found_ini'

        if(self.data):
            check_boards = self.get(key, '')

            if board_id in check_boards:
                check = True
        return check
