# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/scipy-notebook

RUN true \
 # for bash \
 && pip install calysto_bash \
 ### configure git \
 && git config --global user.email "notebook.user@example.org" && git config --global user.name "Notebook User" \
 # for debugging \
 && apt-get install rsync \
 && pip install --pre rise \
 && apt-get install -y graphviz \
 && pip install folium graphviz \
 && true
