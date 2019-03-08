# -*- coding: utf-8 -*-

import os, sys
from skimage import io
from skimage import img_as_ubyte

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pyimg"))

from refine import crop_center


def test_remove_weak_connection():
    # img_path = os.path.join(TEST_PATH, "data/input/0000106b_img.png")
    img_path = os.path.join(TEST_PATH, "data/input/AliceLake.jpg")
    img = io.imread(img_path)

    crop_img = crop_center(img, crop_h=200, crop_w=400)
    import matplotlib.pylab as plt
    plt.imshow(crop_img)
    # plt.show()
