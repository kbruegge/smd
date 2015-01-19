__author__ = 'kai'

import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pylab as plt


def main():
    temp, forecast, humidity = np.genfromtxt("tabelle.csv", delimiter=",", usecols=[0,1,2], unpack=True)
    wind, label = np.genfromtxt("tabelle.csv", delimiter=",", usecols=[3,4], unpack=True, dtype=np.bool)

    ig = information_gain_binary(wind, label)
    print("Entropy of label bits: " + str(ig))

    temperature_cuts = np.arange(18, 29, 1)
    igs_temp = information_gain_for_cuts(temperature_cuts, temp, label)


    humidity_cuts = np.arange(65, 95, 5)
    igs_humidity = information_gain_for_cuts(humidity_cuts, humidity, label)

    forecast_cuts = np.arange(0, 2, 1)
    igs_forecast = information_gain_for_cuts(forecast_cuts, forecast, label)


    # print(igs_temp)
    # print(igs_humidity)
    # print(igs_forecast)
    fig, (top, center, bottom) = plt.subplots(nrows=3, ncols=1)
    top.plot(temperature_cuts, igs_temp, 'bo', label="Temperature" )
    top.set_ylabel('IG Temperature')
    # top.set_xlabel('Cut')
    center.plot(humidity_cuts, igs_humidity, 'go', label="Humidity")
    center.set_ylabel('IG Humidity')

    bottom.plot(forecast_cuts, igs_forecast,'ro',  label="Forecast")
    bottom.set_ylabel('IG Forecast')

    top.set_xlim([17, 29])
    center.set_xlim([60, 95])
    bottom.set_xlim([-0.2, 1.2])

    fig.suptitle('Information Gain', fontsize=14, fontweight='bold')

    plt.savefig("plots.png")


def information_gain_for_cuts(cuts, X, label):
    igs = []
    for cut in cuts:
        X_c = X > cut
        # print(X_c)
        igs.append(information_gain_binary(X_c, label))
    return  igs


def information_gain_binary(X, label):
    p_F, p_T = np.bincount(X)/float(np.size(X))

    label_f = label[X==False]
    label_t = label[X==True]

    H = binary_entropy(label)

    H_X = p_T*binary_entropy(label_t) + p_F*binary_entropy(label_f)

    return H - H_X



def binary_entropy(a):
    f, t = np.bincount(a)/float(np.size(a))
    if f == 0:
        return - t * np.log2(t)
    if t == 0:
        return - f * np.log2(f)
    return - f * np.log2(f) - t * np.log2(t)




if __name__ == '__main__':
    main()