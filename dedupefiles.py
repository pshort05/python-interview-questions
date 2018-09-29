#  Scan a directory structure and replace any duplicate files with a link to the first file

import os
import hashlib

def dedup(current, original):
    os.remove(current)
    os.link(original, current)
    print "Linking {} to {}".format(current, original)


def get_file_hash(path):
    with open(path, 'rb') as f:
        buffer = f.read()
        return hashlib.sha1(buffer)


file_store = {}

def scan_files(directory):

    root = os.listdir(directory)
    for item in root:
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            scan_files(full_path)
        elif os.path.isfile(full_path):
            hashed = get_file_hash(full_path)
            if hashed in file_store:
                dedup(full_path, file_store.get(hashed))
                pass
            else:
                print hashed, full_path
                file_store[hashed] = full_path
                #file_store.update({hashed,full_path})
            pass
        pass  # not a file nor directory
    pass  # done traversing files in root
    return



scan_files('/Users/pshort/Downloads/')
