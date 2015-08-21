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
