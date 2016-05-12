# Timeline

(Looking at doing featherstones method instead of NewtonEuler Method)

Week 1 [May 23rd - May 30th]

- Create benchmarking tool to track project progress
    - The tool will run test code and simulations using both `KanesMethod` and
      `LagrangesMethod` and save the results in an SQLite database where each
      table represents a different test
    - In addition to the speed results, each row in the table will include
      information on who ran the tests (probably see if I can access Github
      username for this),what version of python was used, what operating system
      was used and the hardware details of the computer used (CPU speed and
      RAM)
    - A profile of portions of the tested code will be saved in a subfolder
    - A viewer of the results would be made using the matplotlib library
        - Sub options for viewing results will be added as time allows
    - Tool will be made such that it is easily extendable
        - Can be used by other members of the community for their projects
        - Can be used with the `NewtonEuler` class that will be created later
          in the project
    - __PR__: Resulting tool could be introduced as a pull request depending on
      whether or not this is desired in the main code base

- Learn and practice Kane's method of generating equations of motion so that I
  will have a better understanding of how the code works

- Note: The items listed for week 1 would begin at the beginning of May much
  before the project officially begins

Week 2, 3 [May 30th - June 13th]

- Begin going through internals of the `KanesMethod` and `LagrangesMethod` to
  determine what the commonalities are that could be drawn from a base class

- Create a basic implementation of the base class from which `KanesMethod` and
  `LagrangesMethod` would be subclasses

Week 4, 5 [June 13th - June 27th]

- Continue working out and condensing code to complete the base class for the
  equations of motion generators
    - Keeping attention to enhancing speed and performance of code during
      consolidation

- Develop the supporting documentation for the base equations of motion
  generation class

- Complete the midterm evaluation with the functioning base class, test code
  for the base class and the supporting documentation as the deliverable
    - __PR__: Base class code, test code for the base class and documentation
      for the base class

Week 6, 7 [June 27th - July 11th]

- Look into best practices for coding a `NewtonEulerMethod` class and begin
  creation of that class. This will be a general design period and as the
  desired API is developed. Test code will be written to verify the agreed upon
  API.

Week 8, 9 [July 11th - July 25th]

- Complete `NewtonEulerMethod` class

- Update the documentation explaining the new method

- __PR__: `NewtonEulerMethod` class code, test code and documentation

Week 10 - 13 [July 25th - August 23rd]

- Finish any documentation or code that is still needing to be completed

- Continue to refactor and improve the quality of the code written for the
  project

- By this point a complete understanding of the code underlying the methods
  should be obtained and thus effort towards performance enhancement and speed
  would return the greatest results

- Make final preparations for the final evaluation
    - Final deliverables would include
        - Equations of motion generator base class
        - Newton-Euler equations of motion generator class
        - Benchmarking results
    - __PR__: Any remaining items, code, documentation fixes etc.
