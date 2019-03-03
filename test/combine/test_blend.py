# -*- coding: utf-8 -*-

# import os, sys
# import numpy as np
#
# FILE_PATH = os.path.abspath(__file__)
# TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
# PRJ_PATH = os.path.dirname(TEST_PATH)
# sys.path.insert(0, os.path.join(PRJ_PATH, "pyimg"))
#
# DATA_DIR = os.path.join(TEST_PATH, "data")
# from combine import blend_images
# from combine import graymask2rgb


# def test_blend_images():
#     mask_path = os.path.join(DATA_DIR, "input/input123.png")
#     img_path = os.path.join(DATA_DIR, "gray/gray123.png")
#     # Read mask and image
#     mask = misc.imread(mask_path)
#     img = misc.imread(img_path)
#     # Convert mask to rgb
#     mask_rgb = graymask2rgb(mask, 'r')
#     # combine img and mask_rgb
#     combine = blend_images(img, mask_rgb, 0.8)

#     # import matplotlib.pyplot as plt
#     # plt.imshow(combine)
#     # plt.show()
