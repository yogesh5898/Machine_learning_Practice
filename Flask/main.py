from flask import Flask, render_template, request

""" Creating instance of first class 
Which is our WSGI - Web server gateway interface application"""

app = Flask(__name__)

""" which go to this path and run the below function"""


@app.route('/')
def welcome():
    return "Welcome to the best Flask course"


@app.route('/basic_html_content', methods=['GET'])
def surprise():
    return "<html><h1> This is My HTML tags content </h1></html>"


@app.route('/login_page', methods=['GET', 'POST'])
def templates():
    if request.method == 'POST':
        name = request.form['username']
        return f'Hello {name}!'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

"""debug=true if we set this we don't need to refresh every time when the changes made. Just update and save the change which
will automatically update in server too"""
