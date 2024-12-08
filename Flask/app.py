from flask import Flask

""" Creating instance of first class 
Which is our WSGI - Web server gateway interface application"""

app = Flask(__name__)

""" which go to this path and run the below function"""
@app.route('/')
def welcome():
    return "Welcome to the best Flask course"


@app.route('/special_page5898')
def surprise():
    return "This is the special page"

if __name__ == '__main__':
    app.run(debug=True)

"""debug=true if we set this we don't need to refresh every time when the changes made. Just update and save the change which
will automatically update in server too"""