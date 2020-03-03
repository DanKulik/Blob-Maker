import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt


def mk_blob(**kwargs):
    '''Makes a blob by generating a circle with a variable radius based on a
       set distribution function and applying Gaussian filter to smooth through
       the data

       **kwargs include:
         dist: the distribution functions include vonmises, wald, and normal
         value: integer value for the 1st component of each numpy function
         scale: integer value for the 2st component of each numpy function
         size: array size
         sigma: sigma vale for the Gaussian filter
         plot: Boolean plot setting

        returns x and y array values
    '''

    dist = 'normal'
    val = 1
    scale = 0
    size = 100
    sigma = 2
    plot = 'False'

    for key, component in kwargs.items():
        if key == 'dist':
            dist = component
        if key == 'value':
            val = component
        if key == 'size':
            size = component
        if key == 'scale':
            scale = component
        if key == 'sigma':
            sigma = component
        if key == 'plot':
            plot = component

    if ((dist == 'wald') or (dist == 'vonmises')) & (scale == 0):
        scale = 100
    elif scale == 0:
        scale = 0.15 
        
    if dist=='wald':
        r = np.random.wald(val, scale, size=size)
    elif dist=='vonmises':
        r = np.random.vonmises(val, scale, size=size)
    else:
        r = np.random.normal(val, scale, size=size)

    theta = np.linspace(np.pi/2, 5*np.pi/2, size)

    x = r*np.cos(theta)
    y = r*np.sin(theta)

    x = np.append(x,x[0])
    y = np.append(y,y[0])

    x = gaussian_filter(x, sigma=sigma)
    y = gaussian_filter(y, sigma=sigma)
    x[size] = x[0]
    y[size] = y[0]
    
    if plot:
        plt.plot(x,y)
        plt.show()

    return x,y
