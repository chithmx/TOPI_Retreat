## Exercise C - Engineer

So far we were doing exactly 1 fit to the information, which was given to us.
The central values are the most likely outcome of the measurement and the uncertainties
were used in determining this one fit. Of course in this way we got a single
set of best model parameters ($a, b$).
In our simple case here `curve_fit` also provides us in addition with an uncertainty
on those model parameter, but how about more a complicated case?

Actually, we can go one step further by applying the Monte Carlo replica method
(see e.g. [JHEP 12 (2024) 064](<https://doi.org/10.1007/JHEP12(2024)064>) and reference there in for a more
detailed discussion).
The idea is that we can consider the data that we have just as
_one particular measurement out of many possible_. The central value is still the most likely true value
(and we trust that who ever made the measurement did the best he could), but we now go beyond by
generating **pseudodata replicas**. We can do so if we assume that we know the true data distribution.
In this case we will (correctly) assume that the data is distributed Gaussian around the central value.

How to do this in practice? For a given datapoint $y_i$ with (gaussian, i.e. statistical) uncertainty $\sigma_i$
we generate a new pseudodata replica, by drawing 1 sample from a Gaussian distribution centered at $y_i$
and with standard deviation $\sigma_i$. Each replica is a new sample. The uncertainty associated with each
replica is still $\sigma_i$.

In this way the **ensemble of replicas**, i.e. the collection of all replicas together, will, with
sufficiently many replicas, be again a faithful distribution of the underlying measurement.
Together they encode the same information, i.e. the central value $y_i$ and its uncertainty $\sigma_i$.
Keep in mind that a single replica has no statistical meaning (the same way a single toss of the dice does not
say anything), but only the ensemble of replicas. You can think of a pseudodata replica as a hypothetical
new run of the very same measurement.

Now, if we do a fit **to each of the pseudodata replicas in turn** we get also a distribution of the
model parameter, which we can again statistically analyze to get an uncertainty on the model parameters
(see also e.g. [Eur.Phys.J.C 82 (2022) 4, 330](https://doi.org/10.1140/epjc/s10052-022-10297-x) for more
mathematical details).

Note that this procedure is completely independent from how the Programmer generate their data in
Exercise B - we only use the (public) information in the data files here. They are only in so far
connected as in our controlled fake environment here we use consistent settings, i.e. everything is
Gaussian everywhere. In real life the data distribution is (much) more complicated and in principle unknown
(that's why we fit in the first place). However, often we _assume_ to know the data distribution
(specifically that it is Gaussian). Note that also correlated (systematic) errors can be included into
the pseudodata generation (as long as they are faithfully estimated).

### Fitting

**Step 1:** Define a MC sampler class

The class could, e.g., look similar to this:

```py
class MCSampler:
    """Monte Carlo pseudodata generator."""
    central: np.ndarray
    """Central values."""
    yerr: np.ndarray
    """Uncertainties."""
    def next() -> np.ndarray:
        """Generate a new sample"""
        # do the actual sampling here
```

**Step 2:** Fit to 100 replicas.

1. Draw N replicas
1. Make 1 fit to each replica in turn
1. Keep track of your results

### Plotting

**Step 3:** Adjust the plots.

Typically you don't want to draw all replicas (since they have no statistical meaning - though you can just
to check if they are reasonable), but you want to convey the statistical meaning, i.e. the central value, which
you can obtain by averaging over all replicas, and the uncertainty, which you can obtain by using the standard
formulae.

**Step 4:** Plot the model parameters.

- The typical plot is to bin the obtained model parameters and then show their frequency
- Since everything is Gaussian, the plot has also to be a Gaussian around the true value (which you can know from the Programmer)
- If you want to show an advanced plot you can show the correlation between the model parameters, by plotting $a(b)$ (or similar)

**Step 5:** Plot the goodness-of-fit distribution.

Again, since everything is Gaussian, also this plot has to be a Gaussian.
