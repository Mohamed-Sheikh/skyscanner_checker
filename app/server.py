from flask import Flask, render_template, request
import os

"""Main application file"""
app = Flask(__name__)
curr_dir = os.getcwd()

@app.route('/')
def index():
    file_name = 'index.html'
    return render_template(file_name)

"""When routed, will display results of ticket prices"""
@app.route('/results')
def results():
    pass

"""Main entry point for application"""
def main():
    app.run(debug=True)

main()

