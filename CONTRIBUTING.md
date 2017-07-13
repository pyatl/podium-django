# CONTRIBUTING #

Podium is meant to be a beginner-friendly project to easily allow new
contributors to jump right in and get their hands dirty.  If you have problems
with getting set up or running the project please [submit an issue](
https://github.com/pyatl/podium-django/issues).

## Basics ##
If you're fairly new to Django and haven't already done it, we highly
recommend going through the official [Django Tutorial](
https://docs.djangoproject.com/en/1.11/intro/tutorial01/) before anything else.

If you've never attempted to contribute to an open-source project on Github
before, please review Github's guides on the general Github Flow and how to
create Pull Requests.
[Github Flow](https://guides.github.com/introduction/flow/)
[Forking a project](https://guides.github.com/activities/forking/)

Once you're familiar with Django and the basic workflow, check out the issue
tracker and look for issues flagged for beginners to find something to work
on.

If you're very new to contributing to a project on Github, please refer to
our [Beginner's Guide](BEGINNERS.md)

## Documentation ##
We always welcome additional documentation that helps clarify the project,
code structure, etc.  reStructuredText is the preferred format for
documentation so that tools like Sphinx or Read The Docs can be easily
used to publish documentation. Please review your documentation for
spelling or grammar mistakes before submitting.

## Issues ##
Please [submit an issue on Github](
https://github.com/pyatl/podium-django/issues) if you find any bugs in the
 project itself or any of the developer setup steps.  Even if you are going
 to submit a Pull Request immediately to fix the issue, submitting an issue
 first helps us to track past bugs and fixes, and helps us know what we
need to review.

## Coding Guidelines ##
In order for the project to remain easy for anyone to use, run, and
contribute to, we request that any Pull Requests submitted follow a basic
set of coding guidelines.  All code submitted should:
- Conform to Python PEP8 style standards 
(https://www.python.org/dev/peps/pep-0008/).It's recommended to use a tool
 like [pep8] or [flake8] to automatically check your code before committing,
 if your editor doesn't do this for you.
- Conform to the Django style guidelines for Django-specific code:
(https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
- Pass all existing tests.  Just run `python manage.py test` before committing.
- Add tests if it adds features, removes features, or fixes a bug.  It's
 especially nice to have tests that validate that a reported bug has been fixed.
- Be submitted in small, concise commits.  This makes it much easier for
 maintainers to review your code more quickly and thus get your contributions
merged more quickly.
- Have meaningful, well-formatted commit messages.  This blog post provides
a great guide to commit messages: (https://chris.beams.io/posts/git-commit/)

While these guidelines may seem strict in some regards, they make it very easy
for anyone to jump into the project without having to spend time interpreting
a variety of coding styles, odd spacing, etc.


