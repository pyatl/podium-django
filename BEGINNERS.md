# Beginner's Guide to Contributing #

## Introduction ##
This guide is meant to provide you step-by-step instructions on how to get the
appropriate tools and configuration in place to contribute code or
documentation changes to the project on Github, following standard best
practices used throughout the open source community.  While these instructions
are intended to be specific to *this* project, they should be applicable to
many other projects, both open source and private.

## What You Need ##
Before you can begin coding and contributing, you'll need the following:
- A Github account.  You can sign up for a free account [here](
https://github.com/join).  Remember that peers, coworkers, and potential
future employers may look you up on Github, so take some time to make sure
your profile is filled out with appropriate information.
- A git client of your choice.  The [command-line git client](
https://git-scm.com/downloads) is the most common, and is used for the
examples in this guide.  There are a variety of [GUI clients](
https://git-scm.com/downloads/guis) as well if you prefer.
- A copy of Python 3.  This project is tested with Python 3.6.1. Download it
[here](https://www.python.org/downloads/release/python-361/) or use your
package manager to install it if you're on Linux.
- The Python package installer, `pip`.  You can install it by following the
[instructions here](https://pip.pypa.io/en/stable/installing/). Once you've
installed it you can verify your install by running `pip --version` on your
command line.  You should see something like this:
    ```
    pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
    ```
- **(Optional)** The PostgreSQL database engine.  You can [download it](
https://www.postgresql.org/download/) or install it from your package manager.
If you can't install or set up Postgres, the project is set up to fall back on
the sqlite3 database, which is included in Python 3.

## Initial Setup ##
Your set up as a contributor is going to be slightly different than simply
setting up the project to use it on your own. You're going to fork the Github
repository to create your own copy, commit and push your changes there until
you're satisified with them, and then create a Pull Request to submit your
changes back to the original repository, where a maintainer will review and
eventually merge the changes.  Follow these steps for your intial setup:
- Go to the primary repository at https://github.com/pyatl/podium-django
- Click the Fork button on the top right side of the page to create your own
copy of the repository under your own account name.  This will be the copy
you have write access to and can push changes to.
- Open a terminal on your local machine, change directories to where you
want to keep the project, and clone your forked repository.
    ```
    git clone https://github.com/<your username>/podium-django
    ```
You should now have a local repository of all the code, with a remote named
`origin` which points back to your forked repository.
- Switch directories into the newly created podium-django directory and add a
second remote to point back to the original upstream repository. This will be
the remote you use to update your fork with the latest changes to the primary
repository.
    ```
    git remote add upstream https://github.com/pyatl/podium-django
    ```

## Getting the Project Running ##
Before you make any modifications the project, you want to ensure you can run
the project as-is.  This will help you diagnose any issues you may run into
when making modifications, so you can be sure it isn't being caused by
something unrelated to your own changes.
- **(Optional)** Set up a [virtualenv](https://virtualenv.pypa.io/en/stable/)
for the project.  This will help avoid any unwanted interaction with any other
projects you may have on your development machine.
    - Create the virtualenv.  You can call it whatever you like and keep it
in whatever directory you like.
        ```
        python3 -m venv <virtualenv directory>
        ```
    - Activate the virtualenv.
        ```
        Linux / OS X:
        source <virtualenv directory>/bin/activate

        Windows:
        <virtualenv directory>/Scripts/activate.bat
        ```
    You only nee to create the virtualenv once, but you'll need to activate it
    each time you work on the project.
- Change to the project's directory, and install the project's Python package
requirements.
    ```
    pip install -r requirements.txt
    ```
- If you've installed PostgreSQL, create a database and a user. Skip this step
you intend to use sqlite3 instead.
    ```
    # Connect to Postgres.  You may need to do this as a different user
    # on some systems.
    psql
    # Create the database
    CREATE DATABASE podium;
    # Create a user
    CREATE USER podium_user WITH PASSWORD 'abc123';
    # Disconnect from Postgres
    \q
    ```
- Copy the example.env at the project root to a new .env file.
- Edit the .env file and fill in information for your own development environment.
    - If using PostgreSQL, set the `DATABASE_URL`.  If using sqlite3, just
comment out the `DATABASE_URL` variable instead.  For Postgres, the url format
should be `postgres://username:password@hostname/database`.  So, for the
database created above, assuming Postgres is running locally, the
`DATABASE_URL` would be `postgres://podium_user:abc123@localhost/podium`
   	- Create a .env file and set anything for `DJANGO_SECRET_KEY`
	 - Create your own random secret key to fill in the `DJANGO_SECRET_KEY` value.
        ```
        python manage.py shell
        >>>from django.core.management.utils import get_random_secret_key
        >>>get_random_secret_key()
        ```
    - Uncomment the `DJANGO_DEBUG` variable to enable Django's debugging mode,
which is very useful for diagnosing problems while developing.
- Migrate your database to create all the tables the project needs.
    ```
    python manage.py migrate
    ```
- Create a superuser account so you can log into the Django admin. This command
will prompt your for an email address, username, and password.
    ```
    python manage.py createsuperuser
    ```
- Run Django's local development server.
    ```
    python manage.py runserver
    ```
The project should now be running.  You can browse to the admin at
http://localhost:8000/admin and log in using the credentials you created with
the `createsuperuser` command.  If you can log in and see the Django admin
interface, and use it to create, edit, or delete database records, you've set
up the project correctly.

Now you're ready to begin making changes!

## Select or Submit an Issue ##
Review the current Issues for [novice](
https://github.com/pyatl/podium-django/labels/novice) issues.  Select one
you'd like to address and add a comment to let the maintainers know you're
working on it.

If you don't see an existing isssue you'd like to work on, but you've found
a bug or have an idea for a feature or enhancement, please create a new issue
first, and include a clear description of the bug or feature.

## Create a Branch ##
Now that you've selected or submitted an issue, you'll want to create a branch
to do your work on. This allows you to always keep your `master` branch as a
clean copy of the code from upstream. By always doing your work on a branch,
you can also work on multiple separate issues at once.
- Create your branch. It's recommended to give your branch a meaningful name.
    ```
    git checkout -b feature_XYZ
    ```

## Make Your Changes ##
- Edit the code or documenation as required to implement your changes.
- Include unit tests for any non-trivial functionality changes.
- Make your changes in small, logically related commits.
- Ensure your commit messages clearly explain the "why" of each change.
- Format your message according to the recommended standard pattern:
    ```
    Brief summary of changes in 50 characters or less
    <blank line>
    A longer, more detailed description of the change, if required. Keep the
    lines to 72 characters or less and explain any non-obvious techniques
    you may have used or additional context that someone might need to
    fully understand your commit.
    ```
    See the [Pro Git book](
    https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#_commit_guidelines)
    for more guidelines on git commit best practices.

## Validate and Test Your Changes ##
Once you're satisfied with your commits, you should always verify that your
changes haven't broken existing features or introduced any new bugs.
- Run the automated test suite with `python manage.py test` from the project
root.
- Run a linter like [pycodestyle](
https://pycodestyle.readthedocs.io/en/latest/) to check that your code meets
PEP8 style guidelines.
- Manually run the project and test that your changes are running and your
feature is available and working properly, or that the bugfix you added fully
corrects the bug.

## Publish Your Changes ##
Now that your changes have been made and you've tested them, you're ready to
publish the changes to Github.
- Update from upstream.  Other changes may have been made to the project while
you were working on your changes, so update your fork to the latest copy of the
repository to make your changes merge in more cleanly.
    ```
    git checkout master
    git pull --rebase upstream master
    git checkout feature_XYZ
    git rebase master
    ```
    NOTE: When you rebase from master, it's possible you might have a conflict
    with a change someone else made. Follow the guidelines [here](
    https://help.github.com/articles/resolving-merge-conflicts-after-a-git-rebase/) if you need
    help resolving a conflict.
- Push your local branch to your fork.
    ```
    git push origin HEAD
    ```
    This will create a new branch on Github if you havne't pushed this branch
    before, or update your existing branch if you pushed some commits previously.

## Send Your Pull Request ##
Now that your branch with your modifications has been pushed up to Github,
you're ready to send your changes back to the original repository for the
maintainers to review and eventually merge into the project.
- Log in to Github and go to your forked repository.
- Click "Branches" and find the branch you just pushed up (sometimes there is
a notification and easy link to new branches on the front page of your
repository).
- From the Branch list page or when viewing the branch's code, click
"New Pull Request" to create a pull request.
- Enter a descriptive comment summarizing all the changes.
- Specifically mention the issue your pull request applies to in your
description (ie "Fixes issue #25" or "Closes #12"). By using the pound (#) and
the issue number, Github will automatically link your pull request to the
issue for easy tracking.

That's it, you've submitted your first pull request to the project.  Now you
just have to wait for a maintainer to review your pull request and merge it
into the master branch.  Remember to be patient - the maintainers are all
volunteers on the project, and have to juggle the time reviewing pull requests
with work obligations, family life, and other hobbies.

## Correct Issues on Your Pull Request ##
You should always try to be thorough in your own checks before you submit a
pull request, but sometimes you may inadvertently leave something out. At
other times, a maintainer more experienced on the project may have some
suggestions for modifications to your pull request. Don't be discouraged! The
best way to learn how to be a good open source contributor is to get feedback
and guidance from the project maintainers.

If a maintainer reviews your pull request and asks for changes before accepting
it, follow these steps to correct and update your pull request:
- Carefully read the maintainers instructions on what should be modified. If
you don't completely understand the request, feel free to ask questions by
adding comments on the Pull Request page.
- Make your changes locally on the same branch you did your original work on.
This allows you to update the existing pull request rather than creating a
new one.
- It's recommended that you don't add more commits just to correct a small
issue with one of your existing commits (for example, code style issues,
spelling mistakes, better commit messages).  Instead, you can use some of git's
powerful features to modify the commits.
    - If you just need to modify the last commit, use `git commit --amend`
    - If you need to modify more than one commit, use `git rebase --interactive
master`
    - If you use either of the commands above to modify a commit, git actually
creates a brand new commit.  This means that you'll need to use the --force
option to push to your branch on Github, since you've essentially "rewritten
history".  These features should only be used to "clean up" work that you've
done locally or to correct pull requests before they are accepted. Don't
amend or rebase commits that have already been merged into the main project.
        ```
        git push --force origin HEAD
        ```
- If you must add new commits (for instance, to add more unit tests), just
push the work as you did in the "Publish Your Changes" section above.
    ```
    git push origin HEAD
    ```
- Once you push the modifications to your branch, Github will automatically
update your pull request for you (it may take a few seconds).  You don't need
to take any further actions.
- Now you only need to wait for a maintainer to review your pull request
again. They may have further feedback for you, or they may simply approve your
changes and merge them into the project's master branch.

## Final Notes ##
Congratulations, you've just made your first contribution to the project!
Hopefully this will be the first of many. You can now take a few final steps
for your contribution.
- Change back to your master branch with `git checkout master`
- The next time you update your master branch with `git pull --rebase upstream
master` you should now see your changes incorporated.
- Now that your changes are part of the project, you can delete the local
branch where you did your work, and that same branch on Github if you like.
There's no real downside to leaving them there, so if you'd prefer not to
remove them that's fine too.
