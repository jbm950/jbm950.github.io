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

F = open(folderpath + filesep + filename + ".md", "w")
headingln1 = "__" + name + "__  \n"
headingln2 = "__" + author + "__  \n"
headingln3 = "__Published in " + journal + ": " + date_pub + "__  \n"
headingln4 = '<a href="' + link + '" target="_blank">Full Article</a>\n'

heading = [headingln1, headingln2, headingln3, headingln4]

for line in heading:
    F.write(line)

print("Add this to notes_main.md")
print("[" + name + "](" + folderpath.replace("." + filesep + "notes", "") +
      filesep + filename + ".html) (" + author + ")")
