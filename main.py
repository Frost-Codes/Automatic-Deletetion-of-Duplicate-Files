import os
import hashlib


def hash_file(filename):
    """Returns the hash value of file"""
    BLOCKSIZE = 65536
    harsher = hashlib.md5()
    with open(filename, 'rb') as file:
        buffer = file.read(BLOCKSIZE)
        while len(buffer) > 0:
            harsher.update(buffer)
            buffer = file.read(BLOCKSIZE)
    return harsher.hexdigest()


if __name__ == '__main__':
    hashMap = {}
    deletedFiles = []
    fileList = [file for file in os.listdir() if os.path.isfile(file)]
    for file in fileList:
        key = hash_file(file)
        if key in hashMap.keys():
            deletedFiles.append(file)
            os.remove(file)
        else:
            hashMap[key] = file
    if len(deletedFiles) != 0:
        print('Deleted files')
        for file in deletedFiles:
            print(file)
    else:
        print('No duplicate files')