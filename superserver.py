from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)


def csv_reader(file_name):
    with open(file_name, "r") as csv_file:
        text = csv.reader(csv_file)
        text_list = list(text)
        return text_list


@app.route('/')
@app.route('/list')
def route_index():
    text_list = csv_reader("data.csv")
    return render_template('list.html', text_list=text_list)


@app.route('/story')
def route_story():
    text_list = csv_reader("data.csv")
    user_id = 0
    for i in range(len(text_list)):
        if text_list[i][0]:
            user_id = int(text_list[i][0]) + 1
    print(user_id)
    return render_template('form.html', user_id=user_id)


@app.route('/save-story', methods=['POST'])
def route_save():
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


@app.route('/story/<id>')
def route_story_id(id=None):
    user_id = id
    edit = True
    text_list = csv_reader("data.csv")
    new_text_list = text_list[int(id)]
    return render_template('form.html', user_id=user_id, edit=edit, new_text_list=new_text_list)

@app.route('/edit-story/<id>', methods=['POST'])
def route_edit_story(id=None):
    text_list = csv_reader("data.csv")
    if request.method == 'POST':
        title = request.form['title']
        story = request.form['story']
        criteria = request.form['criteria']
        value = request.form['value']
        estimation = request.form['estimation']
        status = request.form['status']
        user_id = request.form.get("user_id")
        user_id = int(user_id)
        text_list[user_id] = [user_id, title, story, criteria, value, estimation, status]
        with open("data.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(text_list)
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = 'abcdef'
    app.run(debug=True, port=5000)
