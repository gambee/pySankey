# example.py
# Max Gambee
# NOTE: This is intended as an automation of the creation of the expample.svg
#       in the github repo (& README.md). Not intended as a use case or coding
#       example. Hence, it is not stylistically nor annotationally conducive
#       of learning.

import numpy as np
from sankey import sankey
from random import triangular


# Build the example data,
#   You are not expected to understand this.
data = dict(zip(
    ['source', 'sink', 'weights'],
    [
        np.array(d)
        for d in
        [
            i
            for i in zip(*sum(
                [
                    [
                        (src, snk, triangular(high=10))
                        for src in 'Fee-Fi-Fo-Fum'.split('-')
                    ]
                    for snk in 'I smell the blood of an Englishman'.split(' ')
                ],
                []))
        ]
    ]))

# Save the example data into an SVG Sankey Diagram
sankey(data['source'],
       data['sink'],
       leftWeight=data['weights'],
       figure_name='example')
