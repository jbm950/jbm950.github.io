# Optimal Control Discussion
**Led by: Dr. Anil Rao**  
**Taken: FS 2015**  
**Text: Optimal Control Theory: An Introduction**  
*by: D.E. Kirk*

## Table of Contents

- [Minimum Principle](#minimum_principle)
- [Functions vs. Functionals](#functions_vs_functionals)
- [Calculus of Variations](#calculus_of_variations)

## Minimum Principle {#minimum_principle}

- The most general form of finding a minimum value for a function $f(x)$ can be
  stated as $x^{*} = arg (min_{x \in [a,b]}) f(x)$
    - $min_{x \in [a,b]} f(x)$ will return the minimum value of $f(x)$ over the
      input interval [a, b]
    - $arg$ will find the input value that resulted in the minimum $f(x)$ value
- The minimum principle can be used to determine the optimal solution, $x^{*}$,
  to the function $f(x)$
- This form is more general of a condition than that provided by the first and
  second derivative tests
- This would be considered direct optimization because the function $f(x)$ is
  actually evaluated when finding the optimal input

## Functions vs. Functionals {#functions_vs_functionals}

- Functions map real numbers to real numbers whereas functionals map functions
  to real numbers
    - An example of a functional is an integral. It takes a function as an
      input and maps it to a real number
- When optimizing functions only ordinary calculus is required but when
  optimizing functionals variational calculus is required

> __$\Delta$ vs. $\delta$__

> - $\Delta$ is the difference between points in real space
> - $\delta$ is variation in a function
>       - $\delta f(t)$ is itself a function

## Calculus of Variations {#calculus_of_variations}

- Suppose we want to determine a function $x(t)$ that minimizes an integral
  that is a function of $x(t)$ and $\dot{x}(t)$
    - $J = \int^{t_{f}}_{t_{0}}L[x(t),\dot{x}(t),t]dt$
    - $J$ is refered to as the _action integral_
    - $x(t_{0})$ and $t_{0}$ are fixed
    - $x(t_{f})$ and $t_{f}$ are fixed
- Let $x^{*}(t)$ be the optimal solution and the function $x(t)$ be determined
  as follows
    - $x(t) = x^{*}(t) + \epsilon y(t)$ where $y(t)$ is arbitrary and
      $\epsilon$ is chosen at will
    - $x(t_{0}) = x^{*}(t_{0})$ and $x(t_{f}) = x^{*}(t_{f})$ because those
      points are fixed, therefore $y(t_{0}) = y(t_{f}) = 0$
- Rewriting $J$ with the new definition of $x(t)$ gives the following expression
    - $J = \int^{t_{f}}_{t_{0}}L[x^{*}(t) + \epsilon y(t),\dot{x}^{*}(t) +
      \epsilon \dot{y}(t),t]dt$
    - $J$ is now solely a function of $\epsilon$ and so the critical point can
      be found at $\frac{dJ}{d\epsilon} | _{\epsilon = 0} = 0$
        - $\epsilon$ is set to zero because that is what results in the optimal
          solution ($x(t) = x^{*}(t)$)
- Using the definition of the critical point determined above the followin
  expression emerges
    - $\frac{dJ}{d\epsilon}|_{\epsilon = 0} = \int^{t_{f}}_{t_{0}}
      (\frac{\partial L}{\partial x}$ $\frac{\partial x}{\partial \epsilon} +
      \frac{\partial L}{\partial \dot{x}} \frac{\partial \dot{x}}{\partial
      \epsilon})dt$
- The following results from taking the derivative of x as given above with
  respect to $\epsilon$
    - $\frac{\partial x}{\partial \epsilon} = y$
    - $\frac{\partial \dot{x}}{\partial \epsilon} = \dot{y}$
- When substituted into the above expression the following is the result
    - $\frac{dJ}{d\epsilon}|_{\epsilon = 0} = \int^{t_{f}}_{t_{0}}
      (\frac{\partial L}{\partial x}$ $y +
      \frac{\partial L}{\partial \dot{x}} \dot{y})dt$
        - Note, however, that $\dot{y}$ is not independent of $y$
- In order to finish solving the equation we will integrate the second term in
  the integral by parts
    - $\int^{t_{f}}_{t_{o}} \frac{\partial L}{\partial \dot{x}} \dot{y} dt$ $=
      \left[ \frac{\partial L}{\partial \dot{x}} y \right]^{t_{f}}_{t_{0}}$ $-
      \int^{t_{f}}_{t_{0}} \frac{d}{dt} (\frac{\partial L}{\partial
      \dot{x}})ydt$
        - Keeping in mind from earlier that y evaluated at the boundary points
          is zero the first term in the result goes to zero ($\left[
          \frac{\partial L}{\partial \dot{x}} y \right]^{t_{f}}_{t_{0}} = 0$)
- We can now rewrite the expression for the critical point as:
    - $\frac{dJ}{d\epsilon}|_{\epsilon = 0} = \int^{t_{f}}_{t_{0}}
      \left[\frac{\partial L}{\partial x} - \frac{d}{dt} (\frac{\partial
      L}{\partial \dot{x}}) \right] y dt = 0$
- Since the choice of y is arbitrary the portion inside the brackets has to
  equal zero in order to meet the equality
    - $\left[\frac{\partial L}{\partial x} - \frac{d}{dt} (\frac{\partial
      L}{\partial \dot{x}}) \right] = 0$
- This is the result of the analysis, however, note that it does not give a
  solution, just a condition for optimality
