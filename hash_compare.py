import hashlib
import os
from pathlib import Path


def md5sum(filename):
    """
    用于获取文件的md5值
    :param filename: 文件名
    :return: MD5码
    """
    myhash = hashlib.md5()

    with open(filename, 'rb') as f:
        b = f.read()
        if b > 8096:
            b = b[:8096]
        myhash.update(b)
    return myhash.hexdigest()


if __name__ == "__main__":
    pa = ''
    p = Path(pa)
    filelist = list(p.glob('*/*'))
    for fl in filelist:
        {fl:md5sum(fl)}