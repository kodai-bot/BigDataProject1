import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile
sf = gpd.read_file("3a48037e-b329-418b-9b5b-ae75f67e070c2020329-1-1fr9fy9.c1p9.shp")

# Plot the shapefile
# sf.plot()
# plt.show()
sf.info()
