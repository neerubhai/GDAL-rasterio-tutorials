# GDAL-rasterio-tutorials  🌍📈

Welcome to GDAL-rasterio-tutorials, your go-to resource for mastering raster data processing with GDAL and Rasterio! 🚀 Whether you're a GIS professional, an environmental scientist, or just passionate about geospatial data, these tutorials are designed to enhance your skills in handling, analyzing, and visualizing raster data. Dive into these tutorials and start transforming raw data into insightful geospatial information.
____________________________

### Tutorial 1 - Calculate NDVI index. 🌱
In this tutorial, you'll learn the following:
1. Basics of reading a raster (single or multi-band) using GDAL Python API. 
2. Procure data from raster cells and transfer it to a numpy array. Procure raster properties such cell size, origin (X, Y), spatial reference and NoDataValue.
3. Peform a local raster operation across various bands. A local raster operation is a simple raster operation that uses only data at a cell location in the input to compute a value at that same location in the output raster. You'll learn this by calculating NDVI index that used red and NIR band values at every cell location.
3. Write a raster dataset to disk and transfer the properties of the input raster to it, such as cell size, origin, spatial reference along with an appropriate NoDataValue selected based on the known or expected output value range. 
4. Visualize your data (input and output) using rasterio.plot submodule.

____________________________
### Tutorial 2 - Applying a spatial filter over a moving kernel.🔍
In this tutorial, you'll learn the following:
1. Apply a spatial filter over a moving window on a raster dataset.
2. Use utilities from built-in customized modules such as 'raster to numpy' and 'numpy to raster' to aid in the application of this filter.
3. Script a moving window.
4. Deal with boundary conditions.
4. Work with Digital Elevation Model (DEM) data.
5. Handle NoDataValues while performing analysis.

____________________________
### Tutorial 3 - Speed up analysis with concurrent and parallel processing techniques ⚡
In this tutorial, you'll learn the following:
1. How to speed up your analysis using concurrent processing
2. How to speed up your analysis using parallel processing
3. Compare concurrent and parallel processing against serialized execution and understand the speed up in performance.
