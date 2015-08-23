__Faster, Higher and Greener: Vehicular Optimal Control__  
__Written by David J.N. Limebeer and Anil Rao__  
__Published in IEEE Control Systems Magazine: April 2015__  
<a href="http://vdol.mae.ufl.edu/JournalPublications/IEEE-CSM-14-0038.pdf" target="_blank">Full
Article</a>

##Table of Contents

- [Optimal Control](#optimal_control)
- [Numerical Methods Used in Optimal Control](#num_methods_used)
- [Explicit Simulation (Time Marching)](#explicit_simulation)
- [Implicit Simulation (Collocation)](#implicit_simulation)
- [Indirect Methods](#indirect_methods)
- [Direct Methods](#direct_methods)

## Optimal Control {#optimal_control}

- Often posed in the general Bolza form
    - Minimize the objective functional by determining the following
        - The state of the system (__x__(t))
        - The control for the system (__u__(t))
        - The initial time ($t_{0}$)
        - The terminal time ($t_{f}$)
    - Objective functional subject to:
        - Dynamic constraint
        - Path constraint
        - Boundary condition

- Bolza problem leads to first-order [calculus of
  variations](../grad_general_notes.html#calc_of_variations) conditions
- More details can be found in the [Hamiltonian Boundary-Value Problem](../grad_general_notes.html#hamiltonian_bv_p) section.

## Numerical Methods Used in Optimal Control {#num_methods_used}

- Two different distinctions in solving optimal control problems
    - Problem being solved
        - [Indirect method](#indirect_methods) = Find solution to first-order
          necessary conditions
        - [Direct method](#direct_methods) = Find solution to optimal control
          problem itself
    - Type of numerical method to solve the problem
        - [Explicit Simulation](#explicit_simulation) = Solution obtained using
          a time marching approach
        - [Implicit Simulation](#implicit_simulation) = Solution obtained for
          all time steps simultaneously (no time marching)

## Explicit Simulation (Time Marching) {#explicit_simulation}

- In explicit simulation the solution to future time steps is found using the
  solution to the current and past time steps, hence time marching
- Basic explicit simulation method is the _shooting method_
    - Guess at boundary conditions at one side of the time interval and time
      march to the other side
    - Evaluate the error tolerance at the other side of the interval and if the
      tolerance is not met adjust the guess and repeat
    - Can encounter difficulties due to instabilities in the dynamics
- Overcome difficulties with the _multiple-shooting method_
    - Same as _shooting method_ but divide the time interval into smaller
      subintervals
    - Reduces sensitivity to errors

## Implicit Simulation (Collocation) {#implicit_simulation}

## Indirect Methods {#indirect_methods}

## Direct Methods {#direct_methods}
