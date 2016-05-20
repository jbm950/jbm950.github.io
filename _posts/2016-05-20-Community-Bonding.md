---
layout: posts
title: Community Bonding Period
commentIssueId: 2
---

The community bonding period is coming to a close and so I'd like to write
about what I've done/learned during this time. I've had the opportunity to
create my first blog, have my first meeting with my mentors, submit a couple of
minor pull requests to pydy and sympy, add an example script to the pydy
repository, begin learning about spatial vectors and begin work on some
benchmarking code.

This is my first attempt at blogging and I had some trouble initially setting
it up. For starters I did not know what an RSS feed was or for what it was
used. Also I wanted the blog to be hosted on github pages where I currently
keep my collection of notes and thus I decided to try to use the jekyll static
site backend that github uses. I tried, however, to isolate the blog in its own
subfolder with the rest of my GSoC information but this caused all kinds of
problems with posts showing up multiple times and the RSS feed not updating
properly. I eventually decided to stop trying to separate the posts and just
centrally locate them as is demonstrated in the jekyll documentation. For the
RSS feed I used a template that I found online. Now the posts appeared properly
and the RSS feed updated correctly. The last thing I wanted to do for my blog
before I considered it officially set up was to have some method of allowing
people to comment on my posts. I found a blog post online on how to achieve
this without the need for anything other than what github pages offers and so I
set out to try this method. I used the code shown on the blog post without any
luck. Prior to this I have had zero experience working with javascript and so
I didn't even know where to begin to try to debug why the comments were not
showing up and so I sent the writer of the blog post an email asking for his
assistance. And he replied! He pointed out that I was missing the part where a
java script library would be loaded for use on the page and once I added the
couple of lines of code, commenting on my blog posts is now possible (At least I
think that's what the problem was but again I have no experience working with
javascript). With the ability to comment added, my blog is completely set up
and is connected to the correct channels for the Google Summer of Code.

Early in the community bonding period I was able to have my first meeting with
my mentors for my project. During this meeting it was discussed that I could
change the later portion of my project from working on implementing a Newton
Euler method of equations of motion generation to implementing the faster
Featherstone method. Considering I had no great attachment to the Newton Euler
method I agreed that the faster method would provide a greater benefit for the
overall project. Since the meeting I have spent some time reading on the math
involved in the Featherstone method, specifically spatial vectors and their
uses in dynamics. To this end I have read [A Beginners Guide to 6-D Vectors
(Part 1)](http://ieeexplore.ieee.org/xpls/icp.jsp?arnumber=5569032#article) and
started reading both [A Beginners Guide to 6-D Vectors (Part
2)](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5663690) and Roy
Featherstone's short course on spatial vector algebra.

I have also spent some time beginning to familiarize myself with the code that
I will be working with. To begin I followed Jason Moore's great suggestion of
coding through one of the examples from my dynamics course and adding it to the
pydy/examples folder in the pydy repository. The example I chose to use was a
[simple
pendulum](../../../notes/analytical_dynamics/analytical_dynamics_main.html#e_basic_equation_of_motion)
so that I could focus on the code rather than the complexities of the problem
itself. This code and diagram are currently undergoing the review process now
in order to be added to the pydy repository.

Lastly I have begun work on benchmarking code which is mentioned as part of my
project itself. In working on this part of the project I was able to learn how
to use a SQLite database with python which I had only obtained brief exposure
to in the past. This code currently works using python's timeit library to run
a file utilizing Lagrange's method of equations of motion generation and
another using Kane's method. The code runs each file several thousand times and
iterates through this process 30 times and saves the average of the 30 runs
along with several other useful bits of information about the computer and
version of python being used to run the tests. In addition to the benchmarking
code itself I have been working on a script that will allow viewing of a graph
of the tests utilizing matplotlib and tkinter. This code is close to completion
and the current next major addition will be to add the ability to filter the
tests based on what platform was used/what version of python was used to run
the tests.

This community bonding period has been productive and I am excited to begin the
Google Summer of Code program on Monday.
