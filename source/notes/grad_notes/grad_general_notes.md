# Concepts

> ## Calculus of Variations {#calc_of_variations}

> - Calculus of variations deals with the mathematics of finding a stationary
    point (where $\dot{f}(x) = 0$)
>       - Useful when trying to find maxima and minima to optimize a physical
          quantity.

>> ### Euler-Lagrange Equation Example

>> - Unknown http://www.math.umn.edu/~olver/ln_/cv.pdf

> ## Hamiltonian {#hamiltonian}

> - The control Hamiltonian is by definition $H(x, u, \lambda, t) = L(x, u, t)
    + \lambda^{T}f(x, u, t)$
> - Used in the derivation of optimal control
>       - The control function is $J = \textit{\Phi}[x(t_{f})] +
          \int_{0}^{t_{f}}L(x, u, t)\textit{dt}$
>       - The control function can be re-written as $J =
          \textit{\Phi}[x(t_{f})] + \int_{0}^{t_{f}}L(x, u, t)\textit{dt} +
          \int_{0}^{t_{f}}\lambda^{T}(f-\dot{x})\textit{dt}$ where
          $(f-\dot{x})$ is a zero vector and so the original equation hasn't
          been altered
>       - With the definition of the Hamiltonian the control function can be
          simplified to $J = \textit{\Phi}[x(t_{f})] +
          \int_{0}^{t_{f}}[H-\lambda^{T}\dot{x}]\textit{dt}$
> - The Hamiltonian is important as it provides the source of the costate
    ($\lambda$) differential equations and the optimality condition of the
    Two-Point Boundary Value Problem
>       - $\dot{\lambda} = -\frac{\partial H}{\partial x}$    (Costate
          differential equations)
>       - $\frac{\partial H}{\partial u} = 0$    (Optimality condition)


> ## Hamiltonian Boundary-Value Problem {#hamiltonian_bv_p}

# Terms

- HBVP = Hamiltonian Boundary Value Problem
