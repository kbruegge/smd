__author__ = 'kai'

import ROOT
from root_numpy import root2array, root2rec
import numpy as np
from scipy.spatial import KDTree


def main():
    filename = '../Blatt7.root'

    signal_size = 10000
    background_size = 20000

    print("Reading Data from file " + filename)
    background = root2rec(filename, 'Untergrund_MC', branches=['AnzahlHits', 'x', 'y'])
    signal = root2rec(filename, 'Signal_MC_Akzeptanz', branches=['AnzahlHits', 'x', 'y'])

    background = np.asarray([background['AnzahlHits'], background['x'], background['y']]).T
    signal = np.asarray([signal['AnzahlHits'], signal['x'], signal['y']]).T



    training = np.append(signal[:5000],background[:5000], axis=0)
    label =  np.append(np.ones(5000,  dtype=np.int), np.zeros(5000,  dtype=np.int), axis=0)

    test_data = np.append(signal[:signal_size],background[:background_size], axis=0)
    test_label =  np.append(np.ones(signal_size,  dtype=np.int), np.zeros(background_size,  dtype=np.int), axis=0)


    print("Creating KD-Tree")
    kd = KDTree(training, leafsize=20)
    print("Starting prediction with k = 10")
    prediction = knn(data=test_data, label=label, tree=kd, k=10)
    performance(label=test_label, prediction=prediction)

    print("Starting prediction with k = 20")
    prediction = knn(data=test_data, label=label, tree=kd, k=20)
    performance(label=test_label, prediction=prediction)


    print("Using log(AnzahlHits)")
    #new training and test data for log10(AnzahlHits)
    background[:,0] = np.log10(background[:,0])
    signal[:,0] = np.log10(signal[:,0])
    training = np.append(signal[:5000], background[:5000], axis=0)
    test_data = np.append(signal[:signal_size], background[:background_size], axis=0)
    print("Creating KD-Tree")
    kd = KDTree(training, leafsize=20)
    print("Starting prediction")
    prediction = knn(data=test_data, label=label, tree=kd, k=10)
    performance(label=test_label, prediction=prediction)



def knn(data,label, tree, k=10):
    prediction = np.zeros(np.shape(data[:,0]))

    for i, d in enumerate(data):
        points, indeces = tree.query(d, k=k)
        #count number of ones and zeros in label. and return the number of the higher bin.
        prediction[i] = np.argmax(np.bincount(label[indeces]))

    return prediction

def performance(label, prediction):
    tp, tn = np.bincount(label[(prediction == label)]).astype(dtype=np.float)
    fp, fn = np.bincount(label[(prediction != label)]).astype(dtype=np.float)


    print("Confusion Matrix: ")
    print(str(np.asarray([[tp,fp],[fn, tn]]))  + "\n")
    print("Recall: " + str(tp/(tp + fn)))
    print("Precision: " + str(tp/(tp + fp)))
    print("Significance: " + str(tp/(np.sqrt(tp+ fp))) +  "\n \n")


if __name__ == '__main__':
    main()