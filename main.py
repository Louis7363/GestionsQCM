from flask import Flask,session,flash, request, redirect, url_for, render_template
app = Flask(__name__)
import sqlite3

@app.route('/home', methods = ['GET' , 'POST'])
def home():
    return render_template('home.html')

@app.route('/ajoutQcm', methods = ['GET' , 'POST'])
def Qcm():
    return render_template('qcm.html')

@app.route('/ajoutReponse', methods = ['GET' , 'POST'])
def Reponse():
    return render_template('reponse.html')

app.run(debug=True)
