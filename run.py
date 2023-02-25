import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

lon_left = 55
lat_bottom = 35
lon_right = 75
lat_top = 47

m = Basemap(llcrnrlon=lon_left, llcrnrlat=lat_bottom, urcrnrlon=lon_right, urcrnrlat=lat_top, resolution='l')

#m.drawcoastlines(linewidth=1.5, color='yellow')
m.drawcountries(linewidth=1.5, color='red')
#m.drawrivers(linewidth=0.5, color='blue')


m.fillcontinents(color='white', lake_color='blue', zorder=0)


city_lats = [40.79, 39.67, 41.38, 41.47, 40, 40.4, 40.56, 42.46, 40.50, 37.40,41.5,38.88,40.9]
city_lons = [72.36, 66.96, 69.28, 71.72, 65, 66.60, 68.62, 59.61, 70, 67.22,60.52,66.5,68]
city_names = ['Namangan', 'Samarkand', 'Tashkent', 'Andijan', 'Bukhara', 'Navoiy', 'Syrdarya', 'Karakalpakstan', 'Fergana', 'Surkhandarya', 'Khorezm','Kashkadarya','Jizzakh']

for lat, lon, name in zip(city_lats, city_lons, city_names):
    x, y = m(lon, lat)
    m.plot(x, y, 'bo', markersize=3, color='red', alpha=0.7)
    plt.text(x, y, name, fontsize=8, color='black', alpha=0.8, ha='center', va='center')

# Show the map
plt.show()
