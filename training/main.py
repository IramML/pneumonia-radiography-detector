import numpy as np
import os
import PIL
import PIL.Image
import pathlib
import random
import sys
from utils import Utils

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib'))

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

if __name__ == "__main__":
    utils = Utils()
    project_path = os.path.dirname(os.path.realpath(__file__))

    dataset_folder_path = project_path + "/in/images-dataset"

    normal_dataset_name = "NORMAL"
    pneumonia_dataset_name = "Viral Pneumonia"
    covid_dataset_name = "COVID"

    nn_model = utils.create_nn_model()

    data_dir = pathlib.Path(dataset_folder_path)

    normal_images_paths = list(data_dir.glob(normal_dataset_name + '/*'))
    pneumonia_images_paths = list(data_dir.glob(pneumonia_dataset_name + '/*'))
    covid_images_paths = list(data_dir.glob(covid_dataset_name + '/*'))

    normal_dataset = utils.create_images_dataframe(normal_images_paths, 0)
    pneumonia_dataset = utils.create_images_dataframe(pneumonia_images_paths, 1)
    covid_dataset = utils.create_images_dataframe(covid_images_paths, 2)

    complete_dataset = normal_dataset + pneumonia_dataset + covid_dataset
    random.shuffle(complete_dataset)

    X = [i[0] for i in complete_dataset] 
    y = [i[1] for i in complete_dataset] 

    train_80_percent = round(len(X) * 0.8)

    X_train, X_test, y_train, y_test = X[:train_80_percent], X[train_80_percent:], y[:train_80_percent], y[train_80_percent:]

    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)
    y_train = np.asarray(y_train)
    y_test = np.asarray(y_test)

    nn_model.fit(X_train, y_train, epochs=16)

    test_loss, test_acc = nn_model.evaluate(X_test, y_test)
    print("Accuracy: ", test_acc)

    nn_model.save(project_path + "/out")