import geopandas as gpd

# Load a shapefile
shapefile_path = "path_to_your_shapefile.shp"
gdf = gpd.read_file(shapefile_path)

# Print the first few rows of the GeoDataFrame
print(gdf.head())

# Plot the GeoDataFrame
gdf.plot()
