from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
def index():
	return render_template('index.html')


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




if __name__ == "__main__":
	app.run()


