from taipy.gui import Gui
import pickle
import numpy as np
from PIL import Image

model = pickle.load(open("digit_model.pkl", "rb"))

prediction = "Upload an image"

def predict_digit(state):
    try:
        img = Image.open(state.image_path).convert("L")
        img = img.resize((8,8))

        img = np.array(img)
        img = img / 16.0
        img = img.flatten().reshape(1,-1)

        pred = model.predict(img)

        state.prediction = "Predicted Digit: " + str(pred[0])

    except Exception as e:
        state.prediction = "Error: " + str(e)

page = """
# Handwritten Digit Recognition

Upload an image of a handwritten digit.

<|{image_path}|file_selector|>

## Uploaded Image

<|{image_path}|image|>

<|Predict|button|on_action=predict_digit|>

## Result

<|{prediction}|text|>
"""

Gui(page).run()