import numpy as np
from sankey import sankey
from random import triangular

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

sankey(data['source'],
       data['sink'],
       leftWeight=data['weights'],
       figure_name='example')
