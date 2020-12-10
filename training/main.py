import numpy as np
import os
import PIL
import PIL.Image
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import pathlib
import random
import sys
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib'))
from utils import Utils
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'



if __name__ == "__main__":
    utils = Utils()
    project_path = os.path.dirname(os.path.realpath(__file__))

    dataset_folder_path = project_path + "/in/images-dataset"

    normal_dataset_name = "NORMAL"
    pneumonia_dataset_name = "Viral Pneumonia"

    nn_model = utils.create_nn_model()

    data_dir = pathlib.Path(dataset_folder_path)

    normal_images_paths = list(data_dir.glob(normal_dataset_name + '/*'))
    pneumonia_images_paths = list(data_dir.glob(pneumonia_dataset_name + '/*'))

    normal_dataset = utils.create_images_dataframe(normal_images_paths, 0)
    pneumonia_dataset = utils.create_images_dataframe(pneumonia_images_paths, 1)

    complete_dataset = normal_dataset + pneumonia_dataset
    random.shuffle(complete_dataset)

    X = [i[0] for i in complete_dataset]
    y = [i[1] for i in complete_dataset]

    X_train, X_test, y_train, y_test = X[:1405], X[1405:], y[:1405], y[1405:]

    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)
    y_train = np.asarray(y_train)
    y_test = np.asarray(y_test)

    nn_model.fit(X_train, y_train, epochs=20)

    test_loss, test_acc = nn_model.evaluate(X_test, y_test)
    print("Accuracy: ", test_acc)

    nn_model.save(project_path + "/out")