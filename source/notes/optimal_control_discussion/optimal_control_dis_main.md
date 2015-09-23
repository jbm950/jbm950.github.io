# Optimal Control Discussion
**Led by: Dr. Anil Rao**  
**Taken: FS 2015**  
**Text: Optimal Control Theory: An Introduction**  
*by: D.E. Kirk*

## Table of Contents

- [Minimum Principle](#minimum_principle)
- [Functions vs. Functionals](#functions_vs_functionals)
- [Calculus of Variations](#calculus_of_variations)
- [Dynamical Systems](#dynamical_systems)

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

> __Simple Example Analogous to Calculus of Variations__

> - Suppose we want to determine a function $x(t)$ that minimizes an integral
    that is a function of $x(t)$ and $\dot{x}(t)$
>     - $J = \int^{t_{f}}_{t_{0}}L[x(t),\dot{x}(t),t]dt$
>     - $J$ is refered to as the _action integral_
>     - $x(t_{0})$ and $t_{0}$ are fixed
>     - $x(t_{f})$ and $t_{f}$ are fixed
> - Let $x^{*}(t)$ be the optimal solution and the function $x(t)$ be determined
    as follows
>     - $x(t) = x^{*}(t) + \epsilon y(t)$ where $y(t)$ is arbitrary and
        $\epsilon$ is chosen at will
>     - $x(t_{0}) = x^{*}(t_{0})$ and $x(t_{f}) = x^{*}(t_{f})$ because those
        points are fixed, therefore $y(t_{0}) = y(t_{f}) = 0$
> - Rewriting $J$ with the new definition of $x(t)$ gives the following expression
>     - $J = \int^{t_{f}}_{t_{0}}L[x^{*}(t) + \epsilon y(t),\dot{x}^{*}(t) +
        \epsilon \dot{y}(t),t]dt$
>     - $J$ is now solely a function of $\epsilon$ and so the critical point can
        be found at $\frac{dJ}{d\epsilon} | _{\epsilon = 0} = 0$
>         - $\epsilon$ is set to zero because that is what results in the optimal
            solution ($x(t) = x^{*}(t)$)
> - Using the definition of the critical point determined above the followin
    expression emerges
>     - $\frac{dJ}{d\epsilon}|_{\epsilon = 0} = \int^{t_{f}}_{t_{0}}
        (\frac{\partial L}{\partial x}$ $\frac{\partial x}{\partial \epsilon} +
        \frac{\partial L}{\partial \dot{x}} \frac{\partial \dot{x}}{\partial
        \epsilon})dt$
> - The following results from taking the derivative of x as given above with
    respect to $\epsilon$
>     - $\frac{\partial x}{\partial \epsilon} = y$
>     - $\frac{\partial \dot{x}}{\partial \epsilon} = \dot{y}$
> - When substituted into the above expression the following is the result
>     - $\frac{dJ}{d\epsilon}|_{\epsilon = 0} = \int^{t_{f}}_{t_{0}}
        (\frac{\partial L}{\partial x}$ $y +
        \frac{\partial L}{\partial \dot{x}} \dot{y})dt$
>         - Note, however, that $\dot{y}$ is not independent of $y$
> - In order to finish solving the equation we will integrate the second term in
    the integral by parts
>     - $\int^{t_{f}}_{t_{o}} \frac{\partial L}{\partial \dot{x}} \dot{y} dt$ $=
        \left[ \frac{\partial L}{\partial \dot{x}} y \right]^{t_{f}}_{t_{0}}$ $-
        \int^{t_{f}}_{t_{0}} \frac{d}{dt} (\frac{\partial L}{\partial
        \dot{x}})ydt$
>         - Keeping in mind from earlier that y evaluated at the boundary points
            is zero the first term in the result goes to zero ($\left[
            \frac{\partial L}{\partial \dot{x}} y \right]^{t_{f}}_{t_{0}} = 0$)
> - We can now rewrite the expression for the critical point as:
>     - $\frac{dJ}{d\epsilon}|_{\epsilon = 0} = \int^{t_{f}}_{t_{0}}
        \left[\frac{\partial L}{\partial x} - \frac{d}{dt} (\frac{\partial
        L}{\partial \dot{x}}) \right] y dt = 0$
> - Since the choice of y is arbitrary the portion inside the brackets has to
    equal zero in order to meet the equality
>     - $\left[\frac{\partial L}{\partial x} - \frac{d}{dt} (\frac{\partial
        L}{\partial \dot{x}}) \right] = 0$
> - This is the result of the analysis, however, note that it does not give a
    solution, just a condition for optimality

> __Simple Calculus of Variations Example (same as previous example)__

> - This will be the same example as the previous one but variational calculus
    will be used this time
> - The problem statement remains the same: suppose we want to determine a
    function $x(t)$ that minimizes an integral that is a function of $x(t)$ and
    $\dot{x}(t)$
>       - $J = \int^{t_{f}}_{t_{0}}L[x(t),\dot{x}(t),t]dt$
>       - $J$ is refered to as the _action integral_
>       - $x(t_{0})$ and $t_{0}$ are fixed
>       - $x(t_{f})$ and $t_{f}$ are fixed
> - The first step this time will be to take the variation of J as the extremal
    solution is obtained by setting the first variation equal to zero ($\delta
    J = 0$)
>       - $\delta J = \delta \int^{t_{f}}_{t_{0}}L[x(t),\dot{x}(t),t]dt$
> - Now due to the start and end times being fixed the variation can be moved
    inside the integral as the integral itself will be providing no variation
>       - $\delta J = \int^{t_{f}}_{t_{0}} \delta L[x(t),\dot{x}(t),t]dt$
> - The next step is to find the variation of L with respect to its components
>       - $\delta J = \int^{t_{f}}_{t_{0}} \left[ \frac{\partial L}{\partial x}
          \delta x + \frac{\partial L}{\partial \dot{x}} \delta \dot{x}
          \right]dt$
>       - Note that t has dropped from the function L. This is because the
          integral is definite and therefore t will be integrated out meaning J
          is not a function of t
> - This is the same form of equation that was found above where y is now
    equivalent to x and $\dot{y}$ is now equivalent to $\dot{x}$
> - Using the same integration by parts method as above and keeping in mind
    that the boundary conditions are still fixed the following expression can
    be derived
>       - $\delta J = \int^{t_{f}}_{t_{0}} \left[ \frac{\partial L}{\partial x}
          + \frac{d}{dt} (\frac{\partial L}{\partial \dot{x}}) \right]\delta
          x(t)dt = 0$
> - Therefore for the condition to hold for any variational function $\delta
    x(t)$ the part in brackets must equal zero
>       - $\frac{\partial L}{\partial x} + \frac{d}{dt} (\frac{\partial
          L}{\partial \dot{x}}) = 0$
> - This result is the same as was previously obtained and is still not a
    solution but rather a condition for optimality

> __Advanced Calculus of Variations__

> - More advanced calculus of variations problems arise when portions of the
    boundary conditions are no longer fixed (ex. $x(t_{f})$ is free or $t_{f}$
    is free)
> - One example of this would be a specified start time and position and a
    specified end position but no specified end time
>       - $x(t_{0})$, $t_{0}$ and $x(t_{f})$ are fixed
>       - $t_{f}$ is free
> - Another example would be a specified start time and position and a
    specified end time but no specified end position
>       - $x(t_{0})$, $t_{0}$ and $t_{f}$ are fixed
>       - $x(t_{f})$ is free

> - Before beginning the process to solve the two above examples a
    differentiation first needs to be made at the boundary of the function
    $x(t)$
>       - $\delta x_{f}$ is the difference in the final value of the variation
          $\delta x(t)$ and the function $x(t)$
>       - $\delta x(t_{f})$ is the difference between the value of the
          variation at $\delta x(t_{f})$ (original $t_{f}$ not $\delta t_{f}$)
          and the function $x(t_{f})$
>       - These two values are related by the expression $\delta x_{f} =
          \delta x(t_{f}) + \dot{x}(t_{f}) \delta t_{f}$

>> __First Example__

>> - To begin working through the optimality conditions of the first example
     listed above we start with the problem statement
>>       - $J = \int^{t_{f}}_{t_{0}} L \left[ x(t), \dot{x}(t), t \right] dt$
           where $x(t_{0})$, $t_{0}$ and $x(t_{f})$ are fixed and $t_{f}$ is
           free
>>       - min $J$ at $\delta J = 0$
>>       - There are two quantities that vary ($t_{f}$ and $x(t)$) and these two
           quantities are independent of each other
>> - Taking the variation of the function just like before gives
>>       - $\delta J = \delta \int^{t_{f}}_{t_{0}} L \left[ x(t), \dot{x}(t), t
           \right] dt = 0$
>>       - Unlike in the simple calculus of variations example the variation can
           not simply be moved inside the integral because $t_{f}$ is now
           allowed to vary also
>> - Taking into account the ability of $t_{f}$ to vary the expression becomes
>>       - $\delta J = \frac{\partial J}{\partial t_{f}} \delta t_{f} +
           \int^{t_{f}}_{t_{0}} \delta L$ $\left[ x(t), \dot{x}(t), t]dt$
>> - The left term of the right hand side of the above expression can be
     simplified with the following result
>>       - $\frac{\partial J}{\partial t_{f}} = L \left[ x(t), \dot{x}(t), t
           \right] |_{t_{f}}$ $= L \left[ x(t_{f}), \dot{x}(t_{f}), t_{f}
           \right]$
>> - The second term of the $\delta J$ expression needs to be simplified using
     integration by parts just like it was in the simple calculus of variations
     example
>>       - $\int^{t_{f}}_{t_{0}} \delta L \left[ x(t), \dot{x}(t), t \right] dt$
           $= \int^{t_{f}}_{t_{0}} \left[ \frac{\partial L}{\partial x} \delta x
           + \frac{\partial L}{\partial \dot{x}} \delta \dot{x} \right] dt$
>>       - $\int^{t_{f}}_{t_{o}} \frac{\partial L}{\partial \dot{x}} \delta
           \dot{x} dt$ $= \left[ \frac{\partial L}{\partial \dot{x}} \delta x
           \right]^{t_{f}}_{t_{0}}$ $- \int^{t_{f}}_{t_{0}} \frac{d}{dt}
           (\frac{\partial L}{\partial \dot{x}})\delta xdt$ $= \frac{\partial
           L}{\partial \dot{x}}|_{t_{f}} \delta x(t_{f})$ $-
           \int^{t_{f}}_{t_{0}} \frac{d}{dt} (\frac{\partial L}{\partial
           \dot{x}})\delta xdt$
>> - Since in this problem $\delta x_{f} = 0$ the term $\delta x(t_{f}) =
     -\dot{x}(t_{f}) \delta t_{f}$
>> - Arranging all of the terms back into the expression for the variation of
     the action integral yields
>>       - $\delta J = L \left[ x(t_{f}), \dot{x}(t_{f}), t_{f} \right] \delta
           t_{f} - \frac{\partial L}{\partial \dot{x}}|_{t_{f}} \dot{x}(t_{f})
           \delta t_{f}$ $+ \int^{t_{f}}_{t_{0}} \left[ \frac{\partial
           L}{\partial x} - \frac{d}{dt}\frac{\partial L}{\partial \dot{x}}
           \right] \delta x dt = 0$
>>       - $\delta J = \left( L \left[ x(t_{f}), \dot{x}(t_{f}), t_{f} \right] -
           \frac{\partial L}{\partial \dot{x}}|_{t_{f}} \dot{x}(t_{f}) \right)
           \delta t_{f}$ $+ \int^{t_{f}}_{t_{0}} \left[ \frac{\partial
           L}{\partial x} - \frac{d}{dt}\frac{\partial L}{\partial \dot{x}}
           \right] \delta x dt = 0$
>> - Keeping in mind that $\delta t_{f}$ and $\delta x$ are independent of one
     another, for the above expression to be valid for any varitiation in
     $t_{f}$ or $x(t)$ both terms have to equal zero
>>       - $L \left[ x(t_{f}), \dot{x}(t_{f}), t_{f} \right] -
           \frac{\partial L}{\partial \dot{x}}|_{t_{f}} \dot{x}(t_{f}) = 0$
           (refered to as the natural boundary condition)
>>       - $\frac{\partial L}{\partial x} - \frac{d}{dt}\frac{\partial
           L}{\partial \dot{x}} = 0$
>> - We now have optimality conditions for the case with a non-fixed end time
    $t_{f}$

>> __Second Example__

>> - Now for the second advanced calculus of variations example we will have
     fixed start position and time and a fixed end time but not a fixed end
     position
>>       - $x(t_{0})$, $t_{0}$ and $t_{f}$ are fixed
>>       - $x(t_{f})$ is free
>> - We will again begin by taking the variation of functional $J$ and noting
     that this time because the start and end times are fixed the variation can
     be moved inside the integral
>>       - $\delta J = \delta \int^{t_{f}}_{t_{0}} L \left[ x(t), \dot{x}(t), t
           \right] dt$
>>       - $\delta J = \int^{t_{f}}_{t_{0}} \delta L \left[ x(t), \dot{x}(t), t
           \right] dt$
>>       - $\delta J = \int^{t_{f}}_{t_{0}} \left[ \frac{\partial L}{\partial x}
           \delta x + \frac{\partial L}{\partial \dot{x}} \delta \dot{x}
           \right]dt$
>> - The next step moving forward will be to integrate the second term in the
     integral by parts as has been done in the previous examples
>>       - $\int^{t_{f}}_{t_{0}} \frac{\partial L}{\partial \dot{x}} \delta
           \dot{x}(t)dt$ $= \left[ \frac{\partial L}{\partial \dot{x}} \delta x
           \right]^{t_{f}}_{t_{0}} - \int^{t_{f}}_{t_{0}} \frac{d}{dt}
           (\frac{\partial L}{\partial \dot{x}}) \delta x dt$
>>       - $\int^{t_{f}}_{t_{0}} \frac{\partial L}{\partial \dot{x}} \delta
           \dot{x}(t)dt$ $= \frac{\partial L}{\partial \dot{x}}|_{t_{f}} \delta
           x(t_{f}) - \int^{t_{f}}_{t_{0}} \frac{d}{dt} (\frac{\partial
           L}{\partial \dot{x}}) \delta x dt$
>> - Putting this result back in the previous equation yields the following
     expression
>>       - $\delta J = \frac{\partial L}{\partial \dot{x}}|_{t_{f}} \delta
           x(t_{f}) + \int^{t_{f}}_{t_{0}}$ $\left[ \frac{\partial L}{\partial
           x} - \frac{d}{dt} (\frac{\partial L}{\partial \dot{x}}) \right]\delta
           x dt = 0$
>> - Now considering that the expression has to hold for any variation $\delta
     x(t_{f})$ and $\delta x$ both of the terms have to independently equal
     zero
>>       - $\frac{\partial L}{\partial \dot{x}}|_{t_{f}} = 0$
>>       - $\frac{\partial L}{\partial x} - \frac{d}{dt} (\frac{\partial
           L}{\partial \dot{x}}) = 0$
>> - We now have optimality conditions for the case with a non-fixed end
     position $x(t_{f})$

> - Notice in both of the advanced calculus of variations examples making a
    boundary point free resulted in another optimality condition

## Dynamical Systems {#dynamical_systems}

- A given system can be defined in each point in time by its state
  $\underline{x}(t) = \left[ x_{1}(t), ..., x_{n}(t) \right]^{T}$
- The state of the system is affected by the input control on the system
  $\underline{u}(t) = \left[ u_{1}, ..., u_{m}(t) \right]^{T}$
- Note that the components of the state and control are not refered to as the
  states or controls but rather the $i^{th}$ component of the state or control
    - The states or controls refers to the state or control at multiple time
      instances 
- It is desired to control the motion of the system in a manner that optimizes
  some performance criteria
- The optimization of a performance criteria is going to be translated into
  minimizing a cost functional J
- The cost functional can be written as $J = \Phi(\underline{x}(t_{0}), t_{0},
  \underline{x}(t_{f}), t_{f}) + \int^{t_{f}}_{t_{0}} L \left[
  \underline{x}(t), \underline{u}(t), t \right] dt$
    - The first term of the cost functional is refered to as the Mayer cost or
      endpoint cost and it represents the constraints that are enforced at the
      start and terminus
    - The second term of the cost functional is refered to as the Lagrange
      cost, running cost or integrated cost and it represents the constraints
      that are enforce along the path during motion
