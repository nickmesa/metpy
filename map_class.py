import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import geopandas
from cartopy import crs as ccrs
import cartopy.feature as cfeature

class Map:

    def __init__(self, extent, projection = ccrs.PlateCarree()):
        self.fig = plt.figure(1, figsize = (1280/72, 720/72))        
        self.ax = plt.subplot(1,1,1, projection = ccrs.PlateCarree())
        self.ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
        self.ax.add_feature(cfeature.STATES.with_scale('10m'))
        self.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
        self.ax.add_feature(cfeature.LAND.with_scale('50m'))
        self.ax.set_extent(extent, projection)
    
    def title(self, my_title):
        self.title = plt.title(label = my_title)
    
    def savefig(self, filename):
        self.save = plt.savefig(filename)

    def showfig(self):
        self.show = plt.show()

new_map = Map([-100, -10, 5, 42])

cat_gdf = geopandas.read_file('https://www.nhc.noaa.gov/xgtwo/gtwo_shapefiles.zip')

cat_plot_colors = {'Low': 'yellow', 'Medium': 'orange', 'High': 'red'}

for key in cat_plot_colors.keys():
    geometries = cat_gdf[cat_gdf['RISK5DAY'] == key]
    if len(geometries) > 0:
        new_map.ax.add_geometries(geometries['geometry'], crs = ccrs.PlateCarree(), facecolor = cat_plot_colors[key], edgecolor = 'black', alpha = 0.5)

new_map.title('National Hurricane Center Tropical Weather Outlook')

#new_map.legend(cat_plot_colors)

new_map.savefig('TWO.png')

new_map.showfig()
