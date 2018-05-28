#!/usr/bin/env python
import sys

if "__main__" == __name__:
    if len(sys.argv) != 3:
        print("%s <src_file> <dst_file>" % sys.argv[0])
        sys.exit(1)

    # read file
    hFileSrc = open(sys.argv[1], 'r')
    strText = hFileSrc.read()
    hFileSrc.close()

    # operate
    strText = strText.replace('\r', '')
    strText = strText.replace('\n\n', '\n')

    # write file
    hFileDst = open(sys.argv[2], "w")
    hFileDst.write(strText)
    hFileDst.close()

    print("fix succ!")
