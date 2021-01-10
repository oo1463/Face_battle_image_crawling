import numpy as np
import matplotlib.pyplot as plt
import tarfile
import tensorflow as tf
import os
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dense, Flatten, Dropout, BatchNormalization, Activation
from sklearn.model_selection import train_test_split


def load_images():
    images = np.load('./image_save.npy')
    return images


def load_tag_data():
    tag_data = np.load('./image_tag_save.npy')
    return tag_data


def start_learning():
    images = load_images()
    tag_data = load_tag_data()
    rand = 100
    X_train, X_test, Y_train, Y_test = train_test_split(images, tag_data, test_size=0.3, random_state=rand)

    print(X_train , X_test, Y_train, Y_test)


if __name__ == "__main__":
    start_learning()