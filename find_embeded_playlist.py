#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint

# Assumptions:  unique names
# Assumption: data is always 'type:playlistname' where type is 'folder...' info or 'playlist'
# Assumption: clean data

all_playlists = ["playlist:my-favorites", "folder-start:genres", "folder-start:rock", "playlist:best-of-rock", "folder-end:rock", "folder-end:genres", "playlist:old-stuff"]
find_playlist = "best-of-rock"


def findplaylist( all_lists, playlist):
    mylist = ['/']
    for items in all_lists:
        list_type, item_name = items.split(':')
        if list_type == 'folder-start':
            mylist.append(item_name)
            continue
        if list_type == 'folder-stop':
            mylist.pop()
            continue
        if item_name == playlist:
            return mylist

print findplaylist(all_playlists, find_playlist)
