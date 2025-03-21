## Exercise A - Programmer

Your main task will be to provide the dataset - i.e. the starting point for the Engineer.
We will do so by inventing our own universe in which we dictate the laws of physics.
In order to generate these dataset we develop a set of tools,
which we can then execute.

_Hint_: It often makes sense to do the implementation (Step 1) and the unit test (Step 2) in parallel.
This way it could, e.g., make sense to just put the implementation of the trajectory
and its associated unit tests into one branch. Next, you could, e.g., put the file reading
and its associated unit tests into one branch, etc.

You will work on the `src/generate.py` file - take a look there!

### Implementation

**Step 1:** Complete the implementation of `SkiJump.y`, `SkiJump.from_json_file`,
and `SkiJump.landing`.

_Hints:_

- for `SkiJump.y`: it is $y(x) = a x + b x^2$ - determine $a,b$ from the
  initial velocity and angle! (Yes, this is a math exercise :books: )
- for `SkiJump.from_json_file`: use [`json.load`](https://docs.python.org/3/library/json.html#json.load)
- for `SkiJump.landing`: More math!

:octocat: Remember to make one or several new branches and to commit regularly to them.

We will leave `SkiJump.sample` for step 3.

### Unit testing

Next, we want to check if the implementation is actually correct - we can do this
by using the concept of [Unit testing](https://en.wikipedia.org/wiki/Unit_testing).
Unit test execute a small piece of code in a fully controlled environment and check if it
fulfills the expectations.

- If a code does not pass the unit tests there is no hope it will work in real life
- Unit tests should test a small, independent piece of logic
- Unit tests should be executed regularly, e.g. on every commit (in the CI)
- Unit tests often check invariants or symmetries of your code

The most popular unit test framework for Python is [pytest](https://docs.pytest.org/en/stable/).

Take a look to the `tests/test_generate.py` file!
By convention unit test files start with `test_`and also unit test functions start with `test_`.

Execute the already available unit test via

```sh
$ pytest tests/
```

**Step 2:** Check your implementation using the available unit tests and write the missing ones.

:octocat: Remember to commit regularly.

:octocat: You should create a Pull Requests for every branch now (if not done already).

### Data generation

Finally, we have all tools at hand to write the actual datafile.
To execute the generation script execute

```sh
$ python src/generate.py
```

This command will not work out of the box, but it will tell you what you need to run explicitly.
We fix the underlying code in the next step.

:octocat: You may want to create a new branch which is based on your previous one for these new changes
(since they are almost independent to the former changes).

**Step 3:** Complete the implementation of `SkiJump.sample` and the dataset generation script in `src/generate.py`.

Check that `config/A-test.json` reproduces `data/A-test.txt`, i.e. when running

```sh
$ python src/generate.py config/A-test.json data/A-test-new.txt -n 3
```

you should compare `data/A-test.txt` and `data/A-test-new.txt`.

( :octocat: Advanced question: the above command generates a new file, but recall that we said `git` keeps track of files
and their history. So how can you compare a file across different branches or commits?)

Generate some new theories (in `config/`), then generate a new dataset (from those theories), and then put them into
the `data/` folder for the Engineer (using of course new names everywhere).

:octocat: If you made a new branch, remember also to create a new Pull Request (also put the "base branch"
there to the other branch, such they sit on top of each other)
