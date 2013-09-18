from flask.ext.wtf import Form, TextField, TextAreaField, BooleanField, Required, SelectField, IntegerField, DateTimeField

class UrlForm(Form):
	url = TextField('id')

	

