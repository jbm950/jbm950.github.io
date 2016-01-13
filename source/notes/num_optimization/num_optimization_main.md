# Numerical Optimization
**Taught by: Dr. Bill Hager**  
**Taken: SS 2016**  

Non-required Texts:

- Numerical Optimization (Nocedal & Wright)
- Nonlinear Programming (Bertsekas)

## Table of Contents

- [Optimality Conditions for Unconstrained Problems](#opt_cond_unconstrained)

## Optimality Conditions for Unconstrained Problems {#opt_cond_unconstrained}

- $f: \: \mathbb{R}^{n} \right \mathbb{R}$
- $x^{*}$ is a local minimizer of $f$ if there exists some $\rho \, > \, 0$
  such that $f(x) \geq f(x^{*})$ whenever $||x - x^{*} || \leq \rho$
- Going to be using Euclidian Norm in this class
    - $|| x || = \sqrt{\sum^{n}_{i=1} x_{i}^{2}}$ 

> __Suppose n = 1__

> - $f(x) \geq f(x^{*})$ for all $|x - x^{*}| \leq \rho$
> - $f(x^{*} + \Delta x) \geq f(x^{*})$ whenever $| \Delta x | \leq \rho$
>     - The function in a neighborhood around $x^{*}$ is at most equal to the
        value at $x^{*}$ but never greater
> - $lim_{\Delta x \right 0} \frac{f(x^{*} + \Delta x) - f(x^{*})}{\Delta x}
    \geq 0$
