__author__ = 'Kai'

import numpy as np
import matplotlib.pyplot as plt

#Verteilung nach InversionsMethode
def signal(y, gamma = 2.7, theta_0=50):
    #fF = theta_0 * (1/(-gamma + 1))*E**(-gamma + 1)
    E_inv = (y*(gamma + 1)/theta_0)**(1/(gamma+1))
    return 1/E_inv


def akzeptanz(E):
    y = np.random.random(len(E))

    v = (1-np.exp(-E/2))**3
    #return nur die Werte die die Akzeptanz überleben
    return E[y < v]

def hits(E):
    return 10*np.random.normal(E, 0.2*E, len(E))

def location(N):
    sigma = 1/(np.log10(N))
    x = np.random.normal(7, sigma, len(N))
    y = np.random.normal(3, sigma, len(N))
    return (x,y)



def background_hits(N_background):
    return np.exp(np.random.normal(2, 1, N_background))

def background_location(N_events):
    cov = [[9, 4.5], [4.5, 9]]
    a = np.random.multivariate_normal([0,0], cov, N_events)
    return a[:,0], a[:,1]

def main():
    
    #Produziere Signal events
    N_signal = 100000
    E = signal(np.random.random(N_signal))
    measured_events = akzeptanz(E)
    h = hits(measured_events)
    x, y = location(h)

    #plotten der Signal events
    fig, (top, center, bottom) = plt.subplots(nrows=3, ncols=1)
    top.hist(E, bins = 40)
    top.hist(measured_events, bins=40)
    center.hist(h, bins=40)
    bottom.hist2d(x, y, bins=40)
    
    
    #erzeugen der Hintergrund events
    b_hits = background_hits(10**7)
    x, y = background_location(10**7)
    #und das plotten
    fig, (top, bottom) = plt.subplots(nrows=2, ncols=1)
    top.hist(np.log(b_hits), bins=40)
    bottom.hist2d(x,y, bins=40)
    plt.show()

if __name__ == '__main__':
    main()
