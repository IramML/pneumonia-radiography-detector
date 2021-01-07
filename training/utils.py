import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets as tfds

class Utils:
    def __init__(self):
        super().__init__()

    def create_nn_model(self):
        model = keras.Sequential()
        model.add(layers.Flatten(input_shape=(512, 512)))
        model.add(layers.BatchNormalization())
        model.add(layers.Dense(512, activation=tf.nn.relu))
        model.add(layers.Dense(256, activation=tf.nn.relu))
        model.add(layers.Dense(128, activation=tf.nn.relu))
        model.add(layers.BatchNormalization())
        model.add(layers.Dense(3, activation=tf.nn.softmax))

        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def create_images_dataframe(self, images_path, tag):
        items = [];
        
        for image_path in images_path:
            image = keras.preprocessing.image.load_img(
                image_path, color_mode='grayscale', target_size=(512, 512),
                interpolation='nearest'
            )

            image = keras.preprocessing.image.img_to_array(image)
            image = np.reshape(image, (512, 512))
            item = [(image, tag)]
            items = items + item

        return items