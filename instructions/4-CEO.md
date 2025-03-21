## Exercise B - CEO

### Issues

**Step 1:** Open three Issues to track the status of the three groups in Exercise B.

#### CEO Issue

Title: `B/CEO`
Assignees: the CEO group
Description:

```
- [ ] open all issues for exercise B
- [ ] exercise A is correct
- [ ] Readme
- [ ] pylint
```

#### Programmer Issue

Title: `B/Programmer`
Assignees: the Programmer group
Description:

```
- [ ] Update `SkiJump`
- [ ] Extend unit tests
- [ ] generate new datasets
```

#### Engineer Issue

Title: `B/Engineer`
Assignees: the Engineer group
Description:

```
- [ ] Update fit
- [ ] Update plot
- [ ] Extended plot is available
- [ ] CLI is available
```

### Double-checking

**Step 2:** Double-check Exercise A

#### Internal

Double-check the work of the Programmer and the Engineer from Exercise A: i.e.

- there are several theories in `config/`
- there are several datasets in `data/`
- each theory reproduces its matching dataset (i.e. the data generation of the Programmer is correct)
- a fit to each dataset yields back the underlying theory (i.e. the fitting routine of the Engineer is correct)
- the plots of the fits look reasonable
- there are unit tests for all features in `src/generate.py` and all unit tests pass,
  i.e. `$ pytest tests/` yields all green (if you have the proof in the CI even better!)

#### Other teams

- Open a new issue at [the template repository](https://github.com/felixhekhorn/topi-git-template/issues) and upload
  a few datasets there _without_ telling the underlying theory
- Check for other available datasets there, download them, and then determine the model parameters.
  Track your results in an Issue in _your_ repository.

### Readme

**Step 3:** Update the main Readme of the repository to something more meaningful

This can, e.g., include

- what the repository is about,
- implemented features,
- badges are very popular, e.g. [for Workflows](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/adding-a-workflow-status-badge),
- ...

### Linting

Another useful tool while developing software are [linters](<https://en.wikipedia.org/wiki/Lint_(software)>).
They perform a static code analysis and can this way find trivial bugs, e.g. invalid variable names and incorrect scopes,
or avoid duplication. The most popular tool in Python is [pylint](https://www.pylint.org/).

**Step 4:** Add `pylint` to the tool stack

This includes:

- installing it (remember the `requirements.txt` file!)
- running it and fixing possible errors
- add it to the CI
