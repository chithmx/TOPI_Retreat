## Exercise A - CEO

Your main task will be to organize the repository.

### Pull Requests and Issues

Make sure that all three groups use Pull Request to implement new features and that a suitable reviewer is assigned.
For every Pull Request check that the contributions

- make sense, i.e. they are physically correct
- do not contain trivial typos
- are sufficiently documented

**Step 1:** Open three Issues to track the status of the three groups in Exercise A.

It often makes sense to annotate the respective Pull Request or commit behind a completed task,
e.g. `- [ ] task 1` -> `- [x] task 1 #123`.
Make sure to understand what a specific item is about and ask for clarification if necessary.

#### CEO Issue

Title: `A/CEO`
Assignees: the CEO group
Description:

```
- [ ] open all issues for exercise A
- [ ] enforce code formatting via pre-commit
- [ ] add CI with unit tests
```

#### Programmer Issue

Title: `A/Programmer`
Assignees: the Programmer group
Description:

```
- [ ] complete `SkiJump`
- [ ] unit test all methods
- [ ] complete data generation
- [ ] can reproduce `data/A-test.txt`
```

#### Engineer Issue

Title: `A/Engineer`
Assignees: the Engineer group
Description:

```
- [ ] can fit template data
- [ ] plot fit comparing to data
- [ ] can reproduce values in `config/A-test.json`
```

### Code formatting

When writing larger pieces of code (meaning >50 lines) or when developing codes together in a
collaboration code formatting is becoming an issue.

For example, this is allowed Python code

```py
def f(a   = .1, b=0.):
    return a  +b
f(
1.,     3.)
```

but arguably much harder to read then

```py
def f(a=0.1, b=0.0):
    return a + b


f(1.0, 3.0)
```

Let's use _the same_ formatting everywhere - we can do this by
using the popular [black](https://github.com/psf/black) program.

Now, just using `black` on its own would require everybody to run it constantly - but people might forget it
and we are back to square one, with all mixed code formatting.

Instead, we can _enforce_ the running of `black` by making it run _before every commit_, i.e. before anyone can
contribute to the repository. We can do so by using the [hooks](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks)
which `git` provides and specifically there is a convenient python library for precisely that purpose:
[pre-commit](https://pre-commit.com/).

**Step 2:** Add a pre-commit configuration using the [Quick Start instructions](https://pre-commit.com/#installation) which
should include (at least) the standard white-space hooks and `black`.

Implement this feature through a Pull Request and tell your collaborators this way what they should do and how they can activate
it on their machines. Run `black` on the existing code already.

### GitHub Actions

We want to further automatize things, that _should_ be run all the time but which people might forget.
This concept is called Continuous Integration (CI) and the implementation in GitHub is called
[GitHub Actions](https://docs.github.com/en/actions).

Take a look to the official tutorial: https://docs.github.com/en/actions/writing-workflows/quickstart

One prominent case of a task which should be run in the CI and our example case here is
[Unit testing](https://en.wikipedia.org/wiki/Unit_testing).

Note the difference between pre-commit (discussed above) and the CI:

- pre-commit is installed locally on every machine vs. the CI is run centrally by GitHub
- pre-commit is run on every commit vs. the CI can be triggered on a wide variety of events (including every commit)
- pre-commit is used mostly for basic code tasks (e.g. static code analysis, formatting, white space control) vs.
  the CI may contain complex tasks (using nested instructions or external resources)
- pre-commit should terminate in O(seconds) vs. the CI may take minutes or even hours (Note that GitHub has a time limit)
- pre-commit can run in the CI: https://pre-commit.ci/

**Step 3:** Write a CI script for unit testing.

The machines standing behind the GitHub Actions are just bare machines, so we need to tell them everything
that is needed to run our checks. So, the CI script should look like this:

1. Checkout the repository: [actions/checkout@v4](https://github.com/marketplace/actions/checkout)
1. Install Python: [actions/setup-python@v5](https://github.com/marketplace/actions/setup-python)
1. Install the dependencies that you need for your project (remember the [Setup](./2-Setup.md) instructions)
1. Run the unit test using `$ pytest tests/`
