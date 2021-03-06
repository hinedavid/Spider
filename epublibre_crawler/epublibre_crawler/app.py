import random
import string
import subprocess
import os
import cherrypy
import spiders.__init__.py

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
        Ingrese la consulta y la cantidad de resultados que desea:
            <form method="get" action="generate">
              Busqueda:<input type="text" value="5" name="query" />
	      Resultados:<input type="text" value="5" name="how_many" />
              <button type="submit">Procesar</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, query,how_many):
        #os.chdir(os.path.abspath(os.path.expanduser('/home/david/Desktop/spider')))
        #subprocess.call(['/home/david/Desktop/spider/test.sh', str(query),str(how_many)])
	process = CrawlerProcess()
	process.crawl(BookSpider)
	
	process.start() # the script will block here until all crawling jobs are finished

        fo = open("resultado", "r+")
        strt = fo.read(5000);
            
        return "consultas:" +how_many+""+ "\n resultado: \n" +""+strt

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
