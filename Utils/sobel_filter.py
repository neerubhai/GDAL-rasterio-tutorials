"""
Method to apply a Sobel filter for edge detection
on an input numpy array that represents a single-
or multi-band raster dataset with 3 dimensions
representing [bands, rows, columns]
"""

import numpy as np
def sobelFiterOnArray(input_array):
    """
    :param input_array: input numpy array representing raster with shape [bands, rows, columns],
    input array should also have NoData mask included
    :return: output array with Sobel filter applied
    """
    Gx = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])

    Gy = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]])

    output_array = np.empty(input_array.shape)

    n_bands = input_array.shape[0]
    n_row = input_array.shape[1]
    n_col = input_array.shape[2]

    # Loop through each raster cell
    for band in range(n_bands):
        for row in range(n_row - 1):
            for col in range(n_col - 1):
                sum_Gx = 0
                sum_Gy = 0

                """Use this flag to check for NoData presence in a moving window, 
                if any cell in the window is noData the output value is NoData
                """
                nodata_in_window = False

                # Create a moving window at each cell:
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        # Check for NoData
                        if nodata_in_window == False and input_array.mask[band, row + i, col + j] == False:
                            sum_Gx += input_array[band, row + i, col + j] * Gx[i + 1, j + 1]
                            sum_Gy += input_array[band, row + i, col + j] * Gy[i + 1, j + 1]
                        elif input_array.mask[band, row + i, col + j] == True:
                            nodata_in_window = True
                if nodata_in_window == False:
                    output_array[band, row, col] = (sum_Gx ** 2 + sum_Gy ** 2) ** 0.5
                else:
                    output_array[band, row, col] = input_array.fill_value

    return output_array

