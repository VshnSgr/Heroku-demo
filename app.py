from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import pickle

# load the model from disk
filename = 'nlp_model.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('tranform.pkl','rb'))
app = Flask(__name__)
#tab1  = pd.read_csv("cement.csv")
#tab1.to_html('templates\\result2.html',index=False,col_space=40)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():


	# if request.method == 'POST':
	# 	message = request.form['message']
	# 	data = [message]
	# 	vect = cv.transform(data).toarray()
	# 	my_prediction = clf.predict(vect)
	message = request.form['message']
	df1 =pd.read_csv(message)
	df1.to_html('templates\\result2.html', index=False, col_space=40)
	#return render_template('result2.html',prediction = my_prediction)
	return render_template('result2.html')



if __name__ == '__main__':
	app.run(debug=True)