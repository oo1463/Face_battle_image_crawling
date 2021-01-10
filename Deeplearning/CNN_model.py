import numpy as np
import matplotlib.pyplot as plt
import os
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dense, Flatten, Dropout, BatchNormalization, Activation
from sklearn.model_selection import train_test_split
# from keras.layers.experimental.preprocessing import Rescaling
from keras.utils import to_categorical

def plot_loss_curve(history):

    import matplotlib.pyplot as plt

    plt.figure(figsize=(15, 10))

    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper right')
    plt.show()


def load_images():
    images = np.load('./image_save.npy')
    return images


def load_tag_data():
    tag_data = np.load('./image_tag_save.npy')
    return tag_data


def ont_hot_incoding(y_train, y_test):
    y_train = to_categorical(y_train, 101)
    y_test = to_categorical(y_test, 101)

    return y_train, y_test


def create_model():
    model = Sequential([

        Conv2D(filters=10, kernel_size=(3, 3), input_shape=(96, 96, 3)),
        BatchNormalization(),
        Activation('relu'),

        # Conv2D(filters=10, kernel_size=(3, 3)),
        # BatchNormalization(),
        # Activation('relu'),
        MaxPooling2D(pool_size=(3, 3)),

        # Conv2D(filters=20, kernel_size=(3, 3)),
        # BatchNormalization(),
        # Activation('relu'),
        #
        # Conv2D(filters=20, kernel_size=(3, 3)),
        # BatchNormalization(),
        # Activation('relu'),
        # MaxPooling2D(pool_size=(3, 3)),
        # Dropout(0.3),
        #
        # Conv2D(filters=30, kernel_size=(3, 3)),
        # BatchNormalization(),
        # Activation('relu'),
        #
        # Conv2D(filters=30, kernel_size=(3, 3)),
        # BatchNormalization(),
        # Activation('relu'),
        # MaxPooling2D(pool_size=(3, 3)),
        # Dropout(0.3),
        Dropout(0.2),
        # Dense(50, activation='relu'),
        Flatten(),
        Dense(units=101, activation='softmax')
    ])

    model.compile(optimizer='Adam', loss='mse', metrics=['accuracy'])

    return model


def start_learning():
    images = load_images()
    tag_data = load_tag_data()
    rand = 100
    X_train, X_test, Y_train, Y_test = train_test_split(images, tag_data, test_size=0.3, random_state=rand)

    # print(X_train , X_test, Y_train, Y_test)

    # print(X_test.shape)
    Y_train, Y_test = ont_hot_incoding(Y_train, Y_test)

    model = create_model()
    model.summary()

    history = model.fit(X_train, Y_train, validation_data=(X_test, Y_test), batch_size=32, epochs=10)

    plot_loss_curve(history.history)
    print(history.history)


if __name__ == "__main__":
    start_learning()

