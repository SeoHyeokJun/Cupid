from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/post')
def post():
   return render_template('post.html')

@app.route('/contact')
def contact():
   print("aa")
   return render_template('contact.html')

if __name__ == '__main__':
   app.run()