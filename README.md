# Problem statement:Parse all MD files from a GitHub repository and render the result in HTML format in a web server

1.create virtual environment(pip install virtualenv env)
2.activate scripts
3. install Flask(pip install Flask)
4. install mistune module(pip install mistune)->to parse html files

It contains project.py file and templates folder contains link.html and render.html
When we run project.py, it connects to git hub and clones Assignment1(contains .md files) to local repository(to Desktop).
Then server builds and  display all the routes.
If we click on the link, it displays respective parsed html files.
