# This program will take the name of an article, date published, magazine
# published in, author of the article and make the folder, markdown file and
# link on the notes page

# Also will need subheading for the articles (ex. Engineering)
import os
import sys

name = input("Name of Article: ")
author = input("What is the name of the author(s) of the article: ")
date_pub = input("Date that the article was published (Month Year): ")
journal = input("What was the name of the journal it was published in: ")
link = input("Link to page displaying the article: ")
subhead = input("Subheading for the article to fall under (if none put None): ")

if sys.platform == 'win32':
    filesep = "\\"
else:
    filesep = "/"

filename = name.replace(" ", "_").lower()
folderpath = "." + filesep + "notes" + filesep + filename
if not os.path.exists(folderpath):
    os.makedirs(folderpath)
else:
    AttributeError("Filename already exists")
