from flask import Flask, render_template, url_for, request
import pickle
import pandas as pd
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import boomer

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/addinfo', methods=['POST'])
def addinfo():
    clientz = boomer.Snail()
    clientz.conx()
    readr = clientz.read_em()
    return render_template('readerz.html', readr=readr)


@app.route('/predict', methods=['POST'])
def predict():
    df = pd.read_csv("spam.csv", encoding="latin-1")
    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    # Features and Labels
    df['label'] = df['class'].map({'ham': 0, 'spam': 1})
    X = df['message']
    y = df['label']

    # Extract Feature With CountVectorizer
    cv = CountVectorizer()
    X = cv.fit_transform(X)  # Fit the Data

    #train data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # Naive Bayes Classifier
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))
    print(clf.score(X_train,y_train))
    sss = ("input a string to check if it is a phishing email: ")
    sss = [sss]
    vects = cv.transform(sss).toarray()
    my_predictionzz = clf.predict(vects)
    #devnull='BC9JRhHDadNGQVa'
    if my_predictionzz == 1:
        print("spam")
        message_content="spam", sss
        with open("spam.csv",'a+') as spmsg:
            addit = csv.writer(spmsg)
            addit.writerow(message_content)
    

    elif my_predictionzz == 0:
        print("ham")

    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)

    return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
	# Set host to 0.0.0.0 ("the internet" for connectivity through VMware NAT to the host machine's browser. 
	#Debug =True for output to the console
    app.run(host="0.0.0.0", debug=False)
