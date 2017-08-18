from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/')
def route_list():

    return render_template('list.html')


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
