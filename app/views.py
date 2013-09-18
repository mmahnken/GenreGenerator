from flask import render_template, request
from app import app
from forms import UrlForm
import genre
from genre import getInfoBox

@app.route('/')
@app.route('/index')
def index():
	form = UrlForm()
	return render_template("index.html", form = form)	


@app.route('/getting', methods = ['GET', 'POST'])
def getting():
	urls= []
	#Get first url.
	url = request.form['url']
	urls.append(url)
	#Get additional urls.
	num_urls = len(request.form) - 1
	for num in range(2, num_urls+1):
		url = request.form['url-' + str(num)]
		urls.append(url)
	resp = {}
	for u in urls:
		r = getInfoBox(u)
		resp[u]=r 
	return render_template('results.html', resp = resp)
