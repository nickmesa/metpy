import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import geopandas
from cartopy import crs as ccrs
import cartopy.feature as cfeature

cat_gdf = geopandas.read_file('https://www.nhc.noaa.gov/xgtwo/gtwo_shapefiles.zip')

# print(cat_gdf['PROB5DAY'])

#map_crs = ccrs.LambertConformal(central_latitude=35, central_longitude=-100, standard_parallels=(30,60))
#data_crs = ccrs.LambertConformal(central_latitude=cat_gdf.crs['lat_0'], central_longitude=cat_gdf.crs['lon_0'], standard_parallels=(cat_gdf.crs['lat_1'], cat_gdf.crs['lat_2']))

cat_plot_colors = {'Low': 'yellow', 'Medium': 'orange', 'High': 'red'}

fig = plt.figure(1, figsize = (14,12))
ax = plt.subplot(1,1,1, projection = ccrs.PlateCarree())
ax.set_extent([-100, -10, 5, 42], ccrs.PlateCarree())

ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))
ax.add_feature(cfeature.OCEAN.with_scale('50m'))
ax.add_feature(cfeature.LAND.with_scale('50m'))

for key in cat_plot_colors.keys():
    geometries = cat_gdf[cat_gdf['RISK5DAY'] == key]
    if len(geometries) > 0:
        ax.add_geometries(geometries['geometry'], crs = ccrs.PlateCarree(), facecolor = cat_plot_colors[key], edgecolor = 'black', alpha = 0.5)

ax.set_title(label = 'National Hurricane Center Tropical Weather Outlook')


ax.legend(cat_plot_colors)

plt.savefig('TWO.png')

plt.show()
