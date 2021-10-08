import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import geopandas
from cartopy import crs as ccrs
import cartopy.feature as cfeature

class map:

    fig = plt.figure(1, figsize = (14,12))
    ax = plt.subplot(1,1,1, projection = ccrs.PlateCarree())

    def __init__(self): 
        pass
    
    @classmethod
    def title(cls, my_title):
        plt.title(label = f'{my_title}')

    @classmethod
    def legend(cls,colors):
        plt.legend(cat_plot_colors)
    
map.fig
map.ax

cat_gdf = geopandas.read_file('https://www.nhc.noaa.gov/xgtwo/gtwo_shapefiles.zip')

cat_plot_colors = {'Low': 'yellow', 'Medium': 'orange', 'High': 'red'}

map.ax.set_extent([-100, -10, 5, 42], ccrs.PlateCarree())

map.ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
map.ax.add_feature(cfeature.STATES.with_scale('50m'))
map.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
map.ax.add_feature(cfeature.LAND.with_scale('50m'))

for key in cat_plot_colors.keys():
    geometries = cat_gdf[cat_gdf['RISK5DAY'] == key]
    if len(geometries) > 0:
        map.ax.add_geometries(geometries['geometry'], crs = ccrs.PlateCarree(), facecolor = cat_plot_colors[key], edgecolor = 'black', alpha = 0.5)

map.title('National Hurricane Center Tropical Weather Outlook')

map.legend(cat_plot_colors)

plt.savefig('TWO.png')

plt.show()
