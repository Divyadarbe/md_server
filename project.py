from flask import Flask, abort, render_template
import glob
import os
import mistune
app=Flask(__name__)
from git.repo.base import Repo

md_files = [] # empty list to add .md files to
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
desktop = os.path.join(desktop,'Assignment1')

for file in glob.iglob(os.path.join(desktop,'**/*.md'),recursive=True):
    md_files.append(file)

#route handler to display all the href links and also connect to github and clones the repository
@app.route('/')
def index():

    if((os.path.isdir(desktop))==False):
        #clones the repository if repository folder doesn't exist
        Repo.clone_from("https://github.com/Divyadarbe/Assignment1", desktop)
        #searches .md files recursively & appends them to md_files
        for file in glob.iglob(os.path.join(desktop,'**/*.md'),recursive=True):
            md_files.append(file)
        #displays all the href links
        return render_template('link.html', md_files = md_files)
    else:
        return render_template('link.html', md_files = md_files)

#code to display the parsed html pages
@app.route('/render/<file>')
def render(file):
    if file not in md_files:
        abort(404)
    else:
        path = os.path.join(desktop, file)
        #reads the .md file
        with open(path) as f:
            data = f.read()

    return render_template('render.html', data=mistune.markdown(data)) 


if __name__=="__main__":
	app.run(debug=True)