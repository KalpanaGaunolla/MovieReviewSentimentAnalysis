# Movie Review Sentiment Analysis

In this project, I have created an end-to-end project on the sentiment analysis based on Movie reviews as a proof of concept. The main objective is to predict weather the review is positive or negative with the help of Natural Language Process and Machine Learning. Created API using Flask framework and deployed it on Google Cloud Platform.

## Website link
https://movie-review-234.el.r.appspot.com/

## Demo
![Demo video](https://user-images.githubusercontent.com/81810275/132949830-e7d271a4-fb30-480c-a657-94f752f66799.gif)

## Technical aspect
* Python 3.9
* Front-end: HTML, CSS
* Back-end: Flask
* IDE: Jupyter Notebook, PyCharm
* Deployment: Google Cloud Platform

## How to run this app
Code is written in Python 3.9. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.
* Create virtual environment - *conda create -n myenv python=3.9*
*	Activate the environment - *conda activate myenv*
* Install the packages - *pip install -r requirements.txt*
* Run the app - *python main.py*

## Workflow

### Data Collection
The dataset is used for this project is IMDB dataset

### Data Pre-processing
* Removed all the special characters
* Converted everything into lowercase
* Removed stop words
* Applied lemmatization
* Created Bag of words
* Performed Label encoding on target feature

### Model Creation and Evaluation
* Multinomial Naïve Bayes classifier is applied to train and test the model.
* Model performance evaluated based on accuracy, confusion matrix, classification report.

### Model Deployment
* The model is deployed on Google Cloud Platform using Flask framework







