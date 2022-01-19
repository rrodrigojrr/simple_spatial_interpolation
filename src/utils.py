
import numpy as np


def reshape_grid(x,y,z):
    new_z = z.reshape((len(x), len(y))).T
    lon, lat = np.meshgrid(x, y)
    return lon, lat, new_z


def coordsTransform(x,y):

    lon = np.array([])
    lat = np.array([])

    for i in x:
        for j in y:
            lon = np.append(lon, i)
            lat = np.append(lat, j)

    return lon, lat

