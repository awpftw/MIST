from flask import Flask, render_template, request, url_for, flash
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, BooleanField, validators

class WeanForm(FlaskForm):
	valve1 = BooleanField()
	valve2 = BooleanField()
	minutes = IntegerField('Minutes', [validators.NumberRange(min=1, max=60)])
	seconds = IntegerField('Seconds', [validators.NumberRange(min=1, max=60)])
	submit = SubmitField("Start")

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/mist')
def mist():
	return render_template('mist.html')

@app.route('/wean', methods=['GET', 'POST'])
def wean():
	valve1 = None
	valve2 = None
	minutes = None
	seconds = None
	text = None
	error = None
	successCheck = False

	form = WeanForm()

	if form.validate() == False:
		return render_template('wean.html', form = form)
	else:
		valve1 = form.valve1.data
		valve2 = form.valve2.data
		minutes = form.minutes.data
		seconds = form.seconds.data

		if valve1 == True and valve2 == False:
			text = "1"
			successCheck = True
		elif valve1 == False and valve2 == True:
			text = "2"
			successCheck = True
		else:
			error = 'Check valves, something is wrong!'

	return render_template('wean.html', error=error, form=form, text=text, valve1=valve1, valve2=valve2, minutes=minutes, seconds=seconds, successCheck=successCheck)