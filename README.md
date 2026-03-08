# Handwritten Digit Recognition Dashboard using Taipy

## Project Overview

This project is an interactive web application that recognizes handwritten digits using Machine Learning.
The application allows users to upload an image of a handwritten digit and predicts the corresponding number.

The graphical user interface is built using **Taipy**, while the machine learning model is trained using the **Scikit-learn** library on the **MNIST handwritten digits dataset**.

This project demonstrates how machine learning models can be integrated with an interactive dashboard for real-time predictions.

---

## Problem Statement

Handwritten digit recognition is a classical problem in machine learning and pattern recognition. Humans can easily identify handwritten numbers, but computers require algorithms to analyze and classify them.

The goal of this project is to build a system that:

* Accepts a handwritten digit image from the user
* Processes the image
* Uses a trained machine learning model to predict the digit
* Displays the result in an interactive dashboard

---

## Objectives

* Demonstrate pattern recognition using machine learning
* Build an interactive dashboard using Taipy
* Integrate machine learning models with a user interface
* Provide real-time predictions for handwritten digits

---

## Technologies Used

* Python
* Taipy (GUI Framework)
* Scikit-learn (Machine Learning)
* NumPy (Numerical Computing)
* Pandas (Data Handling)
* Pillow (Image Processing)

---

## Project Structure

```
digit-recognition-taipy/
│
├── app.py               # Main Taipy GUI application
├── train_model.py       # Script to train the ML model
├── digit_model.pkl      # Saved trained model
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## Installation

### Step 1: Clone the repository or download the project

```
git clone <repository-url>
```

or download the folder manually.

### Step 2: Install required dependencies

```
pip install -r requirements.txt
```

---

## Training the Model

Run the following command to train the machine learning model:

```
python train_model.py
```

This will generate the file:

```
digit_model.pkl
```

which contains the trained model.

---

## Running the Application

Run the Taipy application using:

```
python app.py
```

After running the command, a web interface will open in your browser.

---

## How to Use

1. Open the application in the browser.
2. Upload an image containing a handwritten digit.
3. Click the **Predict** button.
4. The system will analyze the image and display the predicted digit.

---

## Applications

Handwritten digit recognition has several real-world applications, including:

* Postal code recognition
* Bank cheque processing
* Automatic form digitization
* Document analysis systems

---

## Future Improvements

Possible improvements to the project include:

* Adding a drawing canvas for users to draw digits directly
* Using deep learning models for higher accuracy
* Adding prediction confidence scores
* Improving GUI design and visualization

---

## Author

Kumar Gaurav
B.Tech Computer Science and Engineering
National Institute of Technology Agartala

---

## License

This project is created for educational purposes.
# Handwritten Digit Recognition Dashboard using Taipy

## Project Overview

This project is an interactive web application that recognizes handwritten digits using Machine Learning.
The application allows users to upload an image of a handwritten digit and predicts the corresponding number.

The graphical user interface is built using **Taipy**, while the machine learning model is trained using the **Scikit-learn** library on the **MNIST handwritten digits dataset**.

This project demonstrates how machine learning models can be integrated with an interactive dashboard for real-time predictions.

---

## Problem Statement

Handwritten digit recognition is a classical problem in machine learning and pattern recognition. Humans can easily identify handwritten numbers, but computers require algorithms to analyze and classify them.

The goal of this project is to build a system that:

* Accepts a handwritten digit image from the user
* Processes the image
* Uses a trained machine learning model to predict the digit
* Displays the result in an interactive dashboard

---

## Objectives

* Demonstrate pattern recognition using machine learning
* Build an interactive dashboard using Taipy
* Integrate machine learning models with a user interface
* Provide real-time predictions for handwritten digits

---

## Technologies Used

* Python
* Taipy (GUI Framework)
* Scikit-learn (Machine Learning)
* NumPy (Numerical Computing)
* Pandas (Data Handling)
* Pillow (Image Processing)

---

## Project Structure

```
digit-recognition-taipy/
│
├── app.py               # Main Taipy GUI application
├── train_model.py       # Script to train the ML model
├── digit_model.pkl      # Saved trained model
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## Installation

### Step 1: Clone the repository or download the project

```
git clone <repository-url>
```

or download the folder manually.

### Step 2: Install required dependencies

```
pip install -r requirements.txt
```

---

## Training the Model

Run the following command to train the machine learning model:

```
python train_model.py
```

This will generate the file:

```
digit_model.pkl
```

which contains the trained model.

---

## Running the Application

Run the Taipy application using:

```
python app.py
```

After running the command, a web interface will open in your browser.

---

## How to Use

1. Open the application in the browser.
2. Upload an image containing a handwritten digit.
3. Click the **Predict** button.
4. The system will analyze the image and display the predicted digit.

---

## Applications

Handwritten digit recognition has several real-world applications, including:

* Postal code recognition
* Bank cheque processing
* Automatic form digitization
* Document analysis systems

---

## Future Improvements

Possible improvements to the project include:

* Adding a drawing canvas for users to draw digits directly
* Using deep learning models for higher accuracy
* Adding prediction confidence scores
* Improving GUI design and visualization

---

## Author

Kumar Gaurav
B.Tech Computer Science and Engineering
National Institute of Technology Agartala

---

## License

This project is created for educational purposes.
