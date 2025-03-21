This directory holds the data files.

The files are in `txt` format and you can load them, e.g., with
[numpy.loadtxt](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html)
and write them with [numpy.savetxt](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html).

Each row represents one measurement and the columns correspond to
- in `A-test.txt`: the abscissa $x_i$, the ordinate $y_i$
- in `B-test.txt`: the abscissa $x_i$, the ordinate $y_i$, the uncertainty $\sigma_i$

The files are used for the respective exercises.

`A-test.txt` has to be reproduced by generating data from `config/A-test.json`,
but `B-test.txt` has to be only statistically equivalent to data generated from `config/B-test.json`.

Put your generated data files into this directory.
Define your own naming convention for the files and you should document that
(here for example).
