"""
Method to calculate NDVI index on a numpy array representing a multiband raster dataset
"""
import numpy as np
import os
from multiprocessing import current_process
import logging
logger = logging.getLogger()

def create_ndvi_array(input_raster_array):
    """
    :param input_raster_array: input numpy array representing raster with shape [bands, rows, columns],
    input array should also have NoData mask included.
    The input raster is expected to have a red and near infrared band as the first and fourth bands respectively.
    :return: NDVI numpy array
    """

    red = input_raster_array[0, :, :]
    nir = input_raster_array[3, :, :]
    red = np.ma.masked_where(nir+red == 0, red)
    ndvi = np.empty([1, input_raster_array.shape[1], input_raster_array.shape[2]])
    ndvi[0, :, :] = (nir - red) / (nir + red)
    return ndvi


