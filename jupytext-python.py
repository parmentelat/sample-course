# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# ***NOTE***
#
# ce notebook est le premier de ceux qui utilisent un **workflow basé sur jupytext**
#
# en pratique ça signifie que
# * dans mon repo de travail je sauve automatiquement un `.ipynb` **ET** un `.py` 
# * je ne mets **sous git QUE le `.py`** 
#
# mon objectif est de vérifier que nbhosting fonctionne correctement avec de tels notebooks  
# **update**: ça ne fonctionne pas en l'état sous nbhosting; 
# mais j'hésite à faire la correction pour la raison suivante. 
#
#
#
# les avantages :
# * `git diff` plus facile (pas besoin de nbdime en fait)
# * `git commit` plus facile (pas besoin de nbstripout non plus)
# * `git pull` plus facile (jupytext est configuré pour **ne pas sauver certains détails** comme notamment le niveau de version de Python qui n'arrête pas de changer entre moi et les différentes images sur nbhosting)
#
# à suivre sur la durée donc

# %%
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)


# %%
fact(12)
