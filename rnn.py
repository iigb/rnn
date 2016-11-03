#!/usr/bin/python3
# E.L. 11/2/16

import shutil, sys, re

def doRename(f):
    # clean up funky filenames... no blanks or non alphanumeric

    # convert blanks to underscore
    f = '_'.join(f.split())

    # zap anything not alphanumeric and dot, slash, underscore
    f = re.sub("[^a-zA-Z0-9_./]+", "", f)

    # cut down multiple underscore _____ into single underscore
    f = re.sub("[_]+","_",f)
    return (f)


def main():
    if len(sys.argv) < 2:
        sys.exit('Insufficient args')

    for fin in sys.argv[1:]:
        t = doRename(fin)
        if t != fin:
            shutil.move(fin, t)

if __name__ == '__main__':
    main()
