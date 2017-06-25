from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "session1"

@app.route('/')
def index():
    session['gold'] = 0
    session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def gold():
    amt = 0
    if request.form['button'] == 'farm':
        amt = random.randrange(9,21)
    elif request.form['button'] == 'cave':
        amt = random.randrange(4,11)
    elif request.form['button'] == 'house':
        amt = random.randrange(1,6)
    elif request.form['button'] == 'casino':
        choice = random.randrange(0,3)
        amt = random.randrange(-1,51)
        if choice == 1:
            amt = -amt

    if amt >= 0:
        session['activities'].append("Earned "+str(amt)+" from the "+request.form['button']+"!")
    else:
        session['activities'].append("Walked into the Casino and lost "+str(amt)+", bummer....")
    session['gold'] += amt
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('gold')
    session.pop('activities')
    return redirect('/')

app.run(debug=True)
