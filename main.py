from flask import Flask,session,flash, request, redirect, url_for, render_template
app = Flask(__name__)
import sqlite3

@app.route('/', methods = ['GET' , 'POST'])
def home():
    return render_template('home.html')

@app.route('/creationQcm', methods = ['GET' , 'POST'])
def Qcm():
    return render_template('qcm.html')

@app.route('/ajoutQcm', methods = ['GET' , 'POST'])
def ajoutQcm():
    form = request.form
    nomQcm = form["nomQcm"]
    nombreQuestions = int(form["nombreQuestions"])
    print(nomQcm,nombreQuestions)
    inputs=""
    for i in range (nombreQuestions) :
        inputs += f"<input type='text' placeholder='Entrez la réponse de la question {i+1}'>"
        print(i,inputs)
    print(inputs)
    return render_template('bonnesReponses.html',inputs=inputs)

@app.route('/ajoutReponse', methods = ['GET' , 'POST'])
def Reponse():
    return render_template('reponse.html')

app.run(debug=True)