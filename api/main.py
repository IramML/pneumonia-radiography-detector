from tensorflow import keras
from PIL import Image, ImageOps
import os
import numpy as np
from flask import request, jsonify
from app import create_app


app = create_app()

@app.route("/api/predict", methods=['POST'])
def home():
    image = request.files.get("image")
    image = Image.open(image.stream).convert('LA')
    image = image.resize((512,512), Image.ANTIALIAS)
    image = ImageOps.grayscale(image)
    image = keras.preprocessing.image.img_to_array(image)
    image = np.reshape(image, (512, 512))

    project_path = os.path.dirname(os.path.realpath(__file__))
    nn_model = keras.models.load_model(project_path + "/model" )

    predict = nn_model.predict(np.array([image]))
    str_prediction = "Normal" if predict[0] < 0.5 else "Pneumonia"
    return jsonify(
        code = 200,
        message = "Request successfully",
        prediction = str_prediction
    )