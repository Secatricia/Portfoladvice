# coding:utf-8
import time
from http.server import HTTPServer
from server import Server
import cgi
import cgitb
from logging import raiseExceptions

if __name__ == '__main__':

    HOST_NAME = 'localhost'
    PORT_NUMBER = 8888

    if __name__ == '__main__':
        httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
        print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))

        cgitb.enable()
        form = cgi.FieldStorage()

        if form.getvalue("montant"):
            montant = form.getvalue("montant")
            print(montant)
        else:
            raise Exception("Pas de montant")

        print("Content-type: text/html; charset=utf-8\n")

        html = """<!DOCTYPE html>
  <head>
      <meta charset="UTF-8">
    <title>Page_reponse</title>
  </head>
  <body>
  """
        print(html)
        print(f"tu as {montant}!")

        html = """
  </body>
  </html>
  """
        print(html)
