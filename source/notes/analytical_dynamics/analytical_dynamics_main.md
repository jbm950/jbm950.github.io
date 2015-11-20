# Analytical Dynamics
**Taught by: Dr. Riccardo Bevilacqua**  
**Taken: FS 2015**  
**Text: Dynamics of Particles and Rigid Bodies: A Systematic Approach**  
*by: Anil Rao*

## Table of Contents

> ### Kinematics

> - [Scalars](#scalars)
> - [Vectors](#vectors)
> - [Reference Frames](#reference_frames)
> - [Coordinate System](#coordinate_system)
> - [Vector Derivatives](#vector_derivatives)
> - [Transport Theorem](#transport_theorem)
> - [Cylindrical Coordinate Systems](#cylindrical_coordinate_systems)
> - [Spherical Coordinate Systems](#spherical_coordinate_system)
> - [Euler Angles](#euler_angles)
> - [Intrinsic Coordinates](#intrinsic_coordinates)
> - [Motion Between Two Points in the Same Reference Frame](#motion_two_points)
> - [Rolling and Slipping](#rolling_and_slipping)

> ### Kinetics of Particles

> - [Inertial Reference Frame(s)](#inertial_ref_frames)
> - [Three Laws of Mechanics](#three_laws_of_mechanics)
> - [Angular Momentum](#angular_momentum)
> - [Relative Velocity](#relative_velocity)
> - [Friction Force Models](#friction_force_models)
> - [Linear Spring Force Model](#linear_spring_force_model)

> ### Kinematics and Kinetics of Rigid Bodies/Systems of Particles

> - [Center of Mass](#center_of_mass)
> - [Tensors](#tensors)
> - [Angular Momentum](#angular_momentum2)
> - [Pure Torque](#pure_torque)
> - [Euler's Laws](#eulers_laws)

> ### Analytical Dynamics

> - [Parameterize a Problem](#parameterize_prob)
> - [Lagrange Equations](#lagrange_equations)

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

## Cylindrical Coordinate Systems {#cylindrical_coordinate_systems}

- In the given diagram a cylindrical coordinate system can be established in
  the reference frame defined by the plane containing points O, P and Q (or
  vectors r and $\underline{r}$)
- The coordinate system in this reference frame will be:
    - Origin at O
    - $\underline{e}_{r}$ = along $\underline{OQ}$
    - $\underline{e}_{z}$ = $\underline{E}_{z}$
    - $\underline{e}_{\theta}$ = $\underline{e}_{z} \times \underline{e}_{r}$
- This coordinate system rotates with $\theta$ and as it rotates the line
  $\underline{QP}$ forms the outside of a cylinder which gives the coordinate
  system its name

<div align="center">
<table class="image">
<tr><td><img src="./img/cylindrical_coor_sys.png"
alt="Cylindrical Coordinate System" title="Cylindrical Coordinate System"
width="300" height="300"/> 
</td></tr>
</table>
</div>

## Spherical Coordinate Systems {#spherical_coordinate_system}

- For the given diagram we will create a new reference frame that conatains the
  vector $\underline{r}$ and is perpendicular to the plane created by
  $\underline{E}_{z}$ and $\underline{r}$
    - Note that this new reference plane differs from the reference frame
      containing the cylindrical coordinate system by an angle $\phi$
    - This reference frame rotates with $\theta$ and $\phi$
- The spherical coordinate system in this new reference frame will be:
    - Origin at O
    - $\underline{u}_{r}$ = along $\underline{r}$
    - $\underline{u}_{\theta}$ = $\underline{e}_{\theta}$ (from cylindrical
      coordinate system)
    - $\underline{u}_{\phi}$ = $\underline{u}_{\theta} \times \underline{u}_{r}$
- For a constant $\underline{r}$, the full rotation of point P with respect to
  both $\theta$ and $\phi$ produces a sphere which is where the name for this
  coordinate system originates

<div align="center">
<table class="image">
<tr><td><img src="./img/spherical_coor_sys.png"
alt="Spherical Coordinate System" title="Spherical Coordinate System"
width="300" height="300"/> 
</td></tr>
</table>
</div>

## Euler Angles {#euler_angles}

- Start with a few important defintions of angles
    1. There is no vector such that its derivative is equal to the angular
       acceleration
        - For $^{A}\underline{\omega}^{R} = \omega_{1} \underline{e}_{1} +
          \omega_{2} \underline{e}_{2} + \omega_{3} \underline{e}_{3}$ there
          will never be a vector $b$ such that $\dot{b}_{1} = \omega_{1}$,
          $\dot{b}_{2} = \omega_{2}$, $\dot{b}_{3} = \omega_{3}$
    2. Rotations do NOT commute
        - Order is extremely important
- There are many different rotation orders (12 combinations for three axes)
    - Can repeat numbers so long as the repeated numbers are not sequential
- The most commonly used rotation sequence is the 321 sequence (z, y, x)

- First rotation in the 321 sequence is $\psi$ around the z-axis

<div align="center">
<table class="image">
<tr><td><img src="./img/euler_angle_step_1.png"
alt="Euler Angle First Rotation" title="Euler Angle First Rotation"
width="300" height="300"/> 
</td></tr>
</table>
</div>

- The second rotation is $\theta$ around the new y-axis

<div align="center">
<table class="image">
<tr><td><img src="./img/euler_angle_step_2.png"
alt="Euler Angle Second Rotation" title="Euler Angle Second Rotation"
width="300" height="300"/> 
</td></tr>
</table>
</div>

- Last rotation is $\phi$ around the new x-axis

<div align="center">
<table class="image">
<tr><td><img src="./img/euler_angle_step_3.png"
alt="Euler Angle Third Rotation" title="Euler Angle Third Rotation"
width="300" height="300"/> 
</td></tr>
</table>
</div>

- Careful with the second and third rotations as they are around the NEW
  axis formed from the previous rotations
- We now have 4 different coordinate systems fixed in four different reference
  frames
    - $A \Rightarrow \left{\underline{E}_{x}, \underline{E}_{y},
      \underline{E}_{z}\right}$
    - $R \Rightarrow \left{\underline{e}_{x}, \underline{e}_{y},
      \underline{e}_{z}\right}$
    - $P \Rightarrow \left{\underline{p}_{x}, \underline{p}_{y},
      \underline{p}_{z}\right}$
    - $Q \Rightarrow \left{\underline{q}_{x}, \underline{q}_{y},
      \underline{q}_{z}\right}$
- We can now define the angular velocity of the final, body frame as seen by
  the initial frame as:
    - $^{A}\underline{\omega}^{R} = ^{A}\underline{\omega}^{P} +
      ^{P}\underline{\omega}^{Q} + ^{Q}\underline{\omega}^{R}$ $=
      \dot{\psi}\underline{p}_{z} + \dot{\theta}\underline{q}_{2} +
      \dot{\phi}\underline{e}_{x}$
- Due to the fact that the rotations can often be measured in reference frame R
  by gyroscopes, it is often desired to have the angular velocity defined in
  that coordinate system
    - $^{A}\underline{\omega}^{R} = (\dot{\phi} - \dot{\psi}sin\theta)
      \underline{e}_{x} + (\dot{\psi}cos\theta sin\phi +$ $\dot{\theta}cos\phi)
      \underline{e}_{y} + (\dot{\psi}cos\theta cos\phi - \dot{\theta}sin\phi)
      \underline{e}_{z}$

> ### Limitations of Euler Angles

> - For each sequence of rotations there is a rotation that will result in a
    singularity where there is an infinite combination of values for the first
    two rotations to arrive at that same orientation
>       - For a 321 sequence for example there is a singularity for a 90 degree
          rotation as the second rotation causing an infinite number of
          combinations of $\psi$ and $\phi$ to arrive at the same final
          orientation
> - Singularities basically occur when the same axis in space is reused

## Intrinsic Coordinates {#intrinsic_coordinates}

- An intrinsic coordinate system is one that is based within the motion and
  trajectory of a particle
    - If there's no motion there can not be an intrinsic coordinate system
- The three unit vectors of an intrinsic coordinate system are the tangential
  vector ($\underline{e}_{t}$), the principal normal to the trajectory
  ($\underline{e}_{n}$) and the principal binormal to the trajectory
  ($\underline{e}_{b}$)
- When defined for a using the motion of point P in the general reference frame
  A the three vectors are defined as:
    - $\underline{e}_{t} = \frac{^{A}\underline{V}_{P}}{\|
      ^{A}\underline{V}_{P} \|}$
    - $\underline{e}_{n} = \frac{ \frac{^{A}d}{dt} \underline{e}_{t}}{\|
      \frac{^{A}d}{dt} \underline{e}_{t} \|}$
    - $\underline{e}_{b} = \underline{e}_{t} \times \underline{e}_{n}$
- Vector $\underline{e}_{n}$ points to the center of curvature of the
  trajectory of point P in reference frame A and so difficulties can be
  encountered when the trajectory is a straight line

## Motion Between Two Points in the Same Reference Frame {#motion_two_points}

- For two points Q and P in the same rigid body, a relation can be derived for
  their velocities and accelerations
- For general reference frame A the position vector between points Q and P
  fixed in reference frame R can be given as:
    - $\underline{r}_{^{Q}/_{P}} = \underline{r}_{Q} - \underline{r}_{P}$
- Now taking the time derivative of $\underline{r}_{^{Q}/_{P}}$ in the A
  reference frame and including the transport theorem between the A reference
  frame and the R reference frame leads to the following expression
    - $\frac{^{A}d}{dt} \underline{r}_{^{Q}/_{P}} =
      \frac{^{A}d}{dt}(\underline{r}_{Q} - \underline{r}_{P})$
    - $^{A}\underline{V}_{Q} - ^{A}\underline{V}_{P} =
      \frac{^{R}d}{dt}\underline{r}_{^{Q}/_{P}} + ^{A}\underline{\omega}^{R}
      \times (\underline{r}_{Q} - \underline{r}_{P})$
- Noting that the distance between points Q and P do not change by definition
  of a rigid body the first term on the right hand side of the above expression
  equals zero
    - $^{A}\underline{V}_{Q} - ^{A}\underline{V}_{P} =
      ^{A}\underline{\omega}^{R} \times (\underline{r}_{Q} -
      \underline{r}_{P})$
- By taking another time derivative of the above expression the difference in
  accelerations of the two points can be obtained
    - $^{A}\underline{a}_{Q} - ^{A}\underline{a}_{P} = \frac{^{A}d}{dt}
      [^{A}\underline{\omega}^{R} \times (\underline{r}_{Q} -
      \underline{r}_{P})]$
    - $^{A}\underline{a}_{Q} - ^{A}\underline{a}_{P} = \frac{^{A}d}{dt}
      (^{A}\underline{\omega}^{R}) \times (\underline{r}_{Q} -
      \underline{r}_{P})$ $+ ^{A}\underline{\omega}^{R} \times \frac{^{A}d}{dt}
      (\underline{r}_{Q} - \underline{r}_{P})$
- Now keeping in mind that $\frac{^{A}d}{dt} (^{A}\underline{\omega}^{R})$ is
  the angular acceleration $^{A}\underline{\alpha}^{R}$ and that
  $\frac{^{A}d}{dt} (\underline{r}_{Q} - \underline{r}_{P})$ is the velocity
  expression that has already been found, the acceleration expression can be
  simplified to the following expression
    - $^{A}\underline{a}_{Q} - ^{A}\underline{a}_{P} =
      ^{A}\underline{\alpha}^{R} \times (\underline{r}_{Q} - \underline{r}_{P})
      +$ $^{A}\underline{\omega}^{R} \times \left[ ^{A}\underline{\omega}^{R}
      \times (\underline{r}_{Q} - \underline{r}_{P}) \right]$
    - It is important to remember that cross products are not commutative and
      that the order in which they are performed is important

## Rolling and Slipping {#rolling_and_slipping}

- The condition for rolling between two rigid bodies R and S in a general
  reference frame is the following expression
    - $^{A}\underline{V}^{R}_{C} = ^{A}\underline{V}^{S}_{C}$ where point C is
      the point of contact between rigid bodies R and S
- Sliding between two rigid bodies occurs anytime the rolling condition is not
  met
- Note that when considering rolling motion there are three point C's to
  consider
    1. The instantaneous point of contact between the two rigid bodies which
       doesn't belong to either body
    2. The point C belonging to rigid body R
    3. The point C belonging to rigid body S
- Therefore in the above condition for rolling the term
  $^{A}\underline{V}^{R}_{C}$ stands for the velocity of point C belonging to
  rigid body R in reference frame A

## Inertial Reference Frames {#inertial_ref_frames}

- An inertial reference frame is one for which we will assume exists as a set
  of absolutely stationary points
- Inertial reference frames are an imaginary concept that is an approximation
  of reality since all motion is relative the question arises to whom are the
  set of points stationary
- We can pick reference frames to be our inertial reference frame when the
  degree of motion of the points is negligible compared to the motion that we
  are studying

## Three Laws of Mechanics {#three_laws_of_mechanics}

- When studying kinetics there the particles are no longer massless and we are
  considering the effect of action on the particles (forces/vectors)

1. The first law of mechanics or the inertia law states that an object at rest
   tends to remain at rest and an object in motion tends to remain in motion
2. The second law of mechanics relates forces to momentum as it's most common
   form shows ($\underline{F} = m ^{N}\underline{a}$ where $^{N}\underline{a}$
   is the acceleration in an inertial reference frame)
3. The last of the three laws of mechanics states that for every action there
   is an equal and opposite reaction
    - If the resultant force lies on the same line of action as the initial
      force (sliding vectors) then it is considered the strong form of the 3rd
      law
    - The weak form of the third law is when the resultant force and the
      initial force are not on the same line of action

## Angular Momentum {#angular_momentum}

- Some problems are easier to solve by using the concept of angular momentum
  where the definition of angular momentum for a particle P about point Q is
  given as
    - $^{N}\underline{H}_{Q} =(\underline{r}_{P} - \underline{r}_{Q}) \times m
      (^{N}\underline{V}_{P} - ^{N}\underline{V}_{Q})$ where $\underline{P}$
      and $\underline{Q}$ are measured relative to the origin of N and m is the
      mass of particle P
- Another useful relation from the angular momentum is the time rate of change
  of the angular momentum
    - $\frac{d}{dt}(^{N}\underline{H}_{Q}) = (^{N}\underline{V}_{P} -
      ^{N}\underline{V}_{Q}) \times m(^{N}\underline{V}_{P} -
      ^{N}\underline{V}_{Q})$ $+ (\underline{r}_{P} - \underline{r}_{Q}) \times
      m(^{N}\underline{a}_{P} - ^{N}\underline{a}_{Q})$
    - Note that the first term involves taking the cross product of a vector
      with the same vector and is therefore zero and so the expression can be
      rewritten as 
        - $\frac{d}{dt}(^{N}\underline{H}_{Q}) =$ $(\underline{r}_{P} -
          \underline{r}_{Q}) \times m(^{N}\underline{a}_{P} -
          ^{N}\underline{a}_{Q})$
- The above expression can as the cross product of the distance between the two
  points with each acceleration individually
    - $\frac{d}{dt}(^{N}\underline{H}_{Q}) = (\underline{r}_{P} -
      \underline{r}_{Q}) \times m ^{N}\underline{a}_{P} - (\underline{r}_{P} -
      \underline{r}_{Q}) \times m ^{N}\underline{a}_{Q}$
    - Since m is the mass of particle P the term $m ^{N}\underline{a}_{P}$ is
      the sum of forces $^{N}\underline{F}$ acting on point P by Newton's third
      law of mechanics
        - $\frac{d}{dt}(^{N}\underline{H}_{Q}) = (\underline{r}_{P} -
          \underline{r}_{Q}) \times ^{N}\underline{F} -
          (\underline{r}_{P} - \underline{r}_{Q}) \times m
          ^{N}\underline{a}_{Q}$
- The term $(\underline{r}_{P} - \underline{r}_{Q}) \times ^{N}\underline{F}$
  is the moment of all of the forces acting on particle P with respect to point
  Q and so the expression can be rewritten one more time as the following
    - $\frac{d}{dt}(^{N}\underline{H}_{Q}) = \underline{M}_{Q} -
      (\underline{r}_{P} - \underline{r}_{Q}) \times m ^{N}\underline{a}_{Q}$

## Relative Velocity {#relative_velocity}

- Relative velocity is the vector that represents the motion of one point
  compared to another
- For two points P and Q the relative velocity can be expressed as follows
    - $\underline{V}_{rel} = ^{A}\underline{V}_{P} - ^{A}\underline{V}_{Q}$
    - Note that the relative velocity is reference frame independent
        - $^{A}\underline{V}_{P} - ^{A}\underline{V}_{Q} =
          ^{B}\underline{V}_{P} - ^{B}\underline{V}_{Q}$

## Friction Force Models {#friction_force_models}

- Irregardless of the model the friction force $\underline{F}_{f}$ will oppose
  the relative motion between two surfaces
    - Caution as it may not oppose the direction of overall motion of the
      object

> __Coulomb Friction__

> - $\underline{F}_{f} = -\mu \| \underline{R} \| \frac{\underline{V}_{rel}}{\|
    \underline{V}_{rel} \|}$ 
>       - $\underline{R}$ is the resultant force normal to the point of contact
>       - $\mu =$ coefficient of friction

> __Viscous Friction__

> - $\underline{F}_{f} = -c\underline{V}_{rel}$
>       - $c =$ coefficient of vicsous friction

## Linear Spring Force Model {#linear_spring_force_model}

- For particle $P$ with mass $m$ and point $Q$ being connected by a linear
  spring the force model can be written as follows
    - $\underline{F}_{s} = -k(\el - \el_{0})\underline{u}_{s}$
        - $\el = \| \underline{r} - \underline{Q} \|$
        - $\el_{0} =$ the spring length when it is unstreched/uncompressed
        - $k =$ the spring constant
        - $\underline{u}_{s} = \frac{\underline{r}_{P} - \underline{r}_{Q}}{\|
          \underline{r}_{P} - \underline{r}_{Q} \|}$


## Center of Mass {#center_of_mass}

- Whether working with a system of particles or a rigid body the center of mass
  is an important point to know the position of while trying to solve problems
- For a system of particles the center of mass is found by taking the sum of
  the mass of individual particles multiplied by their position vectors and
  dividing by the overall mass of the system
    - $\underline{\bar{r}} = \frac{\sum m_{i}\underline{r}_{i}}{\sum m_{i}}$
- Finding the center of mass of a rigid body is practically the same process
  but due to the rigid body having potentially infinite points with mass the
  sum in the above expression naturally turns into an integral
    - $\underline{\bar{r}} = \frac{\int_{R} \underline{r} dm}{\int_{R} dm}$
- Additional quantities that are useful are the velocity and acceleration of
  the center of mass and these quantities are easy to find when considering
  that the mass of the system/rigid body is not time dependent
    - For a system of particles
        - $^{N}\underline{\bar{V}} = \frac{\sum
          m_{i}^{N}\underline{V}_{i}}{\sum m_{i}}$
        - $^{N}\underline{\bar{a}} = \frac{\sum
          m_{i}^{N}\underline{a}_{i}}{\sum m_{i}}$
    - For a rigid body
        - $^{N}\underline{\bar{V}} = \frac{\int_{R} (^{N}\underline{V})
          dm}{\int_{R} dm}$
        - $^{N}\underline{\bar{a}} = \frac{\int_{R} (^{N}\underline{a})
          dm}{\int_{R} dm}$

## Tensors {#tensors}

- Tensors are geometrical objects similar to vectors
- Tensors are reference frame independent
- Letting $\underline{b}$ be a vector in $E^{3}$, we define a tensor
  $\underline{\underline{T}}$ as a linear operator which takes vectors as
  inputs and returns vectors
    - An example of a tensor that has been used often in this class already is
      the cross product
- If a tensor is represented by a matrix it must include a basis or it is not a
  tensor just a matrix
- A tensor is represented as operating on a vector by a large dot 
    - $\underline{\underline{T}} \bullet \underline{b}$
    - Tensor $\underline{\underline{T}}$ operating on vector $\underline{b}$

> __Tensor Product__

> - One common operation that will need to be defined is that of the tensor
    product
>       - $\left( \underline{a} \otimes \underline{b} \right) \bullet
          \underline{c} =$ $\left( \underline{c} \cdot \underline{b})
          \underline{a}$
>       - $\underline{a} \otimes \underline{b}$ is the tensor
>       - The dot on the right hand side is a dot product not an "operates on"
          operator therefore the result is a scalar multiplied by the
          $\underline{a}$ vector
> - Example of the tensor created by $\underline{a} \otimes \underline{b}$
>       - $\underline{a} = a_{1} \underline{e}_{1} + a_{2} \underline{e}_{2} +
          a_{3} \underline{e}_{3}$
>       - $\underline{b} = b_{1} \underline{e}_{1} + b_{2} \underline{e}_{2} +
          b_{3} \underline{e}_{3}$
>       - $\underline{a} \otimes \underline{b} = a_{1} b_{1} (e_{1} \otimes
          e_{1}) + a_{1} b_{2} (e_{1} \otimes e_{2}) + a_{1} b_{3} (e_{1}
          \otimes e_{3}) +$ $a_{2} b_{1} (e_{2} \otimes e_{1}) + a_{2} b_{2}
          (e_{2} \otimes e_{2}) + a_{2} b_{3} (e_{2} \otimes e_{3}) +$ $a_{3}
          b_{1} (e_{3} \otimes e_{1}) + a_{3} b_{2} (e_{3} \otimes e_{2}) +
          a_{3} b_{3} (e_{3} \otimes e_{3})$

## Angular Momentum of Rigid Bodies/Systems of Particles {#angular_momentum2}

- For a system of particles the angular momentum about point Q is given by the
  following expression. The first time derivative of the angluar momentum for a
  system of particles is also presented
    - $^{N}\underline{H}_{Q} = \sum_{i=1}^{n} (\underline{r}_{i} -
      \underline{r}_{Q}) \times m_{i}(^{N}\underline{V}_{i} -
      ^{N}\underline{V}_{Q})$
    - $\frac{^{N}d}{dt} (^{N}\underline{H}_{Q}) = \underline{M}_{Q} -
      (\underline{\bar{r}} - \underline{r}_{Q}) \times m ^{N}\underline{a}_{Q}$
        - Where $\underline{M}_{Q}$ is the real moment given by
          $\sum_{i=1}^{n}(\underline{r}_{i} - \underline{r}_{Q}) \times
          \underline{F}_{i}$
- For a rigid body the angular momentum about point Q is given by the following
  expression. The first time derivative of the angular momentum expression is
  also provided
    - $^{N}\underline{H}_{Q} = \int_{R} \left[ (\underline{r} -
      \underline{r}_{Q}) \times (^{N}\underline{V} - ^{N}\underline{V}_{Q})
      \right] dm$ for generic point $Q$
    - $^{N}\underline{H}_{B} = (^{N}\underline{\underline{I}}_{B}^{R})
      \bullet (^{N}\underline{\omega}^{R})$ where $B$ is on rigid body $R$
    - $^{N}\underline{\bar{H}} = (^{N}\underline{\underline{\bar{I}}}) \bullet
      (^{N}\underline{\omega}^{R})$ if $B$ is the center of mass
        - $(^{N}\underline{\underline{\bar{I}}})$ can be found in tables in
          text books for general shapes/configurations
    - The generic expression of angular momentum of a rigid body about generic
      point Q can be found from the angular momentum about its center of mass
      from the following expression
        - $^{N}\underline{H}_{Q}  -  ^{N}\underline{\bar{H}} =
          (\underline{r}_{Q} - \underline{\bar{r}}) \times m
          (^{N}\underline{V}_{Q} - ^{N}\underline{\bar{V}})$
            - The parallel axis theorem can be found from this expression but
              this is a stronger expression and as such should stick to this
              one instead

## Pure Torque {#pure_torque}

- Pure torque is a moment on a rigid body that is independent of the point on
  the body for which the moment is being determined
- Can be represented by a force couple which creates a moment with zero net
  force
- Symbolically represented as $\tau$
- Including pure torque in the expression for the sum of moments for a system
  of particles about generic point Q yields the following expression
    - $\underline{M}_{Q} = \sum_{i=1}^{n} (\underline{r}_{i} -
      \underline{r}_{Q}) \times \underline{F}_{i} + \tau$

## Euler's Laws {#eulers_laws}

> __First Law__

> - $\underline{F} = m ^{N}\underline{\bar{a}}$
>       - Where N is inertial

> __Second Law__

> - $\underline{M}_{O} = \frac{^{N}d}{dt} (^{N}\underline{H}_{O})$
>       - Where O is a point that is inertially fixed
> - When moved to a generic point that does not have to be inertially fixed the
    second law becomes the following
>       - $\frac{^{N}d}{dt} (^{N}\underline{H}_{Q}) = \underline{M}_{Q} +
          (\underline{r}_{Q} - \underline{\bar{r}}) \times m
          ^{N}\underline{a}_{Q}$

## Parameterize a Problem {#parameterize_prob}

- When looking at how to parameterize a problem we first must consider the
  degrees of freedom (M) the system has and how many of those degrees are
  constrained (P)

## Lagrange Equations {#lagrange_equations}

- Lagrange equations provide a means of formulating problems without forces
  caused by constraints on the system
- Lagrange equations are derived from Newton's Second Law ($\underline{F} = m
  ^{N}\underline{a}$)
- We will need the different expressions for kinetic energy when working with
  Lagrange Equations

> __Kinetic Energy of a Particle__

> - $T = \frac{1}{2} m (^{N}\underline{V}) \cdot (^{N}\underline{V})$

> __Kinetic Energy for a System of Particles__

> - $T = \sum_{J=1}^{n} (\frac{1}{2} m_{J}) (^{N}\underline{V}_{J}) \cdot
    (^{N}\underline{V}_{J})$ 

> __Kinetic Energy for a Rigid Body (Koenig Decomposition)__

> - $T = \frac{1}{2} m \underline{\bar{V}} \cdot \underline{\bar{V}} +
    \frac{1}{2} \underline{\bar{H}} \cdot (^{N}\underline{\omega}^{R})$

- The _Fundamental Form of Lagrange's Equations_ is the following expression
    - $\frac{d}{dt} \left( \frac{\partial T}{\partial \dot{q}_{i}} \right) -
      \frac{\partial T}{\partial q_{i}} = \underline{F} \cdot \frac{\partial
      \underline{r}}{\partial q_{i}}$
<br></br>

- Lagrange's Equation for a rigid body is given by the following expression
    - $\frac{d}{dt} \left(\frac{\partial T}{\partial \dot{q}_{i}} \right)$ $-
      \frac{\partial T}{\partial q_{i}} = Q_{i}$
    - where
        - $Q_{i} = \underline{F} \cdot \frac{\partial
          \underline{\dot{\bar{r}}}}{\partial \dot{q}_{i}} +
          \underline{\bar{M}} \cdot \frac{\partial
          ^{N}\underline{\omega}^{R}}{\partial \dot{q}_{i}}$ for i = 1, ..., 6
        - $\underline{F} = \sum_{J=1}^{k} \underline{F}_{J}$
        - $\underline{M} = \sum_{J=1}^{m} \underline{M}_{J}$

## Examples {#examples}

> ### Examples Content

>> #### Kinematics

>> - [Transport Theorem](#e_transport_theorem)
>> - [Cylindrical Coordinate System](#e_cylindrical_coor_sys)
>> - [Spherical Coordinate System](#e_spherical_coor_sys)
>> - [Intrinsic Coordinate System](#e_intrinsic_coor_sys)
>> - [Rolling Motion](#e_rolling_motion)

>> #### Kinetics

>> - [Basic Equation of Motion](#e_basic_equation_of_motion)
>> - [Angular Momentum](#e_angular_momentum)
>> - [Friction Force Models](#e_friction_force_models)
>> - [Linear Spring Force Models](#e_linear_spring_force_models)

>> #### Kinetics for a System of Particles

>> - [Basic System of Particles](#basic_sys_of_particles)
>> - [Angular Momentum](#sys_of_particles_angular_momentum)

>> #### Kinetics for Rigid Bodies

>> - [Basic Rigid Body Problem](#basic_rigid_body)
>> - [Gyroscope Example](#gyroscope)
>> - [Pendulum Example](#pendulum)

> ### Transport Theorem Examples {#e_transport_theorem}

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
>>      - $\underline{e}_{\theta}$ = $\underline{e}_{z} \times
          \underline{e}_{r}$

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
>>>     - $^{G}\underline{V}_{P} = \frac{^{G}d\underline{r}}{dt}$ $=
          -r\dot{\theta}sin(\theta)\underline{E}_{x} +
          r\dot{\theta}cos(\theta)\underline{E}_{y}$

>>> - The second approach involves leaving the equations with terms referenced
      in the disk reference frame and uses the transport theorem
>>>     - $^{G}\underline{V}_{P} = (^{D}\underline{V}_{P}) +
          ^{G}\underline{\omega}^{D} \times \underline{r}$
>>>         - $^{D}\underline{V}_{P} = 0$
>>>         - $^{G}\underline{\omega}^{D} =\dot{\theta}\underline{e}_{z}$
>>>         - $\underline{r} = r\underline{e}_{r}$
>>>     - $^{G}\underline{V}_{P} = \dot{\theta}\underline{e}_{z} \times
          r\underline{e}_{r} = \dot{\theta}r\underline{e}_{\theta}$

>> - The second approach leaves a much cleaner equation for further derivatives
     and so this is the form we'll use when finding the acceleration
>>      - $^{G}a_{P} = \frac{^{G}d}{dt}(^{G}\underline{V}_{P}) =
          \frac{^{D}d}{dt}(^{G}\underline{V}_{P}) + ^{G}\underline{\omega}^{D}
          \times$ $^{G}\underline{V}_{P} = \ddot{\theta}r\underline{e}_{\theta}
          + \dot{\theta}\underline{e}_{z} \times
          \dot{\theta}r\underline{e}_{\theta}$ $=
          \ddot{\theta}r\underline{e}_{\theta} -
          \dot{\theta}^{2}r\underline{e}_{r}$

> - __Second Transport Theorem Example:__

>> - This example is the same as the previous one execept it has an additional
     rotation $\beta$ around its base
>> - It's good practice to have an additional reference frame for each rotation
     and so in this example we'll use three reference frames: disk (D), disk at
     $\theta = 0$ (C) and the ground (G)

<div align="center">
<table class="image">
<tr><td><img src="./img/trans_theo_example2_diagram1.png"
alt="Example 2, Diagram 1" title="Example 2, Diagram 1" width="200"
height="200"/> 
</td></tr>
</table>
</div>

>> - Always start by defining the reference frames and then the coordinate
     systems within them
>> - Coordinate system fixed in the disk reference frame (D)
>>      - Origin at point O
>>      - $\underline{u}_{r}$ = along $\underline{OP}$
>>      - $\underline{u}_{z}$ = perpendicular to the disk, positive with
          $\theta$
>>      - $\underline{u}_{\theta}$ = $\underline{u}_{z} \times
          \underline{u}_{r}$

<div align="center">
<table class="image">
<tr><td><img src="./img/disk_ref_frame2.png"
alt="Disk Reference Frame 2" title="Disk Reference Frame 2" width="125"
height="125"/> 
</td></tr>
</table>
</div>

>> - Coordinate system fixed in the ground reference frame (G)
>>      - Origin at point O
>>      - $\underline{E}_{z}$ = Out of the page
>>      - $\underline{E}_{x}$ = along the line $\underline{OP}$ @ $\theta = 0$,
          $\beta = 0$
>>      - $\underline{E}_{y}$ = $\underline{E}_{z} \times \underline{E}_{x}$

<div align="center">
<table class="image">
<tr><td><img src="./img/ground_ref_frame.png"
alt="Ground Reference Frame" title="Ground Reference Frame" width="200"
height="200"/> 
</td></tr>
</table>
</div>

>> - Coordinate system fixed in the disk at $\theta = 0$ reference frame (C)
     (rotates with $\beta$)
>>      - Origin at point O
>>      - $\underline{e}_{\theta} = \underline{E}_{y}$
>>      - $\underline{e}_{r}$ = along $\underline{OP}$ at $\theta = 0$
>>      - $\underline{e}_{z}$ = $\underline{u}_{z}$

<div align="center">
<table class="image">
<tr><td><img src="./img/disk_ref_frame3.png"
alt="Disk Reference Frame Fixed with Theta = 0" title="Disk Reference Frame
Fixed with Theta = 0" width="200" height="200"/> 
</td></tr>
</table>
</div>

>> - Just as in the previous example the velocity and acceleration in the disk
     reference frame (D) will equal zero
>>      - $^{D}\underline{V}_{P} = (^{D}\underline{a}_{P}) = 0$

>> - Now to find the velocity of point P in the ground reference frame we
     are going to take advantage of the transport theorem again
>>      - $\underline{r} = r\underline{u}_{r}$
>>      - $^{G}\underline{\omega}^{C} = \dot{\beta}\underline{e}_{\theta}$
>>      - $^{C}\underline{\omega}^{D} = \dot{\theta}\underline{u}_{z}$
>>      - $^{G}\underline{V}_{P} = \frac{^{G}d\underline{r}}{dt}$ $=
          \frac{^{D}d\underline{r}}{dt} + ^{G}\underline{\omega}^{D} \times
          \underline{r}$
>>          - $^{G}\underline{V}_{P} = ^{D}\underline{V}_{P} +
              (^{G}\underline{\omega}^{C} + ^{C}\underline{\omega}^{D}) \times
              \underline{r}$
>>          - $^{G}\underline{V}_{P} = 0 + (\dot{\beta}\underline{e}_{\theta} +
              \dot{\theta}\underline{u}_{z}) \times (r\underline{u}_{r})$
>>          - $^{G}\underline{V}_{P} =
              [\dot{\beta}(cos(\theta)\underline{u}_{\theta} +
              sin(\theta)\underline{u}_{r}) + \dot{\theta}\underline{u}_{z}]
              \times (r\underline{u}_{r})$
>>          - $^{G}\underline{V}_{P} =
              -\dot{\beta}cos(\theta)r\underline{u}_{z} +
              \dot{\theta}r\underline{u}_{\theta}$

> ### Cylindrical Coordinate System Example {#e_cylindrical_coor_sys}

> - Find the equation for the velocity and acceleration of point P in the A
    reference frame ($^{A}\underline{V}_{P}, ^{A}\underline{a}_{P}$)
> - For this problem we will use two different approaches:
>       - The first approach will be to derive the velocity and acceleration
          using a coordinate system fixed in reference frame A
>       - The second approach will be to develop and use a cylindrical
          coordinate system fixed in a reference frame C

> - For the first approach the reference frame is already defined in the
    following figure

<div align="center">
<table class="image">
<tr><td><img src="./img/cylindrical_coor_sys.png"
alt="Cylindrical Coordinate System" title="Cylindrical Coordinate System"
width="300" height="300"/> 
</td></tr>
</table>
</div>

> - The vector $\underline{r}$ will be defined in these coordinates as
    $\underline{r} = x\underline{E}_{x} + y\underline{E}_{y} +
    z\underline{E}_{z}$
> - We can now find $^{A}\underline{V}_{P}$
>       - $^{A}\underline{V}_{P} = \frac{^{A}d\underline{r}}{dt} =
          \dot{x}\underline{E}_{x} + \dot{y}\underline{E}_{y} +
          \dot{z}\underline{E}_{z}$
> - The same process can be used to find $^{A}a_{P}$
>       - $^{A}\underline{a}_{P} = \frac{^{A}d}{dt}(^{A}\underline{V}_{P}) =
          \ddot{x}\underline{E}_{x} + \ddot{y}\underline{E}_{y} +
          \ddot{z}\underline{E}_{z}$

> - For the second approach we need more formal clarifications of our reference
    frames and coordinate systems
>       - We will be using two reference frames: reference frame A in which the
          {$\underline{E}_{x}, \underline{E}_{y}, \underline{E}_{z}$} are
          already fixed and reference frame B which is the plane containing
          points O, P and Q (or vectors $r$ and $\underline{r}$)
> - Coordinate system fixed in reference frame B (Cylindrical Coordinates)
>       - Origin at point O
>       - $\underline{e}_{r}$ = along line $\underline{OQ}$
>       - $\underline{e}_{z}$ = $\underline{E}_{z}$
>       - $\underline{e}_{\theta}$ = $\underline{e}_{z} \times
          \underline{e}_{r}$

<div align="center">
<table class="image">
<tr><td><img src="./img/e_cylindrical_coor_sys.png"
alt="Cylindrical Coordinate System Example" title="Cylindrical Coordinate
System Example" width="300" height="300"/> 
</td></tr>
</table>
</div>

> - Now we're going to define $\underline{r}$ in the cylindrical coordinates
    (in reference frame B)
>       - $\underline{r} = r\underline{e}_{r} + z\underline{e}_{z}$
> - We can now find $^{A}\underline{V}_{P}$ using the cylindrical coordinates
>       - $^{A}\underline{V}_{P} = \frac{^{A}d\underline{r}}{dt} =
          \frac{^{B}d\underline{r}}{dt} + ^{A}\underline{\omega}^{B} \times
          \underline{r}$
>       - $^{A}\underline{V}_{P} = \dot{r}\underline{e}_{r} +
          \dot{z}\underline{e}_{z} + (\dot{\theta}\underline{e}_{z}) \times
          (r\underline{e}_{r} + z\underline{e}_{z})$
>       - $^{A}\underline{V}_{P} = \dot{r}\underline{e}_{r} +
          \dot{z}\underline{e}_{z} + \dot{\theta}r\underline{e}_{\theta}$
> - Now that we have the velocity we can find the acceleration
>       - $^{A}\underline{a}_{P} = \frac{^{A}d}{dt}(^{A}\underline{V}_{P}) =
          \frac{^{B}d}{dt}(^{A}\underline{V}_{P}) + ^{A}\underline{\omega}^{B}
          \times ^{A}\underline{V}_{P}$
>       - $^{A}\underline{a}_{P} = \frac{^{A}d}{dt}(\dot{r}\underline{e}_{r} +
          \dot{z}\underline{e}_{z} + \dot{\theta}r\underline{e}_{\theta})$ $+
          \dot{\theta}\underline{e}_{z} \times (\dot{r}\underline{e}_{r} +
          \dot{z}\underline{e}_{z} + \dot{\theta}r\underline{e}_{\theta})$
>       - $^{A}\underline{a}_{P} = \ddot{r}\underline{e}_{r} +
          \ddot{z}\underline{e}_{z} + (\ddot{\theta}r +
          \dot{\theta}\dot{r})\underline{e}_{\theta}$ $+
          \dot{\theta}\dot{r}\underline{e}_{\theta} +
          \dot{\theta}^{2}r\underline{e}_{r}$

> ### Spherical Coordinate System Example {#e_spherical_coor_sys}

> - The problem is to find the velocity and acceleration of point P in the A
    reference frame ($^{A}\underline{V}_{P}$ and $^{A}\underline{V}_{P}$)
> - Since the example for cylindrical coordinate systems already found the
    expression using the coordinate system in reference frame A and using the
    cylindrical coordinate system, this example will only be using the
    spherical coordinate system approach

<div align="center">
<table class="image">
<tr><td><img src="./img/spherical_coor_sys.png"
alt="Spherical Coordinate System" title="Spherical Coordinate System"
width="300" height="300"/> 
</td></tr>
</table>
</div>

> - In order to define the spherical coordinate system three reference frames
    will be used:
>       - The given reference frame (A)
>       - The reference frame fixed in the plane containing points O, P and Q
          (or vectors $r$ and $\underline{r}$) (B)
>       - The reference frame fixed in the plane containing vector
          $\underline{r}$ that is perpendicular to the plane containing vectors
          $\underline{E}_{z}$ and $\underline{r}$ (C)
> - Coordinate system in reference frame A is already given $A \right
    \left{E_{x},E_{y},E_{z}\right}$ and origin at point O
> - Coordinate system fixed in reference frame B (Cylindrical Coordinates)
>       - Origin at point O
>       - $\underline{e}_{r}$ = along line $\underline{OQ}$
>       - $\underline{e}_{z}$ = $\underline{E}_{z}$
>       - $\underline{e}_{\theta}$ = $\underline{e}_{z} \times
          \underline{e}_{r}$

<div align="center">
<table class="image">
<tr><td><img src="./img/e_cylindrical_coor_sys.png"
alt="Cylindrical Coordinate System Example" title="Cylindrical Coordinate
System Example" width="300" height="300"/> 
</td></tr>
</table>
</div>

> - Coordinate system fixed in referenc frame C (Spherical Coordinates)
>       - Origin at point O
>       - $\underline{u}_{r} = \frac{\underline{r}}{\| \underline{r} \|}$
>       - $\underline{u}_{\theta} = \underline{e}_{\theta}$
>       - $\underline{u}_{\phi} = \underline{u}_{\theta} \times
          \underline{u}_{r}$

<div align="center">
<table class="image">
<tr><td><img src="./img/e_spherical_coor_sys.png"
alt="Spherical Coordinate System" title="Spherical Coordinate System"
width="300" height="300"/> 
</td></tr>
</table>
</div>

> - First note that the angular accelertation between reference frames A and C
    can be expressed as
>       - $^{A}\underline{\omega}^{C} = ^{A}\underline{\omega}^{B} +
          ^{B}\underline{\omega}^{C}  = \dot{\theta} \underline{e}_{z} +
          \dot{\phi} \underline{u}_{\theta}$
> - Now we can find the velocity of point P in the A reference frame by making
    use of the transport theorem and the following definition of
    $\underline{r}$: $\underline{r}_{P} = p \underline{u}_{r}$
>       - $^{A}\underline{V}_{P} = \frac{^{C}d\underline{r}_{P}}{dt} +
          ^{A}\underline{\omega}^{C} \times \underline{r}_{P}$ $=
          \frac{^{C}d}{dt} (p \underline{u}_{r}) +
          (\dot{\theta}\underline{e}_{z} + \dot{\phi}\underline{u}_{\theta})
          \times (p \underline{u}_{r})$
>       - $^{A}\underline{V}_{P} = \dot{p} \underline{u}_{r} + (\dot{\theta}
          (cos\phi \underline{u}_{r} - sin\phi \underline{u}_{\phi}) +
          \dot{\phi} \underline{u}_{\theta}) \times p \underline{u}_{r}$
>       - $^{A}\underline{V}_{P} = \dot{p} \underline{u}_{r} + \dot{\theta} p$
          $sin\phi \underline{u}_{\theta} + \dot{\phi} p \underline{u}_{\phi}$
> - The same process can be used to find the acceleration of point P in
    reference frame A, however, the expression becomes very large and so it
    will be omitted here for space

> ### Intrinsic Coordinate System Example {#e_intrinsic_coor_sys}

<div align="center">
<table class="image">
<tr><td><img src="./img/e_intrinsic_coordinate_sys.png"
alt="Intrinsic Coordinate System" title="Intrinsic Coordinate System"
width="300" height="300"/> 
</td></tr>
</table>
</div>

> - Given the above set up find the intrinsic coordinate system for point P
> - To begin the velocity and acceleration of point P will be found in
    reference frame A
> - Two different reference frames will be used: the given reference frame (A)
    and the reference frame using the plane containing vectors $\underline{OP}$
    and $\underline{E}_{z}$
> - Coordinate system fixed in reference frame A
>       - Origin at O
>       - $\underline{E}_{x} =$ to the right
>       - $\underline{E}_{z} =$ out of the page
>       - $\underline{E}_{y} = \underline{E}_{z} \times \underline{E}_{x}$

> - Coordinate system fixed in reference frame B
>       - Origin at O
>       - $\underline{e}_{r} =$ along $\underline{OP}$
>       - $\underline{e}_{z} = \underline{E}_{z}$
>       - $\underline{e}_{\theta} = \underline{e}_{z} \times \underline{e}_{r}$

> - Now we can find the velocity of point P in reference frame A using
    $\underline{r} = sin\theta \underline{e}_{r}$
>       - $^{A}\underline{V}_{P} = \frac{^{A}d}{dt}(sin\theta
          \underline{e}_{r}) = \frac{^{B}d}{dt}(sin\theta \underline{e}_{r}) +
          ^{A}\underline{\omega}^{B} \times (sin\theta \underline{e}_{r})$
>       - $^{A}\underline{V}_{P} = \dot{\theta}cos\theta \underline{e}_{r} +
          \dot{\theta}\underline{e}_{z} \times sin\theta \underline{e}_{r}$
>       - $^{A}\underline{V}_{P} = \dot{\theta}\cos\theta \underline{e}_{r} +
          \dot{\theta}sin\theta \underline{e}_{\theta}$
> - Now the that the velocity has been found the acceleration of point P in
    reference frame A can be found
>       - $^{A}\underline{a}_{P} = \frac{^{A}d}{dt}(\dot{\theta}cos\theta
          \underline{e}_{r} + \dot{\theta}sin\theta \underline{e}_{\theta})$ $=
          \frac{^{B}d}{dt}(\dot{\theta}cos\theta \underline{e}_{r} +
          \dot{\theta}sin\theta \underline{e}_{\theta})$ $+
          ^{A}\underline{\omega}^{B} \times (\dot{\theta}cos\theta
          \underline{e}_{r} + \dot{\theta}sin\theta \underline{e}_{\theta})$
>       - $^{A}\underline{a}_{P} = (\ddot{\theta}cos\theta -
          \dot{\theta}^{2}sin\theta) \underline{e}_{r} +
          (\ddot{\theta}sin\theta + \dot{\theta}^{2}cos\theta)
          \underline{e}_{\theta}$ $+ \dot{\theta} \underline{e}_{z} \times
          (\dot{\theta}cos\theta \underline{e}_{r} + \dot{\theta}sin\theta
          \underline{e}_{\theta})$
>       - $^{A}\underline{a}_{P} = (\ddot{\theta}cos\theta -
          \dot{\theta}^{2}sin\theta) \underline{e}_{r} +
          (\ddot{\theta}sin\theta + \dot{\theta}^{2}cos\theta)
          \underline{e}_{\theta}$ $+ \dot{\theta}^{2}cos\theta
          \underline{e}_{\theta} - \dot{\theta}^{2}sin\theta \underline{e}_{r}$
>       - $^{A}\underline{a}_{P} = (\ddot{\theta}cos\theta -
          2\dot{\theta}^{2}sin\theta) \underline{e}_{r} +
          (\ddot{\theta}sin\theta + 2\dot{\theta}^{2}cos\theta)
          \underline{e}_{\theta}$

> - Let us now find the vectors of the intrinsic coordinate system attached to
    point P
> - Start with the tangential vector $\underline{e}_{t}$
>       - $\| ^{A}\underline{V}_{P} \| = \sqrt{(\dot{\theta} cos\theta)^{2} +
          (\dot{\theta} sin\theta})^{2}}$ $= \sqrt{\dot{\theta}^{2}
          (cos^{2}\theta + sin^{2}\theta)} = \dot{\theta}$
>       - $\underline{e}_{t} = \frac{^{A}\underline{V}_{P}}{\|
          ^{A}\underline{V}_{P} \|}$ $= \frac{\dot{\theta}cos\theta
          \underline{e}_{r} + \dot{\theta}sin\theta
          \underline{e}_{\theta}}{\dot{\theta}} = cos\theta \underline{e}_{r} +
          sin\theta \underline{e}_{\theta}$
> - Now that the tangential vector has been found the principle normal to the
    trajectory can be found
>       - $\frac{^{A}d}{dt}\underline{e}_{t} = \frac{^{B}d}{dt} (cos\theta
          \underline{e}_{r} +$ $sin\theta \underline{e}_{\theta}) +
          ^{A}\underline{\omega}^{B} \times (cos\theta \underline{e}_{r} +
          sin\theta \underline{e}_{\theta})$
>       - $\frac{^{A}d}{dt}\underline{e}_{t} = -\dot{\theta}sin\theta
          \underline{e}_{r} + \dot{\theta}cos\theta$ $\underline{e}_{\theta} +
          \dot{\theta} \underline{e}_{z} \times (cos\theta \underline{e}_{r} +
          sin\theta \underline{e}_{\theta})$
>       - $\frac{^{A}d}{dt}\underline{e}_{t} = -\dot{\theta}sin\theta
          \underline{e}_{r} + \dot{\theta}cos\theta$ $\underline{e}_{\theta} +
          \dot{\theta} cos\theta \underline{e}_{\theta} -
          \dot{\theta} sin\theta \underline{e}_{r}$ $= -2 \dot{\theta}
          sin\theta \underline{e}_{r} + 2 \dot{\theta} cos\theta
          \underline{e}_{\theta}$
>       - $\| \frac{^{A}d}{dt}\underline{e}_{t} \| = \| -2 \dot{\theta}
          sin\theta \underline{e}_{r} + 2 \dot{\theta} cos\theta
          \underline{e}_{\theta} \|$ $= \sqrt{(2 \dot{\theta} sin\theta)^{2} +
          (2 \dot{\theta} cos\theta)}$
>       - $\| \frac{^{A}d}{dt}\underline{e}_{t} \| = \sqrt{4 \dot{\theta}^{2}
          (sin^{2}\theta + cos^{2}\theta)}$ $= 2 \dot{\theta}$
>       - $\underline{e}_{n} = \frac{\frac{^{A}d}{dt}\underline{e}_{t}}{\|
          \frac{^{A}d}{dt}\underline{e}_{t} \|}$ $= \frac{-2\dot{\theta}
          sin\theta \underline{e}_{r} + 2\dot{\theta} cos\theta
          \underline{e}_{\theta}}{2 \dot{\theta}}$ $= -sin\theta
          \underline{e}_{r} + cos\theta \underline{e}_{\theta}$
> - Finally the princible binormal to the trajectory can be determined
>       - $\underline{e}_{b} = \underline{e}_{t} \times \underline{e}_{n} =
          (cos\theta \underline{e}_{r} +$ $sin\theta \underline{e}_{\theta})
          \times (-sin\theta \underline{e}_{r} + cos\theta
          \underline{e}_{\theta})$
>       - $\underline{e}_{b} = (cos^{2}\theta + sin^{2}\theta)
          \underline{e}_{z}$
>       - $\underline{e}_{b} = \underline{e}_{z}$

> ### Rolling Motion {#e_rolling_motion}

> - This example also includes examples on motion between two points fixed in
    the same rigid body
> - The diagram for the problem is given as follows

<div align="center">
<table class="image">
<tr><td><img src="./img/e_rollandslip.png"
alt="Roll and Slip Example" title="Roll and Slip Example"
width="400" height="400"/> 
</td></tr>
</table>
</div>

> - It is desired to find the velocity and acceleration of point O and point P
    given that there is roll without slip between the disk and the wedge
> - To begin we will define two different reference frames, the disk (D) and
    the ground (G)
> - Coordinate system fixed in the ground reference frame  (G)
>       - Origin at point O at time = 0
>       - $\underline{E}_{z}$ = into the page
>       - $\underline{E}_{x}$ = along $\underline{OC}$
>       - $\underline{E}_{y}$ = $\underline{E}_{z} \times \underline{E}_{x}$

<div align="center">
<table class="image">
<tr><td><img src="./img/e_rollandslip_ground.png"
alt="Roll and Slip Example Ground Reference Frame" title="Roll and Slip Example
Ground Reference Frame" width="300" height="300"/> 
</td></tr>
</table>
</div>

> - Coordinate system fixed in the disk reference frame (D)
>       - Origin at point O
>       - $\underline{e}_{r}$ = along $\underline{OP}$
>       - $\underline{e}_{z}$ = $\underline{E}_{z}$
>       - $\underline{e}_{\theta}$ = $\underline{e}_{z} \times
          \underline{e}_{r}$

> - We will begin by stating the condition for rolling without slip
>       - $(^{A}\underline{V}^{G}_{C}) = (^{A}\underline{V}^{D}_{C})$
>       - In this case we will use the condition in the ground reference frame
          (A = G)
>       - Now we can note that point C in the ground reference frame is fixed
          and therefore its velocity is zero and as a consequence the point C
          in the disk reference frame also has zero velocity
>           - $(^{G}\underline{V}^{G}_{C}) = 0 \Right
              (^{G}\underline{V}^{D}_{C}) = 0$
> - Now we will make use of the velocity relations for two points fixed in the
    same rigid body to relate the velocity between points C and O
>       - $^{G}\underline{V}_{O} - ^{G}\underline{V}_{C} =
          (^{G}\underline{\omega}^{D}) \times (\underline{r}_{O} -
          \underline{r}_{C})$
>       - $^{G}\underline{V}_{O} = \dot{\theta} \underline{E}_{z} \times (-R
          \underline{E}_{x})$
>           - From $^{G}\underline{V}_{C} = \underline{r}_{O} = 0$
>       - $^{G}\underline{V}_{O} = -R \dot{\theta} \underline{E}_{y}$
> - We can use the same relation between two points fixed in a rigid body to
    now relate the velocities of point O and point P
>       - $^{G}\underline{V}_{P} - ^{G}\underline{V}_{O} =
          (^{G}\underline{\omega}^{D}) \times (\underline{r}_{P} -
          \underline{r}_{O})$
>       - $^{G}\underline{V}_{P} = (^{G}\underline{V}_{O}) +
          ^{G}\underline{\omega}^{D} \times \underline{r}_{P}$
>       - $^{G}\underline{V}_{P} = -R \dot{\theta} \underline{E}_{y} +
          \dot{\theta} \underline{e}_{z} \times R \underline{e}_{r}$
>       - $^{G}\underline{V}_{P} = - R \dot{\theta} \underline{E}_{y} + R
          \dot{\theta} \underline{e}_{\theta}$
> - With both of the desired velocities found we can now find the desired
    accelerations. We will be begin with the acceleration of point O
>       - $^{G}\underline{a}_{O} = \frac{^{G}d}{dt}(^{G}\underline{V}_{O}) =
          \frac{^{G}d}{dt}(-R \dot{\theta} \underline{E}_{y})$
>       - $^{G}\underline{a}_{O} = -R \ddot{\theta} \underline{E}_{y}$
> - In order to find the acceleration of point P we are going to use the
    relation between the accelerations of point P and point O
>       - $^{G}\underline{a}_{P} - ^{G}\underline{a}_{O} =
          (^{G}\underline{\alpha}^{D}) \times (\underline{r}_{P} -
          \underline{r}_{O}) +$ $^{G}\underline{\omega}^{D} \times \left[
          ^{G}\underline{\omega}^{D} \times (\underline{r}_{P} -
          \underline{r}_{O}) \right]$
>       - $^{G}\underline{a}_{P} + R \ddot{\theta} \underline{E}_{y} =
          \ddot{\theta}\underline{e}_{z} \times (R \underline{e}_{r}) +
          \dot{\theta}\underline{e}_{z}$ $\times \left[ \dot{\theta}
          \underline{e}_{z} \times (R \underline{e}_{r}) \right]$
>       - $^{G}\underline{a}_{P} = - R \ddot{\theta} \underline{E}_{y} + R
          \ddot{\theta} \underline{e}_{\theta} - R \dot{\theta}^{2}
          \underline{e}_{r}$
> - As a bonus the acceleration of point C on the disk will be found. It should
    be noted that the rolling condition is strictly for velocities and not the
    velocities ($(^{G}\underline{a}^{D}_{C}) \neq (^{G}\underline{a}^{G}_{C})$)
>       - $^{G}\underline{a}_{C} - ^{G}\underline{a}_{O} =
          (^{G}\underline{\alpha}^{D}) \times (\underline{r}_{P} -
          \underline{r}_{O}) +$ $^{G}\underline{\omega}^{D} \times \left[
          ^{G}\underline{\omega}^{D} \times (\underline{r}_{P} -
          \underline{r}_{O}) \right]$
>       - $^{G}\underline{a}_{C} + R \ddot{\theta} \underline{E}_{y} =
          \ddot{\theta}\underline{E}_{z} \times (R \underline{E}_{x}) +
          \dot{\theta}\underline{E}_{z}$ $\times \left[ \dot{\theta}
          \underline{E}_{z} \times (R \underline{E}_{x}) \right]$
>       - $^{G}\underline{a}_{C} = - R \dot{\theta}^{2}
          \underline{E}_{x}$

> ### Basic Equation of Motion {#e_basic_equation_of_motion}

> - The problem is to determine the equations of motion for mass $m$ located at
    point P which is attached by a rod to point O which is fixed in the ground
    and the ground reference frame can be considered intertial

<div align="center">
<table class="image">
<tr><td><img src="./img/e_basic_motion.png"
alt="Basic Equations of Motion Example" title="Basic Equations of Motion
Example" width="300" height="300"/> 
</td></tr>
</table>
</div>

> - Only one equation of motion is expected due to the mass being constrained
    to a trajectory that lies on a single line
> - We will begin by defining our reference frames. For this problem two frames
    will be used due to the presence of a rotation
>       - Ground reference frame (G)
>       - Plane perpendicular to the page containing $\underline{OP}$ (A)
> - Coordinate system fixed in the ground reference frame (G)
>       - Origin fixed at O
>       - $\underline{E}_{z}$ = out of the page
>       - $\underline{E}_{x}$ = along $\underline{OP}$ at $\theta$ = 0
>       - $\underline{E}_{y}$ = $\underline{E}_{z} \times \underline{E}_{x}$
> - Coordinate system fixed in reference frame A
>       - Origin fixed at point O
>       - $\underline{e}_{r}$ = along $\underline{OP}$
>       - $\underline{e}_{r}$ = $\underline{E}_{z}$
>       - $\underline{e}_{\theta}$ = $\underline{e}_{z} \times
          \underline{e}_{r}$
> - Now we will begin by finding the position velocity and acceleration of
    point P in the ground reference frame
>       - $\underline{r}_{P} = \el \underline{e}_{r}$
>       - $^{G}\underline{V}_{P} = \frac{^{A}d}{dt}(\el \underline{e}_{r}) +
          \dot{\theta} \underline{e}_{z} \times \el \underline{e}_{r}$ $=
          \dot{\theta} \el \underline{e}_{\theta}$
>       - $^{G}\underline{a}_{P} = \frac{^{A}d}{dt}(\dot{\theta} \el
          \underline{e}_{\theta}) + \dot{\theta} \underline{e}_{z} \times
          \dot{\theta} \el \underline{e}_{\theta}$ $= \ddot{\theta} \el
          \underline{e}_{\theta} - \dot{\theta}^{2} \el \underline{e}_{r}$
> - With the acceleration of point P in the ground reference frame found we can
    now move on to the kinetics portion of the problem
> - We will begin this portion with a free body diagram to determine what
    forces are present

<div align="center">
<table class="image">
<tr><td><img src="./img/e_basic_motion_FBD.png"
alt="Basic Equations of Motion Example Free Body Diagram" title="Basic
Equations of Motion Example Free Body Diagram" width="300" height="300"/> 
</td></tr>
</table>
</div>

> - The sum of forces is therefore as follows
>       - $\underline{F} = m\underline{g} + \underline{R} = mg\underline{E}_{x}
          + R\underline{e}_{r}$
> - With the sum of forces found we can now express all fo the terms in
    Newton's Second Law
>       - $\underline{F} = m ^{G}\underline{a}_{P}$
>       - $mg \underline{E}_{x} + R \underline{e}_{r} = m (\ddot{\theta} \el
          \underline{e}_{\theta} - \dot{\theta}^{2} \el \underline{e}_{r})$
> - In the above expression the only unknown value is $R$, therefore we can
    find the desired equation of motion by taking the dot product of each term
    by $\underline{e}_{\theta}$
>       - $mg (cos\theta \underline{e}_{r} - sin\theta \underline{e}_{\theta})
          \cdot \underline{e}_{\theta} + R \underline{e}_{r} \cdot$
          $\underline{e}_{\theta} = m(\ddot{\theta} \el \underline{e}_{\theta}
          - \dot{\theta}^{2} \el \underline{e}_{r}) \cdot
          \underline{e}_{\theta}$
>       - $-mg sin\theta = m \ddot{\theta} \el$
>       - $\ddot{\theta} = - \frac{g}{\el}sin\theta$ 

> ### Angular Momentum {#e_angular_momentum}

> - The problem in this example is to find the equations of motion for the
    point P in the folling figure where point Q slides around the circle at
    given speed $\alpha (t)$

<div align="center">
<table class="image">
<tr><td><img src="./img/e_angular_momentum.png"
alt="Angular Momentum Example" title="Angular Momentum Example" width="300"
height="300"/> 
</td></tr>
</table>
</div>

> - For this problem two different reference frames will be use
>       - Ground (G), treated as inertial
>       - Frame attached to rod along $\underline{QP}$ (A)
> - Coordinate system fixed in Ground reference frame (G)
>       - Origin at point O
>       - $\underline{E}_{x}, \underline{E}_{y}, \underline{E}_{z}$ given in
          the figure
> - Coordinate system fixed in reference frame (A)
>       - Origin at point Q
>       - $\underline{e}_{r}$ = along $\underline{QP}$
>       - $\underline{e}_{z}$ = $\underline{E}_{z}$
>       - $\underline{e}_{\theta}$ = $\underline{e}_{z} \times
          \underline{e}_{r}$
> - The first thing that will need to be done will be to solve for the
    kinematics of point P in the inertial reference frame (G)
>       - $\underline{r}_{P} = \underline{OQ} + \underline{QP}$ $= \el_{1}
          cos\alpha \underline{E}_{x} + \el_{1} sin\alpha \underline{E}_{y} +
          \el_{2} \underline{e}_{r}$
>       - $^{G}\underline{V}_{P} = \frac{^{G}d}{dt}(\el_{1} cos\alpha
          \underline{E}_{x} + \el_{1} sin\alpha$ $\underline{E}_{y}) +
          \frac{^{A}d}{dt}(\el_{2} \underline{e}_{r}) +
          \dot{\theta} \underline{e}_{z} \times \el_{2}
          \underline{e}_{r}$
>       - $^{G}\underline{V}_{P} = - \el_{1} \dot{\alpha} sin\alpha
          \underline{E}_{x} + \el_{1} \dot{\alpha} cos\alpha \underline{E}_{y}
          + \el_{2} \dot{\theta} \underline{e}_{\theta}$
>       - $^{G}\underline{a}_{P} = \frac{^{G}d}{dt} (- \el_{1} \dot{\alpha}
          sin\alpha \underline{E}_{x} + \el_{1} \dot{\alpha} cos\alpha
          \underline{E}_{y}) + \frac{^{A}d}{dt} (\el_{2} \dot{\theta}$
          $\underline{e}_{\theta}) + \dot{\theta} \underline{e}_{z} \times
          (\el_{2} \dot{\theta} \underline{e}_{\theta})$
>       - $^{G}\underline{a}_{P} = (-\el_{1} \ddot{\alpha} sin\alpha  - \el_{1}
          \dot{\alpha}^{2} cos\alpha) \underline{E}_{x}$ $+ (\el_{1}
          \ddot{\alpha} cos\alpha - \el_{1} \dot{\alpha}^{2} sin\alpha)
          \underline{E}_{y}$ $+ \el_{2} \ddot{\theta} \underline{e}_{\theta} -
          \el_{2} \dot{\theta}^{2} \underline{e}_{r}$

> - Next a free body diagram will be used so that the equations of motion can
    be found

<div align="center">
<table class="image">
<tr><td><img src="./img/e_angular_momentum_FBD.png"
alt="Angular Momentum Example Free Body Diagram" title="Angular Momentum
Example Free Body Diagram" width="300" height="300"/> 
</td></tr>
</table>
</div>

> - The equations of motion will be found using two different methods. The
    first will use Newton's second law for reference when the angular momentum
    approach is used.
> - Using Newton's second law will lead to the following result
>       - $\underline{F} = m ^{G}\underline{a}$
>       - $-mg \underline{E}_{y} + R \underline{e}_{r} = m$ $[ (-\el_{1}
>         \ddot{\alpha} sin\alpha  - \el_{1} \dot{\alpha}^{2} cos\alpha)
>         \underline{E}_{x}$ $+ (\el_{1} \ddot{\alpha} cos\alpha - \el_{1}
>         \dot{\alpha}^{2} sin\alpha) \underline{E}_{y}$ $+ \el_{2}
>         \ddot{\theta} \underline{e}_{\theta} - \el_{2} \dot{\theta}^{2}
>         \underline{e}_{r}]$


> ### Friction Force Models {#e_friction_force_models}

<div align="center">
<table class="image">
<tr><td><img src="./img/e_friction_models.png"
alt="Friction Force Models Example" title="Friction Force Models Example"
width="300" height="300"/> 
</td></tr>
</table>
</div>

> ### Linear Spring Force Models {#e_linear_spring_force_models}

<div align="center">
<table class="image">
<tr><td><img src="./img/e_spring_model.png"
alt="Linear Spring Model Example" title="Linear Spring Model Example"
width="300" height="300"/> 
</td></tr>
</table>
</div>
