from flask import Flask, render_template, request, redirect, url_for

""" Creating instance of first class 
Which is our WSGI - Web server gateway interface application"""

app = Flask(__name__)

""" which go to this path and run the below function"""


@app.route('/')
def welcome():
    return "Welcome to the best Flask course"


@app.route('/login_page', methods=['GET', 'POST'])
def templates():
    if request.method == 'POST':
        name = request.form['username']
        return f'Hello {name}!'
    return render_template('index.html')


""" Variable rule """
@app.route('/success/<float:score>')
def success(score):
    res=""
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'
    return render_template('result.html', results=res)


@app.route('/success_result/<float:score>')
def success_result(score):
    res = ""
    if score >= 60:
        res = "Passed"
    else:
        res = "Failed"

    exp = {
        'score' : score,
        'res' : res
    }
    # return render_template('success_results.html', score=score, res=res)
    return render_template('success_results.html', **exp)


@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_Science = float(request.form['data_Science'])

        total_score = (science + maths + c + data_Science)/4
    else:
        return render_template('getresults.html')
    return redirect(url_for('success_result', score=total_score))


if __name__ == '__main__':
    app.run(debug=True)

"""debug=true if we set this we don't need to refresh every time when the changes made. Just update and save the change which
will automatically update in server too"""
