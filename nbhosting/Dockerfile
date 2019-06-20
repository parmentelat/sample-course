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

# the nbgitpuller thingy
RUN pip install git+https://github.com/parmentelat/nbgitpuller@nbhosting && jupyter serverextension enable --py nbgitpuller 

RUN jupyter labextension install @jupyterlab/git && pip install --upgrade jupyterlab-git && jupyter serverextension enable --py jupyterlab_git


