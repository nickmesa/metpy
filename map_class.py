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
    def title(self, my_title):
        ax.set_title(label = f'{my_title}')