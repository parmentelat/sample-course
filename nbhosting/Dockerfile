# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/scipy-notebook

# for bash
RUN pip install calysto_bash

### configure git 
RUN git config --global user.email "notebook.user@example.org" && git config --global user.name "Notebook User"

# for debugging
RUN apt-get install rsync

RUN pip install --pre rise

RUN apt-get install -y graphviz
RUN pip install folium graphviz
