#
# This is a simple compiler that will take my markdown notes files and create
# html files using pandoc and move the resultant files to the main notes
# directory.
#

import os
import shutil
import subprocess

sourcedir = os.path.dirname(os.path.abspath(__file__)) + "/"
parentdir = sourcedir.replace("source/", "")

for subdir, dirs, files in os.walk('./'):
    for file in files:
        if file.endswith(".md"):
            # if the file is a markdown file change it to an html file
            newfile = file.replace(".md", ".html")
            command = "pandoc -s " + file + " -o " + newfile
            subprocess.call(command, shell=True)

            # Create the jekyll front matter
            sourcenewfile = sourcedir + newfile
            frontmatter = "---\nlayout: default\n---\n\n"
            with open(sourcenewfile, 'r') as original:
                data = original.read()
            with open(sourcenewfile, 'w') as modified:
                modified.write(frontmatter + data)

            # Move the new html files to the main directory and delete them
            # from the source directory
            newdir = parentdir + subdir.replace("./", "") + "/"
            if not os.path.exists(newdir):
                os.makedirs(newdir)
            shutil.copy(sourcedir + newfile, newdir + newfile)
            os.remove(sourcenewfile)
