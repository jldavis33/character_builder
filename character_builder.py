from flask import Flask, render_template, redirect, url_for, request, make_response, flash
import json
from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'lkj;lkj;lkjaljks;ladksjf;lkajs;jkfa@#'


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    data = get_saved_data()
    return render_template('index.html', saves=data)


@app.route('/builder')
def builder():
    return render_template('builder.html',
                           saves=get_saved_data(),
                           options=DEFAULTS)


@app.route('/save', methods=['POST'])
def save():
    flash('Alright! That looks awesome!')
    data = get_saved_data()
    data.update(dict(request.form.items()))

    # fake a response so we can set a cookie
    # redirect to url for index()
    response = make_response(redirect(url_for('builder')))

    # set cookie in header convert dict to string
    response.set_cookie('character', json.dumps(data))
    return response


if __name__ == '__main__':

    app.run(debug=True, port=5000)
