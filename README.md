# GDAL-rasterio-exercises

____________________________

Tutorial 1 - Calculate NDVI index.
In this tutorial, you'll learn the following:
1. Basics of reading a raster (single or multi-band) using GDAL Python API. 
2. Procure data from raster cells and transfer it to a numpy array. Procure raster properties such cell size, origin (X, Y), spatial reference and NoDataValue.
3. Peform a local raster operation across various bands. A local raster operation is a simple raster operation that uses only data at a cell location in the input to compute a value at that same location in the output raster. You'll learn this by calculating NDVI index that used red and NIR band values at every cell location.
3. Write a raster dataset to disk and transfer the properties of the input raster to it, such as cell size, origin, spatial reference along with an appropriate NoDataValue selected based on the known or expected output value range. 
4. Visualize your data (input and output) using rasterio.plotting submodule.
