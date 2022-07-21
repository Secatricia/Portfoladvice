#!/usr/bin/python
from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import algo_all_weather


app = Flask(__name__)


@app.route("/")
def accueil():
    return render_template("Accueil.html")


@app.route("/traitement", methods=["POST", "GET"])
def traitement():
    if request.method == "POST":
        paramMysql = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Lucie.D1410',
            'database': 'Portfoladvice_data'
        }

        conn = mysql.connector.connect(**paramMysql)
        cur = conn.cursor()
        cur.execute("SELECT * FROM All_weather_info")
        data_aw = cur.fetchall();
        for item in data_aw:
            print(item)

        data = request.form
        montant = int(data.get('montant'))
        risque = data.get('r1')
        duree = data.get('r2')
        int_montant = int(montant)
        montant_total = 'montant'
        tab_nb_etf = []
        tab_nb_euro = []
        i = 0
        j = 0
        # print(duree)
        # print(risque)
        # print(montant)
        # print(data)
        if int_montant > 0:
            if risque == 'faible':
                if duree == 'long':
                    montant_total, tab_nb_etf, tab_nb_euro = algo_all_weather.algo(montant)
                    print(montant_total)
                    # print(tab_nb_etf)
                    # print(tab_nb_euro)
                    if montant_total != 'Montant insuffisant':
                        return render_template("traitement.html", investissement=montant, donnee=data_aw, total=montant_total, list_nb=tab_nb_etf, list_euro=tab_nb_euro, index=i, nb=j)
                    else:
                        return render_template("Error_montant_insuffisant.html")
            if risque == 'modere':
                if duree == 'long':
                    montant_total, tab_nb_etf, tab_nb_euro = algo_all_weather.algo(montant)
                    # print(montant_total)
                    # print(tab_nb_etf)
                    # print(tab_nb_euro)
                    if montant_total != 'Montant insuffisant':
                        return render_template("traitement.html", investissement=montant, donnee=data_aw)
                    else:
                        return render_template("Error_montant_insuffisant.html")
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
