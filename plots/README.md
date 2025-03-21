The Engineer can put the generated plots (in `.pdf` format) into this directory.

Note that it is usually a good idea to not commit generated files to the
version control, but rather the recipe to generate them.
This is why the [`.gitignore` file](https://git-scm.com/docs/gitignore) is
currently such that it ignores all `.pdf` files.

However, you may want to make an exception from that rule for plots which are needed in other context.
For example these plots may solve a given exercise, demonstrate a specific feature, or might be included in a
Readme or the documentation (though it might be even better to use a dedicated place).
To do so, you can adjust the local [`.gitignore`](./.gitignore) file:
```
# exclude all PDF files
*.pdf
# but this one
!solution_exercise_a.pdf
```
