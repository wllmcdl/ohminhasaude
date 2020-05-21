from flask import Flask, render_template

from Female import Female
from Male import Male

app = Flask(__name__)


# We use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Butler')


if __name__ == '__main__':
    app.run(debug=True)
