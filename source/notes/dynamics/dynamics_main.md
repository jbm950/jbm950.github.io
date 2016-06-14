# Dynamics Notes

This will be the localized place for all future dynamics notes, however,
much of my dynamics notes are currently located on the notes page for my
[analytical dynamics
class](../analytical_dynamics/analytical_dynamics_main.html).

## Table of Contents

- [Equations of Motion](#eom)
- [Mass Matrix](#mass_matrix)
- [Nonholonomic System](#nonholonomic_system)

## Equations of Motion

> __Cannonical Form Given in Featherstone's Book__

> - $H(q)\ddot{q}+C(q,\dot{q})=\tau$
>       - Where:
>           - H is the generalized inertia matrix
>           - C is the generalized bias force
>           - q is the generalized coordinate and its derivatives

> __Unlabeled Form in Kanes Book__

> - $\frac{dx_{i}}{dt} = f_{i}(x_{1},\; ...,\; x_{v};\; t)$ where $(i = 1,\;
    ...,\; v)$
>       - $x_{1},\; ...,\; x_{v}$ are undefined functions of time
>       - Sentence in book "set of v first-order differential equations of the
          form". Doesn't give name to the form.

> __Forms Labeled in Robinovitch's Slides__

> - $M(\phi)\ddot{\phi} = T^{mus} + V(\phi, \dot{\phi}) + G(\phi)$
>       - $M(\phi) =$ inertia (or mass) matrix
>       - $T^{mus} =$ net muscle moment vector
>       - $V(\phi, \dot{\phi}) =$ vector of torques due to centripetal and
          coriolis forces
>       - $G(\phi) =$ vector of joint torques due to gravity
> - Equations appear to be more centered on rotational systems

>> __Forward Dynamics__

>> - $\ddot{\phi} = M(\phi)^{-1}T^{mus} + M(\phi)^{-1}V(\phi, \dot{\phi}) +
     M(\phi)^{-1}G(\phi)$

>> __Inverse Dynamics__

>> - $T^{mus} = M(\phi)\ddot{\phi} + V(\phi, \dot{\phi}) + G(\phi)$

## Mass Matrix {#mass_matrix}

The formal definition for a mass matrix M is 

$T = \frac{1}{2} \dot{q}^{T} M \dot{q}$

where

- $T$ is the kinetic energy of the system
- $\dot{q}$ is first time derivative of the generalized coordinate vector q 

## Nonholonomic system {#nonholonomic_system}

A nonholonomic system is a system whose state depends on the path taken in
order to achieve it. (Path dependent system)

A constraint which does not reduce the degrees of freedom (Knowing one
generalized coordinate and the constraint allows solving for the other
coordinate is a holonomic system, ie two points connected by a massless rod)

<hr>

## Sources

- [Dynamics: Theory and
  Applications](https://ecommons.cornell.edu/handle/1813/638) (Thomas Kane and
  David Levinson)
- [Dynamics pt. 2: Equations of motion and system
  identification](http://www.sfu.ca/~stever/kin840/lecture_outlines/lecture_3_dynamics_pt_2.pdf)
  (Stephen Robinovitch)
- [Mass Matrix, Wikipedia](https://en.wikipedia.org/wiki/Mass_matrix)
- [Nonholonomic systems,
  Wikipedia](https://en.wikipedia.org/wiki/Nonholonomic_system)
- [Nonholonomic
  Constraints](http://www.ingvet.kau.se/juerfuch/kurs/amek/prst/11_nhco.pdf)
- [Rigid Body Dynamics
  Algorithms](http://www.springer.com/us/book/9780387743141) (Roy Featherstone)
