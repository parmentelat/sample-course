---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  formats: md:myst
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
nbhosting:
  title: '%matplotlib inline'
---

# HTML outputs

```{code-cell} ipython3
%matplotlib inline
```

## matplotlib static

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
X = np.linspace(-10, 10)
Y = np.sin(X)
plt.plot(X, Y);
```

## interact

```{code-cell} ipython3
from ipywidgets import interact
```

```{code-cell} ipython3
def my_sinus(phase):
    X = np.linspace(-10, 10)
    Y = np.sin(X+phase)
    plt.plot(X, Y);
    
interact(my_sinus, phase=(0, 2*np.pi));
```
