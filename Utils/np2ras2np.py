"""
Methods to convert a single or multiband raster to numpy array and vice versa

"""
import gdal
import numpy as np

def raster2nparray(input_ras):
    """
    :param input_ras: Input Raster
    :return: NumPy array from a Raster; single or multi-band
    and other raster properties such as originX, originY, cellSize, spatial reference & NoDataValue
    """
    # Open the input DEM data and get properties
    raster_obj = gdal.Open(input_ras)
    geotransform = raster_obj.GetGeoTransform()
    originX = geotransform[0]
    originY = geotransform[3]
    cellsize = geotransform[1]
    spatialref = raster_obj.GetSpatialRef()

    num_bands = raster_obj.RasterCount
    num_cols = raster_obj.RasterXSize
    num_rows = raster_obj.RasterYSize

    nparray = np.empty([num_bands, num_rows, num_cols])
    ndvals = []

    # Get all bands
    for band in range(num_bands):
        raster_band = raster_obj.GetRasterBand(band+1)
        # Read cells as a numpy array
        nparray[band,:,:] = raster_band.ReadAsArray()
        # Get the NoData value
        ndvals.append(raster_band.GetNoDataValue())

    return nparray, originX, originY, cellsize, spatialref, ndvals

def nparray2ras(nparray, outRasterPath, cellSize, rasterOrigin, spRef, ndVals):
    """

    :param nparray: Input NumPy Array
    :param outRasterPath: Output raster Path
    :param cellSize: Output raster cell size
    :param rasterOrigin: Output raster origin as a list with [X, Y] coord values
    :param spRef: Output raster spatial reference
    :return: None
    """

    #start creating the output raster and write to it
    gdalDriver = gdal.GetDriverByName('GTiff')
    output_raster = gdalDriver.Create(outRasterPath, nparray.shape[2], nparray.shape[1], nparray.shape[0], gdal.GDT_Float32)
    output_raster.SetGeoTransform((rasterOrigin[0], cellSize, 0, rasterOrigin[1], 0, -cellSize))
    for band in range(output_raster.RasterCount):
        output_band = output_raster.GetRasterBand(band+1)
        output_band.WriteArray(nparray[band, :, :])
        output_band.SetNoDataValue(ndVals[band])
    output_raster.SetProjection(spRef.ExportToWkt())
    output_raster.FlushCache()