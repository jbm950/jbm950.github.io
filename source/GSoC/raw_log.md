### This is a raw work log and not meant to be a detailed overview of progress

(Weeks start on Sundays)

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
