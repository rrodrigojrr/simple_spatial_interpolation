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

def RBF(x, y, z, xi, yi):
    '''
    Função para calcular o método Radial Basis Function de interpolação

    x  -> Longitude do ponto observado;
    y  -> Latitude do ponto observado;
    z  -> Variável observada;
    xi -> Longitude do ponto a ser estimado;
    yi -> Latitude do ponto a ser estimado

    '''
    dist = distance_matrix(x,y, xi,yi)

    # Mutual pariwise distances between observations
    internal_dist = distance_matrix(x,y, x,y)

    # Now solve for the weights such that mistfit at the observations is minimized
    weights = np.linalg.solve(internal_dist, z)

    # Multiply the weights for each interpolated point by the distances
    zi =  np.dot(dist.T, weights)
    return zi

