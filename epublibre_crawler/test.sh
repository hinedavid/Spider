#! /bin/bash
# Script 

echo "some data for the file" >> "$1"
echo "some data for the file" >> "$2"
scrapy crawl epublibre -o libros.json -t json
