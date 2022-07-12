#!/usr/bin/python
from crypt import methods
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("Accueil.html")

@app.route("/traitement", methods= ["POST", "GET"])
def traitement():
    if request.method == "POST":
        data = request.form
        montant = int(data.get('montant'))
        risque = data.get('r1')
        duree = data.get('r2')
        int_montant = int(montant)
        print(duree)
        print(risque)
        print(montant)
        print(data)
        if int_montant > 0:
            return render_template("traitement.html", investissement=montant)
        return "traitement de données"
    else:
        return redirect(url_for('accueil'))

@app.route("/Definition_projet")
def Definition_projet():
    return render_template("Definition_projet.html")

@app.route("/Les_strategies")
def Les_strategies():
    return render_template("Les_strategies.html")

if __name__ == '__main__':
    app.run(debug=True)
