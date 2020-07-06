---
jupytext:
  cell_metadata_filter: all
  cell_metadata_json: true
  encoding: '# -*- coding: utf-8 -*-'
  formats: md:myst
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# markdown-only

+++

un notebook que l'on publiie seulement au format `.md`

celui-ci est spécifiquement au format `myst`

```{code-cell} ipython3
def fibo(n):
    return 1 if n <= 1 else fibo(n-1) + fibo(n-2)
```

```{code-cell} ipython3
fibo(8)
```
