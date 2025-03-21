## Exercise A - Engineer

Your main task will to do the actual fitting, based on the datasets provided
by the Programmer.

You will work on the `src/fit.py` file - take a look there!

:octocat: Remember to make new branches and to commit regularly to them.

### Fitting

We _assume_ the dataset describes a ski jump under the influence of gravity.
If we can setup a model, which reflects this assumption, and we can fit this model,
we can be confident that it was a normal ski jump after all (and we learned that
gravity acts on earth).

**Step 1:** Determine the starting velocity and starting angle of the test dataset `data/A-test.txt`.

1. Read the input data from file
1. Define the model: $y(x;a,b) = a*x + b*x^2$ (as you know: with gravity objects fly like parabolas and we start at the origin)
1. Fit the model parameters $a,b$ to the data using
   [scipy.optimize.curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html#curve-fit)
1. Find the transformation from $a,b$ to the initial velocity and initial angle

Check that the model parameters of `data/A-test.txt` match to `config/A-test.json`.

### Plotting

Next, we want to visually check if the fit actually makes sense.

**Step 2:** Plot the data and your fit into one diagram.

_Hint:_ Recall that the data points are just points, but the model is a smooth function.

For a small number of model parameters it often makes sense to print them in the plot.

:octocat: Remember to commit regularly.

### Code organization

Can you organize your code in such a way that Step 1 and Step 2 are _independent_ from each other?
This would make sense as they are indeed two orthogonal things: Step 1 is doing the actual physics,
but Step 2 is just one possible way to use the result and specifically one out of many ways to present
the result in a reader-friendly way.
