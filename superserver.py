from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)


def csv_reader(file_name):
    with open(file_name, "r") as csv_file:
        text = csv.reader(csv_file)
        text_list = list(text)
        return text_list


@app.route('/')
def route_index():
    text_list = csv_reader("data.csv")
    if text_list:
        user_id = text_list[0][0]
    else:
        user_id = 0
    
    return render_template('list.html', text_list=text_list)


@app.route('/list')
def route_list():
    return route_index()


@app.route('/story')
def route_form():
    user_id = None
    if user_id == None:
        user_id = 1
    else:
        user_id += 1
    return render_template('form.html', user_id=user_id)


@app.route('/save-story', methods=['POST'])
def route_save():
    print('POST request received!')
    if request.method == 'POST':
        title = request.form['title']
        story = request.form['story']
        criteria = request.form['criteria']
        value = request.form['value']
        estimation = request.form['estimation']
        status = request.form['status']
        user_id = request.form.get("user_id")
        fieldnames = ['user_id', 'title', 'story', 'criteria', 'value', 'estimation', 'status']
        with open("data.csv", "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({
                'user_id': user_id, 'title': title, 'story': story,
                'criteria': criteria, 'value': value, 'estimation': estimation,
                'status': status})
    return redirect('/')



if __name__ == "__main__":
    app.secret_key = 'abcdef'
    app.run(debug=True, port=5000)
