# Work Product

## Benchmarking

The first item for my project was to create benchmarking tools to measure the
progress of later speed enhancements. I first made my own tool but switched to
an existing sympy tool when I learned of its existance. The PR containing my
custom tool was then closed. The benchmarks were added in PR #27 listed below.
The benchmarks currently run fine and are in a state where additional tests can
be added to test more complex variations of `KanesMethod` and
`LagrangesMethod`'s use.

- (Closed) Mechanics Benchmarking <a
  href="https://github.com/sympy/sympy/pull/11154" target="_blank">PR #11154</a>
- (Merged) Added a test for KanesMethod and LagrangesMethod <a
  href="https://github.com/sympy/sympy_benchmarks/pull/27" target="_blank">PR
  #27</a>
- (Merged) Fixed kane benchmark for different input order <a
  href="https://github.com/sympy/sympy_benchmarks/pull/29" target="_blank">PR
  #29</a>
- (Merged) Pydy models migration <a
  href="https://github.com/sympy/sympy/pull/11168" target="_blank">PR #11168</a>

## SymbolicSystem

I began the discussion for a base class for the equations of motion generators
on a PR in sympy. In this PR we started to narrow down what the final class
should accomplish. In trying to figure out the need that the final result would
fill though it became apparent that examples of use of the final result would
be needed and these examples would be better suited for the Pydy repository,
thus a new PR for discussion was created there. In writing out examples the API
for a final result came together. It was decided that a class to make the
equations of motion generators more uniform (thus easing the addition of new
generators) would be better off as a container object for the equations of
motion and other important aspects of rigid body dynamic systems. This way the
output of the equations of motion generators would be consistent and so code
that is written to handle the output of one generator can also handle the
output of other generators. The final result was the `SymbolicSystem` class and
is currently merged into the Sympy repository. The PR in the Pydy repository
remains open because it contains examples of future uses of `SymbolicSystem`
and thus is not ready to be merged but should not be closed either as the
examples could be added after `SymbolicSystem` and pydy.system.System have been
expanded upon.

The `SymbolicSystem` class is complete as far as the scope of the summer
project is concerned but there are still some steps to fully integrate it into
a normal workflow. First step would be to get `KanesMethod` and
`LagrangesMethod` to have a method that produces the `SymbolicSystem` instance
with as much information as the \*Method class contains. Once both equations of
motion generators have the ability to produce `SymbolicSystem` objects, the
pydy.system.System class needs to be rewritten to accept `SymbolicSystem`
objects instead of `KanesMethod` objects. These steps would go a long ways in
getting the new class introduced into a standard workflow.

- (Open) [WIP] Created a basis on which to discuss EOM class <a
  href="https://github.com/pydy/pydy/pull/353" target="_blank">PR #353</a>
- (Closed) [WIP] EOMBase class development <a
  href="https://github.com/sympy/sympy/pull/11182" target="_blank">PR #11182</a>
- (Merged) Added system.py to physics/mechanics <a
  href="https://github.com/sympy/sympy/pull/11431" target="_blank">PR #11431</a>

## Featherstone's Method

In working on implementing Featherstone's method in Sympy, it became apparent
that a body/joint implementation would be needed. There was some work on this
front from a previous Google Summer of Code student, but the work was
incomplete and was not merged. I decided to work on finishing his implentation
but reduce its scope to two joints (revolute and prismatic). In beginning work
on this though I found that his implementation does not quite fit the joint
internals I would need and so I ended up rewriting the joint code. This code is
written but the test code is incomplete. From the test code that is complete,
however, it seems like there are possibly some errors in the code that will
need to be fixed. Once the tests are able to run correctly, the joint code will
probably need to be cleaned to be made presentable and the docstrings will need
to be rewritten to reflect the changes that have been made. The current state
of the joint code can be found in the FeatherstonesMethod PR.

In addition to the joint code, Featherstone's Method also required some
proceesing fucntions for spatial vectors. Code for this has been written and
put in a spatial vector PR. This code is currently awaiting the review process.

Once the joint code is fixed up, the tests finished and is merged along with
the spatial vector code, work on finishing Featherstone's method can begin.
Currently the FeathsertonesMethod code runs without producing errors. Now what
needs to happen is a basic example needs to be done by hand so that test code
can be created for the class. Once the test code has been written,
FeatherstonesMethod code should be fixed where needed and overall cleaned up.
Last the documentation and docstrings should be written to reflect the final
result of the equation of motion generator.

- (Closed) [WIP] Featherstones EOM support <a
  href="https://github.com/sympy/sympy/pull/11331" target="_blank">PR #11331</a>
- (Open) [WIP] FeatherstonesMethod <a
  href="https://github.com/sympy/sympy/pull/11415" target="_blank">PR #11415</a>
- (Merged) Docstring cleanup of physics/mechanics/body.py <a
  href="https://github.com/sympy/sympy/pull/11416" target="_blank">PR #11416</a>
- (Merged) Fixed an error in frame.py <a
  href="https://github.com/sympy/sympy/pull/11504" target="_blank">PR #11504</a>
- (Open) [WIP] Spatial vector functions <a
  href="https://github.com/sympy/sympy/pull/11520" target="_blank">PR #11520</a>

## List of all PR's

This is a list of all PR's that I have interacted with over the summer and will
repeat PR's mentioned above for the different portions of the project.

### Pydy PR's

- (Merged) Examples README typo <a
  href="https://github.com/pydy/pydy/pull/349" target="_blank">PR #349</a>
- (Merged) Pendulum example added <a
  href="https://github.com/pydy/pydy/pull/351" target="_blank">PR #351</a> 
- (Open) [WIP] Created a basis on which to discuss EOM class <a
  href="https://github.com/pydy/pydy/pull/353" target="_blank">PR #353</a>
- (Open) Added a depencency on older version of ipywidgets <a
  href="https://github.com/pydy/pydy-tutorial-human-standing/pull/100"
  target="_blank">PR #100</a>

### Sympy PR's

- (Closed) Mechanics Benchmarking <a
  href="https://github.com/sympy/sympy/pull/11154" target="_blank">PR #11154</a>
- (Merged) Pydy models migration <a
  href="https://github.com/sympy/sympy/pull/11168" target="_blank">PR #11168</a>
- (Merged) Physics documentation <a
  href="https://github.com/sympy/sympy/pull/11117" target="_blank">PR #11117</a>
- (Closed) [WIP] EOMBase class development <a
  href="https://github.com/sympy/sympy/pull/11182" target="_blank">PR #11182</a>
- (Merged) Minor fix in KanesMethod's docstring <a
  href="https://github.com/sympy/sympy/pull/11186" target="_blank">PR #11186</a>
- (Merged) Added support for a bodies attribute to LagrangesMethod <a
  href="https://github.com/sympy/sympy/pull/11263" target="_blank">PR #11263</a>
- (Closed) [WIP] Featherstones EOM support <a
  href="https://github.com/sympy/sympy/pull/11331" target="_blank">PR #11331</a>
- (Merged) Docstring cleanup of physics/mechanics/body.py <a
  href="https://github.com/sympy/sympy/pull/11416" target="_blank">PR #11416</a>
- (Merged) Added system.py to physics/mechanics <a
  href="https://github.com/sympy/sympy/pull/11431" target="_blank">PR #11431</a>
- (Open) [WIP] FeatherstonesMethod <a
  href="https://github.com/sympy/sympy/pull/11415" target="_blank">PR #11415</a>
- (Merged) Fixed an error in frame.py <a
  href="https://github.com/sympy/sympy/pull/11504" target="_blank">PR #11504</a>
- (Open) [WIP] Spatial vector functions <a
  href="https://github.com/sympy/sympy/pull/11520" target="_blank">PR #11520</a>

### Sympy Benchmarking PR's

- (Merged) Added a test for KanesMethod and LagrangesMethod <a
  href="https://github.com/sympy/sympy_benchmarks/pull/27" target="_blank">PR
  #27</a>
- (Merged) Fixed kane benchmark for different input order <a
  href="https://github.com/sympy/sympy_benchmarks/pull/29" target="_blank">PR
  #29</a>


### PR's Reviewed

- (Open) Fix matrix rank with complicated elements <a
  href="https://github.com/sympy/sympy/pull/10650" target="_blank">PR #10650</a>
- (Open) Improved the explanation of the 5 equations in the Kane's Method
  docs <a href="https://github.com/sympy/sympy/pull/11183" target="_blank">PR
  #11183</a>
- (Closed) Remove documented redundant comments <a
  href="https://github.com/sympy/sympy/pull/10698" target="_blank">PR #10698</a>
- (Open) Docmentation comments corrections <a
  href="https://github.com/sympy/sympy/pull/10693" target="_blank">PR #10693</a>
- (Merged) Fix issue #8193 <a
  href="https://github.com/sympy/sympy/pull/11209" target="_blank">PR #11209</a>
- (Open) Blacklisted pygletplot from doctests when pyglet is
  installed <a href="https://github.com/sympy/sympy/pull/10856"
  target="_blank">PR #10856</a>
- (Merged) Fix multiarray import error on appveyor <a
  href="https://github.com/pydy/pydy/pull/354" target="_blank">PR #354</a>
- (Merged) Added docstrings to ast.py <a
  href="https://github.com/sympy/sympy/pull/11333" target="_blank">PR #11333</a>
- (Merged) Speeds up the linear system solve in KanesMethod.rhs() <a
  href="https://github.com/sympy/sympy/pull/10965" target="_blank">PR #10965</a>
- (Merged) Added docstrings to delta and mid property methods <a
  href="https://github.com/sympy/sympy/pull/11432" target="_blank">PR #11432</a>
- (Merged) Added top-level docstring for singularities.py <a
  href="https://github.com/sympy/sympy/pull/11440" target="_blank">PR #11440</a>
- (Merged) Intendation fixes -- sympy/concrete/summations.py<a
  href="https://github.com/sympy/sympy/pull/11473" target="_blank">PR #11473</a> 
- (Open) Adjustments to Legendre, Jacobi symbols docstrings <a
  href="https://github.com/sympy/sympy/pull/11474" target="_blank">PR #11474</a>
- (Open) Added docstring to jordan_cell method <a
  href="https://github.com/sympy/sympy/pull/10356" target="_blank">PR #10356</a>
