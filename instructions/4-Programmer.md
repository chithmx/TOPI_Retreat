## Exercise B - Programmer

In the following we will assume that the uncertainty will be a linear function in $x$.
More mathematically speaking we assume that a data point $y_j$ is given by

$$y_j = y(x_j) + N(\mu=0, \sigma^2 = (x \cdot \tau)^2)$$

where $N(\mu,\sigma^2)$ is the [Gaussian normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
centered around the mean $\mu$ and with standard deviation $\sigma$.
With this model we are introducing (linear) noise away from the origin - one possible (realistic)
physical scenario could be that our camera is mounted at the origin and we have a weaker
resolution at the edge.

The implementation strategy will be following closely the strategy in [Exercise A](./3-Programmer.md).

### Implementation

**Step 1:** Implement the new model.

Since we introduced a new model parameter, $\tau$, we need to

1. add the parameter to our generator class `SkiJump`
1. adjust `read_from_json`
1. we can assume that if the variable is not defined in the config, it is 0 - this way the code will be backward compatible

Once we have access to the parameter, we need to adjust `SkiJump.sample`.
The relevant function in numpy is [`numpy.random.Generator.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal).

### Unit tests

**Step 2:** Extend the unit tests.

If your code is backward compatible, it is usually good to _extend_ the unit tests rather then replacing them.
(Of course also test code may need every now and then some refactoring - it is ordinary code in the first place.)

When writing a test for a function, which includes random number generation (such as `SkiJump.sample` now), some care must be taken
about the "randomness".
Recall that it is very difficult for computers to generate actually (mathematically) "true" random numbers.
Instead they rely on [pseudorandom numbers](https://en.wikipedia.org/wiki/Pseudorandom_number_generator), which are a deterministic
series of numbers based on a [random seed](https://en.wikipedia.org/wiki/Random_seed).
This means by _forcing_ a specific seed we can get back the controlled environment that we want to have in a unit test.
In Numpy the seed can be set in [`numpy.random.default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng).

Summary: always set a seed when testing random numbers.

### Data generation

**Step 3:** Generate new datasets.

The data generation procedure itself may (or may not) need to be slightly changed, since `SkiJump.sample` now also needs to give the uncertainty.
Surely, you need to adjust the file dumping since now we want to add as a third column the respective uncertainty.

Check that you can process `config/B-test.json`. Note that this will _NOT_ reproduce `data/B-test.txt` as this was generated with
a special seed (I'm joking :upside_down_face: I faked it).

Also generate multiple datasets from a single configuration.

_Hint:_ as an extra you can implement an argument to the CLI which allows users to set a seed if they wish - this way also the CLI becomes
reproducible again.
