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
- [Examples](#examples)

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
- Some useful properties of the angular velocity are:
    1. $^{A}\underline{\omega}^{B} = -^{B}\underline{\omega}^{A}$
    2. $^{A}\underline{\omega}^{E} = ^{A}\underline{\omega}^{B} +
       ^{B}\underline{\omega}^{C} + ^{C}\underline{\omega}^{D} +
       ^{D}\underline{\omega}^{E}$

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
> - Next we need to use some of the mathematical definitions of the
    {$\underline{e_{1}}, \underline{e_{2}}, \underline{e_{3}}$} vectors
>       - The vectors are all unit vectors therefore $\underline{e}_{i} \cdot
          \underline{e}_{i} = 1$ for i = 1, 2, 3
>       - The vectors are all mutually orthogonal therefore $\underline{e}_{i}
          \cdot \underline{e}_{j} = 0$ for i $\neq$ j
>       - Taking the derivative of the unit vector rule we obtain
          $\frac{^{A}d(\underline{e}_{i} \cdot \underline{e}_{i})}{dt} =
          \underline{e}_{i} \cdot \frac{^{A}d\underline{e}_{i}}{dt} +
          \frac{^{A}d\underline{e}_{i}}{dt}$ $\cdot \underline{e}_{i} =
          \underline{e}_{i} \cdot \frac{^{A}d\underline{e}_{i}}{dt} = 0$
>           - A result of this is that it shows that a unit length vector,
              $\underline{e}_{i}$, will always be perpendicular to its
              derivative
>       - Taking the derivative of the orthogonal rule we obtain
          $\frac{^{A}d(\underline{e}_{i} \cdot \underline{e}_{j})}{dt} =
          \underline{e}_{i} \cdot \frac{^{A}d\underline{e}_{j}}{dt} +
          \frac{^{A}d\underline{e}_{i}}{dt} \cdot \underline{e}_{j} = 0$
          &nbsp;&nbsp; or &nbsp;&nbsp; $\underline{e}_{i} \cdot
          \frac{^{A}d\underline{e}_{j}}{dt} = -
          \frac{^{A}d\underline{e}_{i}}{dt} \cdot \underline{e}_{j}$
>       - The next step is to write out the derivate of each unit vector in
          terms of a component of $\omega$, the angular velocity,  multiplied
          by each of the unit vectors
>           - $\frac{^{A}d\underline{e}_{1}}{dt} = \omega_{11}\underline{e}_{1}
              + \omega_{21}\underline{e}_{2} + \omega_{31}\underline{e}_{3}$
>           - $\frac{^{A}d\underline{e}_{2}}{dt} = \omega_{12}\underline{e}_{1}
              + \omega_{22}\underline{e}_{2} + \omega_{32}\underline{e}_{3}$
>           - $\frac{^{A}d\underline{e}_{3}}{dt} = \omega_{13}\underline{e}_{1}
              + \omega_{23}\underline{e}_{2} + \omega_{33}\underline{e}_{3}$
>       - We know from the derivative of the unit vector rule that the
          derivative of a unit vector will not contain any component along the
          direction of that unit vector ($\omega_{11} = \omega_{22} =
          \omega_{33} = 0$)
>       - We also know from the result of the derivative of the orthogonal rule
          that the component of the derivative of first vector in the second
          vectors direction is the negative of the second vectors derivative in
          the first vector's direction ($\omega_{21} = - \omega_{12}$,
          $\omega_{13} = - \omega_{31}$, $\omega_{23} = - \omega_{32}$)
>       - With these two rules we can re-write the three
          $\frac{^{A}d\underline{e}_{i}}{dt}$ equations
>           - $\frac{^{A}d\underline{e}_{1}}{dt} = \omega_{21}\underline{e}_{2}
              + \omega_{31}\underline{e}_{3}$
>           - $\frac{^{A}d\underline{e}_{2}}{dt} = -\omega_{21}\underline{e}_{1}
              + \omega_{32}\underline{e}_{3}$
>           - $\frac{^{A}d\underline{e}_{3}}{dt} = -\omega_{31}\underline{e}_{1}
              - \omega_{32}\underline{e}_{2}$
>       - We now define the following three $\omega$'s: $\omega_{1} =
          \omega_{32}$, $\omega_{2} = -\omega_{31}$ and $\omega_{3} =
          \omega_{21}$
>       - With the $\omega$ redefinitions we can introduce
          $^{A}\underline{\omega}^{B}$, the angular velocity of frame B as seen
          by an observer in frame A as $^{A}\underline{\omega}^{B} =
          \omega_{1}\underline{e}_{1} + \omega_{2}\underline{e}_{2} +
          \omega_{3}\underline{e}_{3}$
>           - This definition of angular velocity allows the equation
              $\frac{^{A}d\underline{e}_{i}}{dt} = ^{A}\underline{\omega}^{B}
              \times \underline{e}_{i}$ to produce the three above equations
>       - Substituting the equation for $\frac{^{A}d\underline{e}_{i}}{dt}$
          into the very first equation results in
          $\frac{^{A}d\underline{b}}{dt} = \frac{^{B}d\underline{b}}{dt} +$
          $b_{1}\frac{^{A}d\underline{e}_{1}}{dt} +
          b_{2}\frac{^{A}d\underline{e}_{2}}{dt} +
          b_{3}\frac{^{A}d\underline{e}_{3}}{dt}$ $=
          \frac{^{B}d\underline{b}}{dt} + b_{1}^{A}\underline{\omega}^{B}
          \times \underline{e}_{1} +$ $b_{2}^{A}\underline{\omega}^{B} \times
          \underline{e}_{2} + b_{3}^{A}\underline{\omega}^{B} \times
          \underline{e}_{3}$
>       - To simplify further separate the angular velocity out of the cross
          products: $\frac{^{A}d\underline{b}}{dt} =
          \frac{^{B}d\underline{b}}{dt} + ^{A}\underline{\omega}^{B} \times
          (b_{1}\underline{e}_{1} + b_{2}\underline{e}_{2} +
          b_{3}\underline{e}_{3})$
>           - Now taking the definition of $\underline{b}$ as $\underline{b} =
              b_{1}\underline{e}_{1} + b_{2}\underline{e}_{2} +
              b_{3}\underline{e}_{3}$ we can re-write the above expression as
              $\frac{^{A}d\underline{b}}{dt} = \frac{^{B}d\underline{b}}{dt} +
              ^{A}\underline{\omega}^{B} \times \underline{b}$ which is the
              transport theorem

## Examples {#examples}

> ### Examples Content

> - [Transport Theorem](#e_transport_theorem)

> ### Transport Theorem Examples

> - __First Transport Theorem Example:__

>> - Given a disk (D) rotating about its centerpoint (O), find the velocity and
     acceleration of point P as seen by the disk (D) and the ground (G)

<div align="center">
<table class="image">
<tr><td><img src="./img/trans_theo_example1_diagram1.png"
alt="Example 1, Diagram 1" title="Example 1, Diagram 1" width="200"
height="200"/> 
</td></tr>
</table>
</div>

>> - Start by defining reference frames and then coordinate systems within them
>> - For this problem two reference frames will be used: the disk (D) and the
     ground (G)
>> - Coordinate system fixed in the disk reference frame (D)
>>      - Origin at point O
>>      - $\underline{e}_{r}$ = along the line $\underline{OP}$
>>      - $\underline{e}_{z}$ = out of the page (positive with theta)
>>      - $\underline{e}_{\theta}$ = $\underline{e}_{z} \times \underline{e}_{r}$

<div align="center">
<table class="image">
<tr><td><img src="./img/disk_ref_frame.png"
alt="Disk Reference Frame" title="Disk Reference Frame" width="125"
height="125"/> 
</td></tr>
</table>
</div>

>> - Coordinate system fixed in the ground reference frame (G)
>>      - Origin at point O
>>      - $\underline{E}_{z}$ = $\underline{e}_{z}$
>>      - $\underline{E}_{x}$ = along the line $\underline{OP}$ @ $\theta = 0$
>>      - $\underline{E}_{y}$ = $\underline{E}_{z} \time \underline{E}_{x}$

<div align="center">
<table class="image">
<tr><td><img src="./img/ground_ref_frame.png"
alt="Ground Reference Frame" title="Ground Reference Frame" width="200"
height="200"/> 
</td></tr>
</table>
</div>

>> - Now to find the velocity and acceleration of point P in the disk reference
     frame we take the time derivative of the vector from the origin O to point
     P ($\underline{r} = \underline{OP} = r\underline{e}_{r}$)
>>      - $^{D}\underline{V}_{P} = \frac{^{D}d\underline{r}}{dt} =
          \frac{^{D}d}{dt}(r\underline{e}_{r})$ $=
          \frac{dr}{dt}\underline{e}_{r} + r\frac{^{D}d\underline{e}_{r}}{dt}$
>>      - Neither r nor $\underline{e}_{r}$ are changing in the disk reference
          frame therefore $^{D}\underline{V}_{P} = 0$
>> - Next the acceleration of point P in the disk reference frame is to be
     found by taking a time derivative of the velocity of point P in the disk
     reference frame
>>      - $^{D}\underline{a}_{P} = \frac{^{D}d}{dt}(^{D}\underline{V}_{P}) = 0$
>> - Now the velocity needs to be found for point P in the ground reference
     frame and two different approaches will be shown

>>> - First approach involves writing all of the equations with respect to the
      coordinate system fixed in reference frame G
>>>     - $\underline{r} = r\underline{e}_{r} = rcos(\theta)\underline{E}_{x} +
          rsin(\theta)\underline{E}_{y}$
>>>     - $^{G}\underline{V}_{P} = \frac{^{G}d\underline{r}}{dt}$ $= -r\dot{\theta}sin(\theta)\underline{E}_{x} + r\dot{\theta}cos(\theta)\underline{E}_{y}$
