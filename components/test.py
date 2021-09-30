from PIL import Image
from typing import Union
import numpy as np
import os


def resize(fp: str, scale: Union[float, int]) -> np.ndarray:
    """ Resize an image maintaining its proportions
    Args:
        fp (str): Path argument to image file
        scale (Union[float, int]): Percent as whole number of original image. eg. 53
    Returns:
        image (np.ndarray): Scaled image
    """
    _scale = lambda dim, s: int(dim * s / 100)
    im = Image.open(fp)
    width, height = im.size
    new_width: int = _scale(width, scale)
    new_height: int = _scale(height, scale)
    new_dim: tuple = (new_width, new_height)
    try:os.remove(fp)
    except:pass
    im.resize(new_dim).save(fp)
resize("./components/assets/ntpd.png",150)