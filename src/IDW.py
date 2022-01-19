import numpy as np


def distance_matrix(x0, y0, x1, y1):
    ''' Função para calcular a distância entre dois pontos no espaço'''
    obs = np.vstack((x0, y0)).T
    interp = np.vstack((x1, y1)).T

    # Make a distance matrix between pairwise observations
    # Note: from <http://stackoverflow.com/questions/1871536>
    # (Yay for ufuncs!)
    d0 = np.subtract.outer(obs[:,0], interp[:,0])
    d1 = np.subtract.outer(obs[:,1], interp[:,1])

    return np.hypot(d0, d1)


def IDW(x, y, z, xi, yi, n=2):
    '''
    Função para calcular o método Inverse Distance Weithing de interpolação

    x  -> Longitude do ponto observado;
    y  -> Latitude do ponto observado;
    z  -> Variável observada;
    xi -> Longitude do ponto a ser estimado;
    yi -> Latitude do ponto a ser estimado
    n  -> Potência da distância. 

    '''
    dist = distance_matrix(x,y, xi,yi)

    # In IDW, weights are 1 / distance
    weights = 1.0 / dist ** n

    # Make weights sum to one
    weights /= weights.sum(axis=0)

    # Multiply the weights for each interpolated point by all observed Z-values
    zi = np.dot(weights.T, z)
    return zi