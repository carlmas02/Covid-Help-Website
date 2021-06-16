from flask import Flask,render_template,request,redirect,url_for
from program import *

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html'), 404


@app.route("/basicinfo")
def covid_info():
	return "Test info"

@app.route("/symptoms")
def symptoms():
	return render_template('symptoms.html')

@app.route("/cure")
def cure():
	return render_template('cure.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/virtualtest",methods =["GET","POST"])
def get_form():
	if request.method == "POST":
		name = request.form.get('name')
		age = request.form.get('age')
		fever = request.form.get('fever')
		cough = request.form.get('cough')
		fatigue = request.form.get('fatigue')
		bodypain = request.form.get('bodypain')
		appetite = request.form.get('appetite')
		resp = basic_symp(fever,cough,fatigue,bodypain,appetite)
		if resp :
			return redirect(url_for('run'))
		else:
			header = "Congratulations"
			text = "Your answers predict that you are at a low-risk for COVID-19 ,you must ensure you protect yourself and\
 ensure you are following social distancing norms. "
			return render_template('safe.html',text=text,header = header)

	return render_template('form.html')

@app.route("/virtualtest2",methods =["GET","POST"])
def run():
	if request.method == "POST":
		nose = request.form['nose']
		nausea = request.form['nausea']
		smell = request.form['smell']
		resp = mid_symptoms(nose,nausea,smell)
		if resp:
			return redirect(url_for('run2'))
		else:
			header = "Great"
			text = "Your answers predict that you at a medium to high risk for COVID-19 ,we suggest that you must get \
yourself tested. There are chances that you could be asymtomatic , so we prefer you to visit a doctor or  health-care \
             center "
			return render_template('safe.html',text= text,header=header)

	return render_template('form2.html')

@app.route("/virtualtest3",methods =["GET","POST"])
def run2():
	if request.method == "POST":
		chest = request.form['chest']
		breathing = request.form['breathing']
		resp = danger_symptoms(chest,breathing)
		if resp :
			return "true"
		else :
			return "false"
	return render_template("form3.html")





if __name__ == "__main__":
	app.run()


