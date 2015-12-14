# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
#epublibre_spider.py

# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

# Importar la clase donde almacenar los resultados
from epublibre_crawler.items import BookItem

class BookSpider(CrawlSpider):

    name = "epublibre"

    # Dominios en los que el crawler tiene permiso a acceder
    allowed_domains = ["epublibre.org"]

    # La direccion de inicio para el crawler
    start_urls = ["http://www.epublibre.org"]

    # Regla para diferenciar los enlaces de libros y funcion que se les aplica
    rules = [Rule(SgmlLinkExtractor(allow=['/libro/detalle/\d+']), 'parse_book')]

    def parse_book(self, response):
        """ Parser para las pagina de detalle de los libros"""
        filename = response.url.split("/")[-2]
        sel = Selector(response)
        text = response.body
        open(filename, 'wb').write(text)
        # Creamos un nuevo libro y asignamos los valores extraidos a
        # los campos correspondientes.
        book = BookItem()
        author = sel.xpath("//div[@class='negrita aut_sec']/a/text()").extract()
        title = sel.xpath("//div[@id='titulo_libro']/text()[normalize-space()]").extract()

        # Con Strip eliminamos tabulaciones y linea nueva.
        book['title']  = title[0].strip("\t\n\r")
        book['author'] = author[0].strip("\t\n\r")

        return book
