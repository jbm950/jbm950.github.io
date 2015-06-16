#
# This is a simple compiler that will take my markdown files and
# convert them to html files for the main directory
#

import os
import shutil
import subprocess
import sys

# Windows file separator compatibility
if sys.platform == 'win32':
    filesep = "\\"
else:
    filesep = "/"

# Create different front matters to be used by the compiler
defaultfm = "---\nlayout: default\n---\n\n"

# Find the current and final directory paths
sourcedir = os.path.dirname(os.path.abspath(__file__)) + filesep
parentdir = sourcedir.replace("source" + filesep, "")

for subdir, dirs, files in os.walk('.' + filesep):
    for file in files:
        if file.endswith(".md"):
            # if the file is a markdown file change it to an html file
            sourcefile = sourcedir + subdir.replace("." + filesep, "") +      \
                filesep + file
            print("converting: " + subdir + filesep + file)
            newfile = file.replace(".md", ".html")
            command = r"pandoc -s " + sourcefile + " --webtex -o " + newfile
            subprocess.call(command, shell=True)

            # Create the jekyll front matter
            sourcenewfile = sourcedir + newfile
            frontmatter = defaultfm
            with open(sourcenewfile, 'r') as original:
                data = original.read()
            with open(sourcenewfile, 'w') as modified:
                modified.write(frontmatter + data)

            # Move the new html files to the main directory and delete them
            # from the source directory
            newdir = parentdir + subdir.replace("." + filesep, "") + filesep
            if not os.path.exists(newdir):
                os.makedirs(newdir)
            shutil.copy(sourcedir + newfile, newdir + newfile)
            os.remove(sourcenewfile)
            print("Removed: " + sourcenewfile)
