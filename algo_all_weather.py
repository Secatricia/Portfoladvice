#!/usr/bin/python
from crypt import methods
from operator import index
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

"""File to make the distribution of the user's budget according to the distribution by ETF"""


def algo(montant):
    tab_value = []
    tab_repart = []
    tab_nb_etf = []
    tab_nb_euro = []
    montant_utilisateur = montant
    montant_total = 0
    m_t_etf = 0  # montant total des etf qui composent le portefeuille
    # percent=  pourcentage de repartition par etf
    total_min = 0  # total minimum autorisé pour ce portefeuille
    value = 'value.get'
    index = 0

    paramMysql = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Lucie.D1410',
        'database': 'Portfoladvice_data'
    }

    conn = mysql.connector.connect(**paramMysql)
    cur = conn.cursor()
    cur.execute("SELECT value FROM All_weather_info")
    data_aw = cur.fetchall()
    for item in data_aw:
        tab_value.append(item[0])

    cur.execute("SELECT repartition FROM All_weather_info")
    data_aw = cur.fetchall()
    for per in data_aw:
        tab_repart.append(per[0])

    m_t_etf = montant_total_etf(tab_value)
    total_min = montant_minimum(tab_repart, tab_value)

    if montant_utilisateur > m_t_etf and montant_utilisateur > total_min:

        while index != len(tab_repart):

            if tab_value[index] < (tab_repart[index]*montant_utilisateur)/100:
                    # Is the amount of the etf according to the repartition
                    # possible according to the amount that the user has given
                nb, nb_euro = nb_etf(tab_value[index], tab_repart[index], montant_utilisateur)
                tab_nb_etf.append(nb)
                tab_nb_euro.append(nb_euro)
                
            else:
                return ('Montant insuffisant', tab_nb_etf, tab_nb_euro)
            index += 1

        # print(tab_nb_euro)
            
        tab_nb_euro, tab_nb_etf = montant_final(tab_nb_euro, tab_nb_etf, montant_utilisateur, tab_repart, tab_value)
        # print(tab_nb_euro)
        for i in tab_nb_euro:
            montant_total += i
        

    else:
        return ('Montant insuffisant', tab_nb_etf, tab_nb_euro)

    # print(tab_value)
    # print(tab_nb_etf)
    return(montant_total, tab_nb_etf, tab_nb_euro)


def montant_total_etf(tab_value):
    total = 0

    for value in tab_value:
        total += value
    return total


def montant_minimum(tab_repart, tab_value):

    total_min = 0
    index = 0

    while index != len(tab_repart):

        if ((100 * tab_value[index]) / tab_repart[index]) > total_min:
            total_min = (100 * tab_value[index]) / tab_repart[index]
        index += 1
    return total_min

def nb_etf(etf_value, percent, montant_utilisateur):
    max = percent*montant_utilisateur/100
    nb = 0

    while max > etf_value:
        max -= etf_value
        nb += 1
    nb_euro = nb * etf_value
    return nb, nb_euro

def montant_final(tab_nb_euro, tab_nb_etf, montant_utilisateur, tab_repart, tab_value):
    montant_total = 0
    for i in tab_nb_euro:
        montant_total += i
       
    for index in range(len(tab_value)):
        if (tab_repart[index] - 1) > tab_nb_euro[index]*100/montant_utilisateur:
            if montant_utilisateur - tab_value[index] > 0:
                tab_nb_euro[index] += tab_value[index]
                tab_nb_etf[index] += 1
        index += 1
    
    return tab_nb_euro, tab_nb_etf
