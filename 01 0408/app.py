from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    data = {
        'name': 'ZININ',
        'age': 20,
        'city': 'Malaysia'
    }


    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()
