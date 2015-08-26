__An Efficient Overloaded Method for Computing Derivatives of Mathematical
Functions in MATLAB __  
__Written by Michael A. Patterson, Matthew Weinstein and Anil Rao__  
__Published in ACM Transactions on Mathematical Software: July 2013__  
<a href="http://vdol.mae.ufl.edu/JournalPublications/TOMS-2011-0055.pdf"
target="_blank">Full Article</a>

## Table of Contents

- [Introduction](#introduction)

## Introduction {#introduction}

- Three general categories of derivative approximation techniques
    - Numerical approximation
        - In numerical approximation the derivative is approximated by finding
          the values of the function around the desired point and finding the
          slope between those values
        - Examples of this method include finite differencing and complex-step
          derivative approximation
        - Space between point in finite-differencing can cause problems because
          if the space is too big the derivative will be inaccurate and if the
          space is too small there can be catastrophic cancellation in the
          numerator
        - Complex-step derivative approximation does not suffer from
          catastrophic cancellation with extremely small perturbation sizes
          like finite differencing does
    - Symbolic differentiation
        - Symbolic differentiation is the equivalent of the computer takeing
          the equations and solving for the derivative by hand as it will use
          the actual quantities or variables
        - Not good for very large difficult problems because of possible
          expression explosion
    - Automatic differentiation
        - Computers implement functions in code by doing one elementary
          mathematical operation or function at a time and so automatic
          differentiation uses the standard differentiation rules on each
          operation.
        - Two most well known methods of automatic differentiation are forward
          and reverse mode
        - Forward are reverse mode automatic differentiation are implemented
          using either operator overloading or source transformation
