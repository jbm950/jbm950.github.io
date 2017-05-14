# Beginning Open Source Programming

This guide is primarily focused on beginning contributions to Python open
source projects because that is where I have experience.

# Git/Github

Github is one of the most common places to find open source repositories and one
of the easiest ways to contribute. As such this is the first step to learn
towards open source programming contributions. Below is a series of two videos,
the first describes how to use git the tool and the second describes how to
interact with Github the site.

1. [Github YouTube Tutorial](https://www.youtube.com/watch?v=0fKg7e37bQE)
1. [Github YouTube Tutorial 2](https://www.youtube.com/watch?v=oFYyTZwMyAg)

# Obtain Git

If your machine does not yet have git, it is easy to acquire. On windows follow
this [guide](https://git-scm.com/downloads). On mac or linux, if you try to use
a git command before git is installed, your system will suggest a command that
you can use to acquire git.

# Git SSH Keys

In order to be able to push and pull to your repositories without having to
enter your password every time you need to set up ssh keys with github. Github
has a useful
[guide](https://help.github.com/articles/connecting-to-github-with-ssh/) for
setting up ssh keys. Once you have ssh set up make sure you use the ssh link
for your `git clone` statement.

# Find a project to which you'd like to contribute

Choose a topic you like or something that is meaningful to you. You'll be more
likely to stick with it and you'll learn more. Once you find a project clone it
to your local machine and use the `python setup.py develop`. By using the
`develop` option instead of `install` your python instance will use the git
repo version of the code rather than copying it internally. This means as you
work in the git repository you do not have to reinstall the code to see the
changes take effect.

> _Note:_ If `setup.py develop` is not working it may be that setup.py is using
> distutils instead of setuptools. You can try just changing them in the import
> statement to get it to work.

# First Contributions

When you find your project the first steps will be to read through the
documentation to familiarize yourself with their contribution process, any
standards they use and generally how the code works. I would recommend writing
down any and all spelling and gramatical errors you find while reading. When
you finish reading you can go in and create a pull request to fix all of the
errors you have found. This is a great way to make a first contribution, meet
your fellow contributors and get your feet wet with the contribution process.

# Common Open Source Tools

## PEP8

Python Enhancement Proposal 8
([PEP8](https://www.python.org/dev/peps/pep-0008/)) is a common style guide
across open source projects as it is the one endorsed by Python Software
Foundation itself. If the project you've found does not use a style guide it
would be a good idea to bring this one to their attention. Otherwise use the
exact same style guide that the project uses.

## TravisCI

[TravisCI](https://travis-ci.org/) is a tool that runs a project's tests with
every commit in a PR. This allows members to know that the new code will not
break functionality without having to go through the process of acquiring the
new code and running the tests manually.

## Sphinx

[Sphinx](http://www.sphinx-doc.org/en/stable/) is a documentation tool commonly
used by Python projects. A big reason for this is that is can pull
documentation directly from the code itself. This allows projects to only have
to maintain the code in the docstrings of the classes/functions and still have
good documentation.

The standard formatting for sphinx can lead to docstrings that are not very
readable unrendered and so some extensions have been developed to allow
readable docstrings. The two common extensions are
[numpydoc](https://github.com/numpy/numpydoc/) and
[Napoleon](http://www.sphinx-doc.org/en/stable/ext/napoleon.html). Napoleon is
included with sphinx and numpydoc needs to be installed separately. To get
sphinx to use them you need to add "numpydoc" or "sphinx.ext.napoleon" to the
extensions list in your conf.py file.

## ReadTheDocs

[ReadTheDocs](https://readthedocs.org/) is a site that will host open source
projects documentation for free. Also important is that ReadTheDocs will
integrate with sphinx and automatically update the documentation every time a
pull request is merged.

## Test Code (Python)

This test code
[guide](http://python-guide-pt-br.readthedocs.io/en/latest/writing/tests/) goes
over many different tools that can be used in python to facilitate test code
writing.

## Airspeed Velocity

[Airspeed Velocity](http://asv.readthedocs.io/en/latest/using.html) is a tool
that is used to write benchmark tests. If a project is dealing with
optimization of their code this is a useful tool to turn to.
