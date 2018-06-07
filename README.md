# Fork of pySankey
See the original project here: <a href="https://github.com/anazalea/pySankey">pySankey</a>

## Purpose of pySankey
Uses matplotlib to create simple <a href="https://en.wikipedia.org/wiki/Sankey_diagram">
Sankey diagrams</a> flowing only from left to right.

## Purpose of this Fork
Modify the interface of the main routine so as to allow passing of lists of colors
(without specifying the actual names (maybe they aren't pre-known?)), outputting as
SVG instead of PNG, and eventually add more resilience to the allowed input structures.

## Requirements

Requires python-tk (for python 2.7) or python3-tk (for python 3.x) you can
install the other requirements with:

``` bash
    pip install -r requirements.txt
```

