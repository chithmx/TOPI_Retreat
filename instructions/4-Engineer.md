## Exercise B - Engineer

The implementation strategy will be following closely the strategy in [Exercise A](./3-Engineer.md).

### Fitting

**Step 1:** Adjust the fitting procedure.

The new file structure will be:

1. first column $x_j$ as before
1. second column $y_j$ as before
1. third column $\sigma_j$ - the new uncertainty

Adjust the call to [scipy.optimize.curve_fit] to account for the uncertainty.

Check that the model parameters of `data/B-test.txt` match to `config/B-test.json`.

### Plotting

**Step 2:** Adjust the plot.

- Adjust the representation of the data points
- Give the goodness-of-fit $\chi^2$ in the plot

**Step 3:** Provide an advanced plot which includes the underlying law.

Add a new type of plot where you can include the underlying theory (and maybe its parameters) in addition
to the data and your fit (if the theory is known). Find a meaningful sorting in the drawing order.

### Command Line Interface

**Step 4:** Add a Command Line Interface (CLI).

Python provides the `argparse` library to provide simple command line interfaces.
The official tutorial can be found [online](https://docs.python.org/3/howto/argparse.html#argparse-tutorial)
You can also check `src/generate.py` for a simple example.

From the CLI the user should be able to tell

- which dataset he wants to analyze
- if and which plot he wants (or just text output)
