This directory holds the definitions of the underlying theories.

The files are in [JSON](https://en.wikipedia.org/wiki/JSON) format and
we use the [json module](https://docs.python.org/3/library/json.html) of Python
to parse them.

- `A-test.json` is used as an example configuration in Exercise A
- `B-test.json` is used as an example configuration in Exercise B

Put your invented configurations into this folder.
Define your own naming convention for the files and you should document that
(here for example).

If your data generation script is not backward compatible, i.e. the version
from exercise B can not parse the cards from exercise A, you could e.g. not the
last available commit here.
