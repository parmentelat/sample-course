---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# licence tag & images

+++

let's start with the usual way we used to display licences; that works in the nb but not too well in jb

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<div style="display:grid">
    <span>Thierry Parmentelat</span>
    <span>Valérie Roy</span>
</div>
<div style="display:grid">
    <span>
        <img src="media/inria-25-alpha.png" />
    </span><span>
        <img src="media/ensmp-25-alpha.png" />
    </span>
</div>
</div>

+++

the conjecture is with the html embedding; so an alternative could maybe be

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<div style="display:grid">
    <span>Thierry Parmentelat</span>
    <span>Valérie Roy</span>
</div>
</div>

<img src="media/inria-25-alpha.png" />
<img src="media/ensmp-25-alpha.png" />

+++

## std markdown

+++

![](media/les-mines.jpg)

+++

## myst markdown

+++

because we use myst, we can tweak stuff like this

at least [that's what this page says](https://jupyterbook.org/content/figures.html#images) but I haven't yet gotten that to work as advertised

+++

```{image} media/les-mines.jpg
:alt: les-mines-myst
:class: bg-primary mb-1
:width: 200px
:align: center
```

+++

## raw html

+++

<img src="media/les-mines.jpg">

+++

## raw html with attributes

+++

<img src="media/les-mines.jpg" alt="les-mines" class="bg-primary" width="200px">
