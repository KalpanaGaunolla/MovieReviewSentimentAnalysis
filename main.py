from flask import Flask, render_template, request
import pickle

# Load the Naive Bayes model and TfidfVectorizer object from disk
filename = 'Movie.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('CountVectorizer.pkl','rb'))
app = Flask(__name__)


@app.route('/')


def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    message = request.form['review']
    data = [message]
    vect = cv.transform(data).toarray()
    my_prediction = classifier.predict(vect)

    if my_prediction==[1]:
        result="Thank you for the Positive Review!"
    elif my_prediction==[0]:
        result="Oops!! It's a negative review!"

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
	app.run(debug=True)
