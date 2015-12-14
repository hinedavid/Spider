import random
import string
import subprocess
import os
import cherrypy
#import spider
import epublibre_crawler.spiders

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
        Ingrese la consulta y la cantidad de resultados que desea:
            <form method="get" action="generate">
              Autor:<input type="text" value="Edgar Allan Poe" name="query" />
	      Genero:<input type="text" value="horror" name="how_many" />
              <button type="submit">Procesar</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, query,how_many):
        #os.chdir(os.path.abspath(os.path.expanduser('/home/david/Desktop/spider')))
        subprocess.call(['/home/david/epublibre_crawler/test.sh', str(query),str(how_many)])
        fo = open("resultado", "r+")
        strt = fo.read(5000);
            
        return "consultas:" +how_many+""+ "\n resultado: \n" +""+strt

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
