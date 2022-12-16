from flask import Flask, render_template 

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def index():
	return render_template("main.html")

@app.route('/verify', methods=["GET", "POST"])
def secondpagee():

	return render_template("secondpage.html")

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8085, ssl_context='adhoc')
