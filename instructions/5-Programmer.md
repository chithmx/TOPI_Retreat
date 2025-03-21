## Exercise C - Programmer

Usually the actual hard programming a major task, but we don't want to make our simple model here too complicated.
Thus, we focus on two like-wise important tasks now.

### Documentation

If either you or the Engineer has not done a proper documentation yet, tell the CEO they should have complained before accepting
the respective Pull Requests. Catch-up (everywhere) now if necessary.

The most popular Python library to create a well-structured documentation is [Sphinx](https://www.sphinx-doc.org/en/master/).

Check the quick-start guide: https://www.sphinx-doc.org/en/master/usage/quickstart.html

As said there, you typically want the [autodoc feature](https://www.sphinx-doc.org/en/master/usage/quickstart.html#autodoc).

**Step 1:** Write a proper documentation for all your codes.

The documentation should describe clearly the underlying problem, the developed program,
the available options and showcase some examples.
Recall that the documentation defines your interaction with the outside world.
Maintaining the documentation is thus crucial if you want other people to use your tools.

_Hints:_

1. Use the `doc/` directory to host your documentation to keep it separated from the actual code
1. It is common to not commit generated files to the version control system, that is why there is a `.gitignore` file

### Typing

Python does not require to specify types when writing your code, but uses an implicit deduction - this
is often referred to as [duck typing](https://en.wikipedia.org/wiki/Duck_typing).
However, having explicit types can be very helpful because then you know with what kind of objects you are
dealing with - this can be particularly helpful with [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment).
In order to help with this, Python is providing the [typing module](https://docs.python.org/3/library/typing.html).

**Step 2:** Add types to your code if you haven't done so yet.

You can also check, if your types are consistent using [mypy](https://mypy.readthedocs.io/en/stable/index.html) - which
you can even add to your pre-commit configuration.
