from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    handle = open('log.csv')
    reader = csv.reader(handle)
    datetime = reader.__next__()[1]
    header = reader.__next__()
    return render_template('index.html', reader=reader, datetime=datetime,
                           header=header)


if __name__ == '__main__':
    app.run(debug=True)
