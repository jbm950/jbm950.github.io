### This is a raw work log and not meant to be a detailed overview of progress

(Weeks start on Sundays)

<hr>

## Week 5

### 6/24/2016

- Responded to [PR #354](https://github.com/pydy/pydy/pull/354) where I was
  referenced directly
    - Fixes a spot where an external dependency within conda needed to be
      delcared for the testing environment
- Researched doctests plotting errors and reported findings on [Issue
  #10855](https://github.com/sympy/sympy/issues/10855)
- Continued reading Featherstone's Book (pg 140)

### 6/23/2016

- Continued reading Featherstone's Book (pg 119)
- Tried looking into [PR #10856](https://github.com/sympy/sympy/pull/10856) and
  its associated [Issue #10855](https://github.com/sympy/sympy/issues/10855)
    - Tries to remove tests but when I run locally the tests are not included
      anyways?
        - I dont have pyglet installed so the tests were probably skipped

### 6/22/2016

- Continued reading Featherstone's Book (pg 99)

### 6/21/2016

- Altered the information in pydy-tutorial-human-standing to show a dependence
  on on older version of a specific package
    - Pushed changes in [PR
      #100](https://github.com/pydy/pydy-tutorial-human-standing/pull/100)
- Continued reading Featherstone's Book (pg 78)
- Made a branch for an overhaul of `LagrangesMethod` in SymPy
- Began taking inventory of the changes that [PR
  #11183](https://github.com/sympy/sympy/pull/11183) so I can mirror changes
  for `LagrangesMethod`

### 6/20/2016

- Continued reading Featherstone's Book (pg 69)
- Added a bodies attribute to `LagrangesMethod`
    - Pushed changes in [PR #11263](https://github.com/sympy/sympy/pull/11263)
    - Effort to create identical API between `KanesMethod` and `LagrangesMethod`

<hr>

## Week 4

### 6/17/2016

- Did a more in depth review of new changes to [PR
  #11183](https://github.com/sympy/sympy/pull/11183#issuecomment-225102295)
- Continued reading Featherstone's Book (pg 48)
- Wrote weekly blog post

### 6/16/2016

- Began looking into reviewing [PR
  #11209](https://github.com/sympy/sympy/pull/11209)
    - Did not see any outright errors in the code changes. I know so little of
      how it works though. Biggest change I tried to determine if it was
      necessary is the indentation change but in the end I believe that the
      change is correct.
    - Said it looks good to me and someone else merged it, makes me nervous
      that poeple over estimate my opinion
    - Makes me believe that the code base can use significantly more commenting
- Continued reading Featherstone's Book (pg 31)
- Began a review of new changes to [PR
  #11183](https://github.com/sympy/sympy/pull/11183#issuecomment-225102295)

### 6/15/2016

- Fixed a spot in the examples in [PR
  #353](https://github.com/pydy/pydy/pull/353) where the desired output hadn't
  been changed to match the fact that potential energy was added to
  `output_eqns`.
- Looked for more examples on equations of motion forms
    - Most are focused solely on kinematics
    - Finding a lot that deal with solving for the equations of motion but make
      no attempt to describe different forms for the equations
- Worked on determining what attributes and methods `EOM` should have and
  figured out what wasn't currently represented in the example code
- Added every attribute/method that is planned for eombase.EOM to the example
  code
- Added several error examples to the eombase.EOM example documentation
- Began reading through Featherstone's Book (pg 10)

### 6/14/2016

- Looking for a way to run the kane benchmark on older versions of sympy
    - Decided to a try/except clause
- Continued changing the code eombase examples in pydy to documentation format
- Put a reminder that the tests passed for [PR
  #11186](https://github.com/sympy/sympy/pull/11186) Minor fix in  KanesMethod's
  docstring
- Addressed review comments on [PR #353](https://github.com/pydy/pydy/pull/353)
  by making changes in the examples documentation.
- Continued adding to dynamics notes on equations of motion forms
    - Searched for more places that specify forms for the equations of motion
    - Mentioned progress on base class PR

### 6/13/2016

- Started putting together an example of a pendulum using x, y coordinates and
  manually input eom into `eombase`
- Made some changes to the two mass spring damper example changing the api of
  eombase
- Looking for different distinctions of equations of motion forms
    - Added some notes to the dyamics page
- Looked into how pydy.system works and what sort of things it returns
- Responded to Jason's comments/questions on [PR
  #353](https://github.com/pydy/pydy/pull/353)
    - Had to research in pydy and sympy some in order to provide well reasoned
      responses
- Moving all three examples to a single .rst page where input/output can be
  more easily displayed
- Have to alter the kane benchmark I wrote to account for the fact that the api
  was changed for the kanes_equations(...) call

<hr>

## Week 3

### 6/10/2016

- Began reading through latest changes to [PR
  #11183](https://github.com/sympy/sympy/pull/11183#issuecomment-225102295)
    - Performed a code review of the latest commit's changes to kane.py
- Altered code in [PR #353](https://github.com/pydy/pydy/pull/353) to show
  different methods of entering the equations of motion
    - Added input demonstrations for the different forms accepted by
      ODEFunctionGenerator in PyDy
    - Added ability to give the EOM object additional equations such as kinetic
      energy, auxiliary equations, etc.
    - Looked into combining coordinates and speeds into a single vector states
      and the effect that would have on pydy.system.System
- Discussion over `rhs` as a variable and the possible confusion it creates in
  [PR #353](https://github.com/pydy/pydy/pull/353)

### 6/9/2016

- Diving into how KanesMethod is accessed by pydy.system.System
- Started work on a two mass spring damper system to provide an example for the
  api for the project
    - Solved the equation of motion and put in M * udot = F form by hand
    - Coded up the example
    - Created a [PR #353](https://github.com/pydy/pydy/pull/353)
    - Created a .svg drawing to go along with the example
- Commented/reviewed [PR #10698](https://github.com/sympy/sympy/pull/10698)
  about removing documentation the user view as redundant
    - Sartaj Singh agreed with me that the change wasn't useful and closed the
      PR
- Commented/reviewed [PR #10693](https://github.com/sympy/sympy/pull/10693)
  about fixing documentation spelling/grammar

### 6/8/2016

- Working through [Planar Pendulum
  Example](http://nbviewer.jupyter.org/github/bmcage/odes/blob/master/docs/ipython/Planar%20Pendulum%20as%20DAE.ipynb)
    - Arranged equations into the equation form shown on [Lagrange Docs 3
      equations](http://docs.sympy.org/latest/modules/physics/mechanics/lagrange.html)
      and into mass matrix/forcing vector form and mass matrix full/forcing
      vector full form
    - Made an outline of the things that are actually done in the tutorial
    - Determined that the equations of motion are only used for the residual
      function for the dae object
        - DAE object found in scikits.odes
- Looked over [Double Pendulum
  Example](http://www.pydy.org/examples/double_pendulum.html) in PyDy
    - The code shown in the documentation does not appear to be code found
      anywhere in PyDy
- Looked up
  [IDA](http://www.scholarpedia.org/article/Sundials_equation_solvers) software
  for solving DAE's
    - Is part of Sundials equation solvers suite
- Looked over [Dynamics with
  Python](http://www.moorepants.info/blog/npendulum.html) article written by
  Jason to get more ideas on the use of the generated equations of motion
    - Arranges the equations of motion such that odeint can solve the time
      simulation
        - odeint is found in SciPy
- Read documentation on
  [scipy.integrate.odeint](http://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html#scipy.integrate.odeint)
    - Uses xdot = f(x, t) as input (right hand side)
- Read documentation on [scikit.odes.dae](https://github.com/bmcage/odes)
    - Uses 0 = xdot - f(x, t) as input (residual)
- Looked through [PyDy Mass Spring Damper
  Example](http://nbviewer.jupyter.org/github/pydy/pydy/blob/master/examples/mass_spring_damper/mass_spring_damper.ipynb)
    - System class seems to handle the backend for formatting equations of
      motion for integrators and changing from symbolics to numerics
- Started going through pydy.system.System and disceting its internals
    - Made lists of all attributes, properties and non-property methods of the
      class
    - Found all times eom_method is used in the code and what attributes are
      being accessed

### 6/7/2016

- Worked on migrating the rest of the @properties from ~Methods into the base
  class
- Added a method to the base class to check if the equations of motion have
  been generated yet
- Made a pull request for the property migration, [PR
  #11182](https://github.com/sympy/sympy/pull/11182) (Change from base class
  development)
    - Read through Jason's comments on this PR
    - Replied suggesting a meeting tomorrow morning and moving the discussion
      to a wiki page
- Looked up differences between ODE and ADE
- Read through [Planar Pendulum
  Example](http://nbviewer.jupyter.org/github/bmcage/odes/blob/master/docs/ipython/Planar%20Pendulum%20as%20DAE.ipynb)
  which demonstrates a problem from equations of motion generation to
  simulation/visualization
- Looked up difference between DAE's and ODE's and added the findings to a new
  notes page on website

### 6/6/2016

- Cleaned up the test code for test_eombase.py
- Finished reading
  [pydy-tutorial-human-standing](https://github.com/pydy/pydy-tutorial-human-standing)
- Read through updated changes to [PR
  #11183](https://github.com/sympy/sympy/pull/11183) (Jason's addition to Kanes
  method documentation)
- Created [Issue #11199](https://github.com/sympy/sympy/issues/11199)
  mentioning how in the code base the old linearizer was scheduled to be
  deprecated in version 1.0  but it is still present
- Planning and working on ideas for base class implementation

<hr>

## Week 2

### 6/3/2016

- Worked on solidifying the eom test code such that it will actually run and is
  no longer entirely pseudo code
- Worked on filling out the eom code
- Asked for opinions on inputting the dynamical and kinematical diff eqs into
  EOM
- Wrote weekly blog post
- Modified test code and pushed changes to the SymPy PR
- Started reading
  [pydy-tutorial-human-standing](https://github.com/pydy/pydy-tutorial-human-standing)

### 6/2/2016

- Looked over mass_matrix and forcing methods in both KanesMethod and Lagranges
  Method
- Created a mock up of an equations of motion class
- Read through some of https://en.wikipedia.org/wiki/Nonholonomic_system
- Watched [Constraints and generalized
  coordinates](https://www.youtube.com/watch?v=4RiRAIelAAQ)
    - Less helpful
- Watched [Nonholonomic constraints in Lagrangian mechanics by Prof Anindya
  Chatterjee](https://www.youtube.com/watch?v=fx4esbHWkkk)
    - Rather helpful
- Posted a question asking for clarification to the google groups forum
- Pushed my changes and mock up of an equations of motion class to the [PR
  #11182](https://github.com/sympy/sympy/pull/11182)

### 6/1/2016

- Responded to Jason's question on [PR
  #11117](https://github.com/sympy/sympy/pull/11117) (physics documentation
  fixes)
    - Jason Merged the PR
- Read through Jason's comments on [PR
  #11182](https://github.com/sympy/sympy/pull/11182) (the base equations of
  motion PR/discussion)
    - Replied requesting some decisions and clarifications
- Read through Jasons comments on my question to the google groups forum
- Reviewed [PR #11183](https://github.com/sympy/sympy/pull/11183) where Jason
  added descriptions of the equations mentioned in Kane's documentation
- Read through [PR #345](https://github.com/pydy/pydy/pull/345) in the pydy
  repository where there was a discussion about a base class for the Method
  classes
- Minor fix to KanesMethod docstring, created [PR
  #11186](https://github.com/sympy/sympy/pull/11186#issuecomment-223080554)


### 5/31/2016

- Finished reading [A Beginners Guide to 6-D Vectors (Part
  2)](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5663690)
- Read through "Linearization in Physics/Mechanics" in sympy documentation
- Read through "Potential Issues/Advanced Topics/Future Features in
  Physics/Mechanics" in sympy documentation
- Read through "A rolling disc, with Kane’s method" in sympy documentation
- Read through "A rolling disc, with Kane’s method and constraint forces" in
  sympy documentation
- Read through "A rolling disc using Lagrange’s Method" in sympy documentation
- Read through "A bicycle" in sympy documentation
- Read through "Nonminimal Coordinates Pendulum" in sympy documentation
- Made a branch for EOMBase creation and made a file to hold the code and the
  test code
- Moved and fixed the examples from orient to orient new docstring for [PR
  #11117](https://github.com/sympy/sympy/pull/11117)
    - Asked for some clarification about some of the physics documentation
    - Removed a redundant section from physics/advanced.rst
    - Removed colons from physics/masses.rst in the hopes that it fixes the
      problem of code syntax highlighting and SymPy Live compatibility
    - Responded to Jason's Comments
    - Reverted the colon commit
- Wrote some pseudo-code for test_eombase.py
- Opened an [Issue #96](https://github.com/sympy/sympy-live/issues/96) in the
  sympy live repository over syntax highlighting and SymPy Live's ability to
  run
- Created a [PR #11182](https://github.com/sympy/sympy/pull/11182) to discuss
  the development of the EOm base class
- Asked some terminology questions on the sympy google groups forum

### 5/30/2016

- Changed the tests in sympy/physics/mechanics/tests/test_models.py so that
  mass matrices and forcing vectors were used for comparison in order to cut
  down run time
    - [PR #11168](https://github.com/sympy/sympy/pull/11168) was merged and
      closed by Jason
- Continued research of Kanes and Lagranges method classes
- Read through "Kane’s Method in Physics/Mechanics" in sympy documentation
- Skimmed through "Masses, Inertias, Particles and Rigid Bodies in
  Physics/Mechanics" in sympy documentation
- Read through "Lagrange’s Method in Physics/Mechanics" in sympy documentation

<hr>

## Week 1

### 5/27/2016

- Fixed a docstring issue in models.py where it stated that the retun value was
  a pydy.system.System object which I had changed
- Changed the theta location in models.py's n_link_pendulum_on_cart() function
  in the sympy repository
    - Had to change initial work such that theta would represent a counter
      clockwise rotation as positive
    - Updated the drawing in the docstring to indicate the new location of theta
- Cleaning up the tests so that there are no more extremely long lines and the
  tests check simplify(sym_expr - expected) == Matrix(0's)
- Refreshed knowledged by reading though python book on @property decorators
- Continued research of KanesMethod and LagrangesMethod
- [PR #27](https://github.com/sympy/sympy_benchmarks/pull/27) in
  sympy_benchmarks was merged and closed by Jason

### 5/26/2016

- Ran the sympy_benchmarks using asv, published and previewed again to see if
  it would produce a second data point or if additional data points are
  collected by specifying more commits to test in the config
    - Added a second data point
- Added a mass spring damper test to the lagrange benchmarking code and
  commented it
- Renamed existing kanesmethod and lagrangesmethod benchmarking classes to
  reflect the dynamics situation they test
- Altered the README.rst of sympy_benchmarks to reflect a desire to mirror
  SymPy's directory tree
- Left a request for a determination of the desired scope of my benchmarking
  pull request
- Moved pydy.models to sympy/physics/mechanics
    - Changed the return statements to just return the KanesMethod object
    - Altered the code to reflect the new argument order for .kanes_equations()
- Asked about why the documentation online does not reflect the changes that
  were made to the source code in [Issue
  #10945](https://github.com/sympy/sympy/blob/master/sympy/physics/mechanics/kane.py)
- Addressed Jason's review comments in [PR
  #27](https://github.com/sympy/sympy_benchmarks/pull/27) in the
  sympy_benchmarking repository
- Created tests for the new sympy.physics.mechanics.models.py
- Created a [PR #11168](https://github.com/sympy/sympy/pull/11168) for the
  migration of the models code from PyDy to SymPy
- Mentioned other members of SymPy to look at [PR
  #10650](https://github.com/sympy/sympy/pull/10650) that I had done a review
  of yesterday. These members had been active in another pull request that was
  attempting to fix the same issue
- Took notes on Dynamics topics and generally spent time learning how the code
  works

### 5/25/2016

- Reviewed Jason's comments on my benchmarking pull requests ([PR
  #11154](https://github.com/sympy/sympy/pull/11154) in the sympy repository
  and [PR #27](https://github.com/sympy/sympy_benchmarks/pull/27) in
  sympy_benchmarks repository)
- Looked over pydy.models code for use of KanesMethod interface
- Looked over pydy rolling disk example PR code for use of KanesMethod interface
- Looked over pydy Whipple bicycle model PR code for use of KanesMethod
  interface
- Looked over sympy test_kane3.py for use of KanesMethod interface
- Looked at `KanesMethod` to see what methods were not used in the above four
  locations
- Summarized findings in comments on the above mentioned bencharking pull
  requests
- Altered benchmarking code in sympy_benchmarks
    - Changed the class names for clarity
    - Moved the initialization code for the EOMMethod classes to the setup code
    - Added comments to the Kane's Method code
    - Fixed a typo in the Kane's Method code
- Did a review of [PR #10650](https://github.com/sympy/sympy/pull/10650) in the
  sympy repository
- Restructured SymPy mechanics benchmarks subdirectories to match the directory
  structure in SymPy
- Ran the sympy_benchmarks using asv, published and previewed

### 5/24/2016

- Commented and added docstings to view.py in the benchmarking code
- Added the close() for the cursor and connection to the benchmarking scripts
  that were missing it
- Created a benchmarking branch on by sympy repo and added my benchmarking code
  to it under sympy/benchmarking/mechanics
- Commited the different benchmarking files in a way such that each commit was
  related to one topic (ie. the viewer, the main script, the tests)
- Created a [PR #11154](https://github.com/sympy/sympy/pull/11154) for the
  benchmarking code
    - Jason Points out that there's already a sympy/benchmarking repository
      that uses ASV to perform benchmarking tasks
    - Responded indicating that kane_1.py and lagrange_1.py could be moved to
      `sympy/sympy_benchmarks`
- Finished reading through the slides and slide notes for Featherstone's short
  course on spatial vector algebra
- Continued reading [A Beginners Guide to 6-D Vectors (Part
  2)](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5663690)
    - Made it to "Arithmetic" on page 6
- Read through ASV (airspeed velocity) website. (Python benchmarking package)
    - Read Using Airspeed velocity page and writing benchmarks page
- Created a file for and started collecting notes for the Base class for the
  equations of motion generation methods
- Forked and cloned sympy_benchmarks
- Added kane_1 and lagrange_1 to sympy_benchmarks in mechanics_benchmarks branch
  and altered them to meet airspeed velocity's structure for benchmarking tests
- Created a [PR #27](https://github.com/sympy/sympy_benchmarks/pull/27) to add
  kane_1.py and lagrange_1.py to sympy_benchmarks repository

### 5/23/2016

- Had a brief meeting with Angadh
- Worked on adding filters to benchmarking viewer
    - Had to find the proper widget for this task
    - Figured out how to use tk.Menu
    - Found SQLite command for determining all the tables in a database
    - Got the matplotlib section of the GUI to be drawn over instead of trying
      to add additional graphs
    - Viewer can now update the graph based on switching tables and specifying
      specific python version or platform
- Changed the benchmark code for kane's method and lagrange's method
    - put the LagrangesMethod and form equations in a function (same for
      KanesMethod) and call the function from timeit rather than import the
      whole file
    - Needed to be run significantly fewer iterations to achieve the same run
      time

<hr>

## Pre-Week 3

### 5/20/2016

- Wrote a blog post summerizing what has been done during the community bonding
  period

### 5/18/2016

- Addressed Jasons comments on the simple pendulum example [PR
  #351](https://github.com/pydy/pydy/pull/351)
- Began email correspondance about the planning of weekly meetings
- Began looking up flight prices from Austin to Gainesville
    - Booked a flight
- Started work on a custom viewer for the benchmarking database using tkinter
    - Able to pull up the database, average all the data taken on a single day,
      and plot the data using matplotlib
- Started Roy Featherstones short course on spatial vector algebra
    - Made it to slide 32 in both the slides and slide notes and ended while
      working on questions A2

### 5/16/2016

- Asked for clarification about travel for scipy conference
- Watched a video on using sqlite with python
- Created a database for the benchmarking software
- Created code to run the main overhead for the benchmarking software that
  calls out individual tests
- Created a test to run Kanes Equations based on the example mass spring damper
  code in KanesMethod's docstring
- Created a test to run Lagranges Equations based on the simple pendulum
  example I added to pydy
- Fixed some errors in the physics documentation and created a [PR
  #11117](https://github.com/pydy/pydy/pull/351)
- Began Reading [A Beginners Guide to 6-D Vectors (Part
  2)](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5663690)
- Fixed my adding of RSS feed to PSF GSoC collection of blogs
    - Had accidentally made the pull request between branches of my repository
      rather than my repository and the GSoC repository

<hr>

## Pre-Week 2

### 5/13/2016

- Got pendulum example to match the hand derived results
- Drew a diagram (svg) for the pendulum example
- Created a [PR #351](https://github.com/pydy/pydy/pull/351) for the pendulum
  example in the examples folder of pydy
- Added RSS feed to PSF GSoC collection of blogs
- Started the benchmarking program

### 5/12/2016

- Worked on implementing [Basic Equation of
  Motion](../notes/analytical_dynamics/analytical_dynamics_main.html#e_basic_equation_of_motion)
  in code
    - Got it to the point where it produces an equation of motion but it is not
      matching my handwritten result
- Finished reading [A Beginners Guide to 6-D Vectors (Part
  1)](http://ieeexplore.ieee.org/xpls/icp.jsp?arnumber=5569032#article)
- Figured out how to get the run time for the testing code

### 5/11/2016

- Added a link to the timeline on my website so it was easier to access
- Worked out [Basic Equation of
  Motion](../notes/analytical_dynamics/analytical_dynamics_main.html#e_basic_equation_of_motion)
  using Langrange's Method by hand as a refresher

### 5/10/2016

- Created a [PR #349](https://github.com/pydy/pydy/pull/349) for a simple
  grammar error on the pydy example page
    - Jason merged it
- Began Reading [A Beginners Guide to 6-D Vectors (Part
  1)](http://ieeexplore.ieee.org/xpls/icp.jsp?arnumber=5569032#article)
    - Made it to the beginning of section 6
- Decided on what examples I want to do to learn the equations of motion
  generation with sympy
    - [Basic Equation of Motion](../notes/analytical_dynamics/analytical_dynamics_main.html#e_basic_equation_of_motion)
    - [Basic System of Particles](../notes/analytical_dynamics/analytical_dynamics_main.html#basic_sys_of_particles)

<hr>

## Pre-Week 1

### 5/7/2016

- Edited permissions and changed name of google drive shared folder

### 5/6/2016

- Added blog to Planet Sympy
- Added project details to GSoC-2016-Report on the wiki
- Began looking into non-holonomic constraints and adding notes to the dynamics
  page
- Participated in first meeting with mentors
- Created a folder on google drive to share documents
- Created a page for weekly meetings on website
- Wrote up notes from the meeting
