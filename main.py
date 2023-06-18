from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return 'form submitted!!'
# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route("/works.html")
# def works():
#     return render_template('works.html')


# @app.route("/contact.html")
# def works():
#     return render_template('contact.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')
