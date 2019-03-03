# -*- coding: utf-8 -*-

import os, sys
from skimage import io
from skimage import img_as_ubyte

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pyimg"))

from refine import remove_weak_connection


def test_remove_weak_connection():
    img_path = os.path.join(TEST_PATH, "data/input/0000106b_img.png")
    ori_img = io.imread(img_path)
    bin_img = ori_img > 0
    refine_img = remove_weak_connection(bin_img)
    refine_img = img_as_ubyte(refine_img)

    save_path = os.path.join(TEST_PATH, "data/output/0000106b_refine.png")
    io.imsave(save_path, refine_img)
