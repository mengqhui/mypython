import argparse
import glob
import shelve
import os
from imagehash import *

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, default='./',
                help="path to input dataset of images")
ap.add_argument("-s", "--shelve", required=True, default='./hash.slv',
                help="output shelve database")
args = vars(ap.parse_args())

# open the shelve database
db = shelve.open(args["shelve"], writeback=True)
# loop over the image dataset
image_dataset = glob.glob(args["dataset"] + "/*.*")
for imagePath in image_dataset:
    # load the image and compute the difference hash
    image = Image.open(imagePath)
    h = str(dhash(image))

    # extract the filename from the path and update the database
    # using the hash as the key and the filename append to the
    # list of values
    filename = imagePath[imagePath.rfind("/") + 1:]
    print(filename)
    db[h] = db.get(h, []) + [filename]

# close the shelf database
db.close()
'''
l1 = glob.glob('*/*.*')
l2 = glob.glob('*/*/*.*')
l = l1+l2


def dhash_f(imagePath):
    image = Image.open(imagePath)
    h = str(dhash(image))
    return h


dhash_d = {dhash_f(ll): ll for ll in l}

ll = dhash_d.values()
for ls in ll:
    os.rename(ls, '02/' + ls)


dhash_l = list(map(dhash_f, l))
'''