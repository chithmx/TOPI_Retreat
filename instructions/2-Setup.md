## Setup

You need your own version of this repository, where you can actually change the content as much as you like (and which is not bound to me).

### SSH keys in GitHub

In order to work properly with GitHub everybody needs to register their SSH keys there (and this
way promise that it is actually you working on the code).

Please follow the steps at https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=webui .

Next, we can setup our own repository.

### git setup for the Captain

The captain (and only them) need to execute the following steps:

1. Create a new repository in GitHub under your account.
   Choose a meaningful name and description, else you can keep the repository completely empty - we will import some content next.
1. Clone the template repository: `$ git clone https://github.com/felixhekhorn/topi-git-template.git`
1. Change the origin (i.e. the source of truth) of the repository to your personal repo: `$ git remote set-url origin git@github.com:<your-account>/<your-repo>.git`
1. Push the current state to _your_ repository: `$ git push`
1. Add the other team members as Collaborators in GitHub to your repo: Security -> Collaborators -> Add people

### git setup for the others

Then everybody needs to clone _the Captain's_ repository: `$ git clone git@github.com:<captain-account>/<captain-repo>.git`

### Branches and Pull Requests

When a group implements a new feature always create a new branch, e.g. via `$ git switch -c my-new-branch`.
Remember that there will be three groups changing the repository in parallel - you can solve this by using branches.
Please use sensible branch names in real life.
Don't put too many changes into a single branch, before asking to merge it to the main branch.
Try to make one consistent change, e.g. adding one specific new feature, into one branch.
When you believe your feature is ready, create a Pull Request and ask for a review by the CEO group
(and the CEO group should ask to one or both other groups for their Pull Requests respectively).

Maybe add one intentional bug in your first Pull Request, to check if the Reviewer is actually doing
its job. One time is sufficient, because the material is complex enough that there will be
unintentional bugs around anyways :see_no_evil: .

Please write always concise, clear and descriptive commit messages - this will help you a lot.
See [this blogpost](https://cbea.ms/git-commit/) for a good reasoning.

Joining two different branches is called [merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
and when working with others on a common code basis, there will be situations where different branches want to
make incompatible changes. They are referred to as Merge Conflicts and you will need to address them before the actual
merge to take place, i.e. before you can merge a Pull Request. Often you need to decide on a case-by-case basis
if you want to keep the changes from branch A or from branch B or a mixture of the two.

### Python setup

1. Before you start to develop Python code, make a new virtual environment, e.g. with `$ python -m venv env`.
   This will create a folder `env/` where the actual environment is hosted.
   Create the environment in the base directory of the repository.
   The environment will be not tracked by `git` (since it is machine dependent) and so is not bound to a
   specific branch.
1. Next, you need to activate the new environment via `$ . env/bin/activate`.
   This new environment makes the development independent from the host system, gives full control over
   library versions and better reproducibility.
1. Next, we can install the necessary third-party libraries using `$ pip install -r requirements.txt`
