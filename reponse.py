#!/usr/bin/python3
import cgi
import cgitb
from logging import raiseExceptions

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue("montant"):
    montant = form.getvalue("montant")
    print(montant)
else:
    raiseExceptions("Pas de montant")

print("Content-type: text/html; charset=utf-8\n")

html = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="Definition_projet.css" type="text/css" />

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script type="text/javascript" src="./Definition_projet.js"></script>
    <title>Navbar</title>
</head>
<body>
    <nav class="navbar">
        <div class="navbar-container">
            <input type="checkbox" name="" id="">
            <div class="hamburger-lines">
                <span class="line line1"></span>
                <span class="line line2"></span>
                <span class="line line3"></span>
            </div>
            <ul class="menu-items">
                <li><a href="Accueil.html">Accueil</a></li>
                <li><a href="Definition_projet.html">Definition du projet</a></li>
                <li><a href="Les_strategies.html">Les stratégies</a></li>
            </ul>
            <a href="Accueil.html"><img src="./images/Logo_portfoladvice.png" alt="" align="top"/></a>
        </div>
    </nav>
    <div class="container">
        <div class="wrapper">
          <ul class="steps">
            <li class="is-active">Etape 1</li>
            <li>Etape 2</li>
            <li>Etape 3</li>
          </ul>
          <form class="form-wrapper" action="reponse.py" method="post">
            <fieldset class="section is-active">
              <h3>Montant à investir</h3>
              <input type="text" name="Montant" id="montant" placeholder="Montant en euro">
              <div class="button" type="button">Suivant</div>
            </fieldset>
            <fieldset class="section">
              <h3>Risque</h3>
              <div class="row cf">
                <div class="four col">
                  <input type="radio" name="r1" id="faible" checked>
                  <label for="r1">
                    <h4>Faible</h4>
                  </label>
                </div>
                <div class="four col">
                  <input type="radio" name="r1" id="modere"><label for="modere">
                    <h4>Modéré</h4>
                  </label>
                </div>
                <div class="four col">
                  <input type="radio" name="r1" id="haut"><label for="haut">
                    <h4>Haut</h4>
                  </label>
                </div>
              </div>
              <div class="button" type="button">Suivant</div>
            </fieldset>
            <fieldset class="section 2">
              <h3>Durée d'investissent</h3>
                <div class="row cf">  
                  <div class="four col">
                    <input type="radio" name="r2" id="court" checked>
                    <label for="r1">
                      <h4>Court terme</h4>
                    </label>
                  </div>
                  <div class="four col">
                    <input type="radio" name="r2" id="moyen"><label for="moyen">
                      <h4>Moyen terme</h4>
                    </label>
                  </div>
                  <div class="four col">
                    <input type="radio" name="r2" id="long"><label for="long">
                      <h4>Long terme</h4>
                    </label>
                  </div>
                </div>
                <div class="button" type="submit">Suivant</div>
              </fieldset>
            <fieldset class="section">
              <h3>Account Created!</h3>
              <p>Your account has now been created.</p>
              <div class="button">Reset Form</div>
            </fieldset>
          </form>
        </div>
      </div>
</body>
</html>
"""
print(html)
