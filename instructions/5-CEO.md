## Exercise C - CEO

### Issues

**Step 1:** Open Issues for the various groups if you think that was useful.

Check the respective group instruction pages for possible items.

### Packaging

Python provides an easy way to bundle and distribute libraries and also associated scripts:
building actual Python packages.

First, you should turn the `src/` folder into an actual module by adding an empty file
called `__init__.py`.
To learn more about modules you can read, e.g., [the online documentation](https://docs.python.org/3/tutorial/modules.html).

Next, we want to setup the Python package: this can be achieved by writing a `pyproject.toml` file.
Read the online documentation on how to create this file: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

**Step 2:** Write a `pyproject.toml` file.

By convention the source files of the package are in `src/<your-package>/`, i.e. you should move the current files
in `src/` one directory down with the name that you choose for your package.
The same applies to the unit tests in the `tests/` directory: move them one down.

You can read more about the general idea of packaging online: https://packaging.python.org/en/latest/tutorials/packaging-projects/

### Documentation

This step requires the documentation, which is on the menu of the Programmer in exercise C, already to be available - if
it isn't help with that first.

The documentation defines your interaction with the outside world and many Python packages provide their
documentation via [readthedoc](https://about.readthedocs.com/).
Since we are not developing a proper Python package, but only some demo package we can opt for the second most
popular solution: hosting the documentation via [GitHub Pages](https://pages.github.com/).

**Step 3:** Expose your documentation via GitHub Pages.

There are several ways to do this, but the basic idea is:

1. you need to build the documentation using [Sphinx](https://www.sphinx-doc.org/en/master/)
1. you need to expose the generated HTML files to GitHub Pages
