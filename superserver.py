from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)


def csv_reader(csv):
    with open(csv, mode='r') as csv_file:
        text = csv.reader(csv_file)
        text_list = list(text)
        return text_list

@app.route('/')
def route_list():
    text_list = csv_reader("data.csv")
    return render_template('list.html', text_list=text_list)


@app.route('/story')
def route_form():
    if request.method == 'POST':
        user_title = request.form('title')
        user_story = request.args.get('story')
        acc_criteria = request.args.get('criteria')
        business_value = request.form('value')
        user_title = request.form('title')
        user_estimation = request.form('estimation')
    return render_template('form.html')


if __name__ == "__main__":
    app.secret_key = 'abcdef'
    app.run(debug=True, port=5000)
