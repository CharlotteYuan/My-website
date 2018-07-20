from flask import Flask , render_template

app = Flask(__name__)#two underscorces

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/history')
def history():
	return render_template('history.html')

@app.route('/photo')
def photo():
	return render_template('photo.html')

@app.route('/comment')
def comment():
	return render_template('comment.html')

if __name__ == '__main__':
	app.run(debug = True)  