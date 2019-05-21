# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/scipy-notebook

# the nbgitpuller thingy
RUN pip install nbgitpuller && jupyter serverextension enable --py nbgitpuller 

# for bash
RUN pip install calysto_bash
