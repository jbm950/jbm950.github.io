# Analytical Dynamics
**Taught by: Dr. Riccardo Bevilacqua**  
**Taken: FS 2015**  
**Text: Dynamics of Particles and Rigid Bodies: A Systematic Approach**  
*by: Anil Rao*

## Table of Contents

- [Scalars](#scalars)
- [Vectors](#vectors)
- [Reference Frames](#reference_frames)
- [Coordinate System](#coordinate_system)
- [Vector Derivatives](#vector_derivatives)
- [Transport Theorem](#transport_theorem)

## Scalars {#scalars}

- Scalars do not need reference frames or coordinate systems
- Derivates of scalars follow the formal definition of the derivative
    - Ex. Let y(t) be a scalar function of time t, $\frac{dy}{dt} =
      \lim_{\Delta t \rightarrow 0} \frac{y(t + \Delta t) - y(t)}{\Delta t}$

## Vectors {#vectors}

- Vectors are quantities in $E^{3}$ (3D Euclidian Space) that have both
  magnitude and direction
- Magnitude is defined as $|| \underline{b} || = \sqrt{b \cdot b}$
- Direction of the vector is defined by its unit vector $\underline{u}_{b} =
  \frac{\underline{b}}{|| \underline{b} ||}$
- Vectors are reference frame independent
    - Vectors hold their true magnitude and direction no matter what reference
      frame you're observing from
- There are three types of vectors
    1. Free vectors - $\underline{b}$ & $\underline{b}'$ are the same vector if
       they have the same magnitude and direction
    2. Sliding vectors - $\underline{b}$ & $\underline{b}'$ are the same vector
       if they have the same magnitude and direction & share the same line of
       action in $E^{3}$
        - Ex. force vectors
    3. Bound vectors - $\underline{b}$ & $\underline{b}'$ are the same bound
       vector if they are the same sliding vector & share the same point of
       application
        - Ex. position vectors

## Reference Frames {#reference_frames}

- A reference frame is any set of at least 3 non-colinear points whose mutual
  distances are constant
- A reference frame is a rigid body and vice versa
- Deciding reference frames allows for the formulation of problems
    - They define a point of view put not a basis of measurement

## Coordinate System {#coordinate_system}

- Coordinate systems are a set of three linearly independent vectors
  {$\underline{e_{1}}, \underline{e_{2}}, \underline{e_{3}}$} in $E^{3}$
  (3D Euclidian Space)
- There are three main conviences that are made when creating a coordinate
  system
    1. Have all three vectors {$\underline{e_{1}}, \underline{e_{2}},
       \underline{e_{3}}$} be mutually orthogonal
    2. Have all three vectors {$\underline{e_{1}}, \underline{e_{2}},
       \underline{e_{3}}$} be unit vectors
    3. Create a right handed system
- Coordinate systems are built on reference frames to allow measurement within
  the frame or allow a problem to be implemented
    - The coordinate system moves with its reference frame
    - Coordinate systems must be fixed with only one reference frame whereas
      each reference frame can have infinite coordinate systems
- Bigger problems come from mistakes in the formulation of the problem
  (deciding reference frames) than mistakes in the implementation of the
  problem (deciding and using the coordinate systems)
- Two steps to defining a coordinate system
    1. Pick an origin
    2. Define the three right-handed orthogonal unit vectors,
       {$\underline{e_{1}}, \underline{e_{2}}, \underline{e_{3}}$}

## Vector Derivatives {#vector_derivatives}

- This class will be using Newtonian Mechanics rather than Relativistic
  Mechanics
    - Time is the independent variable ($^{A}t = ^{B}t = t \rightarrow$
      Galilean Invariance)
- Although vectors are reference frame independent, the geometric meaning of
  their derivative vectors are not reference frame independent (though the
  derivative vectors themselves being vectors are reference frame independent)
- Development of the general form of a derivative of a vector as viewed from
  reference frame A
    - $^{A}\underline{b} = b_{1}\underline{e}_{1} + b_{2}\underline{e}_{2} +
      b_{3}\underline{e}_{3}$
    - $\frac{^{A}d\underline{b}}{dt} = \frac{db_{1}(t)}{dt}\underline{e}_{1} +
      \frac{db_{2}(t)}{dt}\underline{e}_{2} +
      \frac{db_{3}(t)}{dt}\underline{e}_{3} +$
      $b_{1}\frac{^{A}d\underline{e}_{1}}{dt} +
      b_{2}\frac{^{A}d\underline{e}_{2}}{dt} +
      b_{3}\frac{^{A}d\underline{e}_{3}}{dt}$
        - The derivatives of the scalars are reference frame independent but
          the derivatives of the vectors are not
        - Utilizing the multiplication rule of derivatives
        - The first three terms represent the rate of change of vector
          $\underline{b}$ in the coordinate system defined by the
          $\underline{e}_{i}$ vectors
        - The last three terms represent the rate of change of the coordinate
          system defined by the $\underline{e}_{i}$ vectors with respect to
          reference frame A
            - If the vectors {$\underline{e_{1}}, \underline{e_{2}},
              \underline{e_{3}}$} are fixed in reference frame A then the last
              three terms in the derivative equal zero

## Transport Theorem {#transport_theorem}

- The transport theorem is a simplification of the vector derivative and can be
  stated as $\frac{^{A}d\underline{b}}{dt} = \frac{^{B}d\underline{b}}{dt} +
  ^{A}\underline{\omega}^{B} \times \underline{b}$ where {$\underline{e_{1}},
  \underline{e_{2}}, \underline{e_{3}}$} are fixed in reference frame B and
  $^{A}\underline{\omega}^{B}$ is the angular velocity of frame B as seen by an
  observer in reference frame A

> ### Transport Theorem Derivation

> - Taking the resultant formula for the derivative of a vector from above
    where {$\underline{e_{1}}, \underline{e_{2}}, \underline{e_{3}}$} are fixed
    in reference frame B we have $\frac{^{A}d\underline{b}}{dt} =
    \frac{db_{1}(t)}{dt}\underline{e}_{1} +
    \frac{db_{2}(t)}{dt}\underline{e}_{2} +
    \frac{db_{3}(t)}{dt}\underline{e}_{3} +$
    $b_{1}\frac{^{A}d\underline{e}_{1}}{dt} +
    b_{2}\frac{^{A}d\underline{e}_{2}}{dt} +
    b_{3}\frac{^{A}d\underline{e}_{3}}{dt}$ &nbsp;&nbsp; or &nbsp;&nbsp;
    $\frac{^{A}d\underline{b}}{dt} = \frac{^{B}d\underline{b}}{dt} +$
    $b_{1}\frac{^{A}d\underline{e}_{1}}{dt} +
    b_{2}\frac{^{A}d\underline{e}_{2}}{dt} +
    b_{3}\frac{^{A}d\underline{e}_{3}}{dt}$
> - Next we need to use some of the mathematical definitions of the {$\underline{e_{1}}, \underline{e_{2}}, \underline{e_{3}}$} vectors
>       - The vectors are all unit vectors therefore 
