# -*- coding: utf-8 -*-

# import os, sys
# # import numpy as np
#
# FILE_PATH = os.path.abspath(__file__)
# TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
# PRJ_PATH = os.path.dirname(TEST_PATH)
# sys.path.insert(0, os.path.join(PRJ_PATH, "pyimg"))
#
# DATA_DIR = os.path.join(TEST_PATH, "data")
# # from combine import graymask2rgb


# def test_graymask2rgb():
#     mask_img_path = os.path.join(DATA_DIR, "gray/gray123.png")
#
#     try:
#         mask_img = misc.imread(mask_img_path)
#     except:
#         print("Load {} error.".format(mask_img_path))

#     # import matplotlib.pyplot as plt
#     # plt.imshow(mask_img, cmap='gray')
#     # plt.show()
#
#     mask_rgb = graymask2rgb(mask_img, channel='r')

#     # import matplotlib.pyplot as plt
#     # plt.imshow(mask_rgb)
#     # plt.show()
