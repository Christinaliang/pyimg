# -*- coding: utf-8 -*-

import os, sys
import numpy as np

__all__ = ['PIL2npArr',
           ]


def PIL2npArr(pil_img):
    """ Convert Pillow image to numpy array.

    """

    np_img = np.asarray(pil_img)
    if len(np_img.shape) == 2:
        pass
    elif len(np_img.shape) == 3:
        if np_img.shape[2] == 4:
            np_img = np_img[...,:-1]
    else:
        raise NotImplementedError()

    return np_img
