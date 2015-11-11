# Robot Geometry
**Taught by: Dr. Carl Crane**  
**Taken: FS 2015**  
**Text: Kinematic Analysis of Robot Manipulators**  
*by: C. Crane and J. Duffy*

## Table of Contents

- [Coordinate Systems](#coord_sys)
- [Homogeneous Coordinates](#homogeneous_coordinates)
- [Coordinate Transformations](#coord_trans)
- [Links](#links)
- [Joints](#joints)
- [Kinematic Chains](#kinematic_chains)
- [Forward Analysis](#forward_analysis)
- [Reverse Analysis](#reverse_analysis)
- [Mobility](#mobility)
- [Planar Representation](#planar_representation)
- [Equivalent Spherical Mechanisms](#equivalent_spherical_mechanisms)
- [Group One Solution Process](#group_one_sol)
- [Group Two Solution Process](#group_two_sol)

## Coordinate Systems {#coord_sys}

- A single coordinate system (A) defined by $\underline{x}_{A},
  \underline{y}_{A}, \underline{z}_{A}$ and $A_{0}$
- $A_{0}$ is the origin of the A coordinate system
- $\underline{x}_{A}, \underline{y}_{A}, \underline{z}_{A}$ are all unit
  vectors and are dimensionless because they represent direction not length
- In $^{B}\underline{x}_{A}$ the B represents what coordinate system the values
  are being given for and the A represents that the vector is the unit vector
  in the x direction in the A coordinate system
- $^{A}\underline{V}_{A_{0} \rightarrow B_{0}}$ = Vector in coordinate system A
  pointing from the point $A_{0}$ to the point $B_{0}$
- $^{A}\underline{P}_{B_{0}}$ = Point $B_{0}$ as seen from coordinate system A
    - $^{A}\underline{V}_{A_{0} \rightarrow B_{0}}$ =
      $^{A}\underline{P}_{B_{0}}$

<div align="center">
<table class="image">
<caption align="bottom">Coordinate System A and Nomenclature</caption>
<tr><td><img src="./img/coordinate_system.png"
alt="Coordinate System A and Nomenclature" title="Coordinate System A and
Nomenclature"/>
</td></tr>
</table>
</div>

## Homogeneous Coordinates {#homogeneous_coordinates}

- Four coordinates to define a vector (X, Y, Z, w)
    - X = $\frac{x}{w}$
    - Y = $\frac{y}{w}$
    - Z = $\frac{z}{w}$
- Advantage of using homogeneous coordinates is that as w goes to zero the
  vectors point to infinity therefore there are unique vectors that point to
  infinity

## Coordinate Transformation {#coord_trans}

- Used to determine the position of a point from one coordinate system to
  another
    - Ex. point 1 may be defined in coordinate system B and it is desired to
      know the location of point 1 in coordinate system A
- To completely define the location and orientation from one coordinate system
  to another 6 values are needed (6 degrees of freedom)
    - Can use the vector pointing from the origin of one system to another to
      provide the translation information $^{A}\underline{V}_{A_{0} \rightarrow
      B_{0}}$ (Provides 3 of the 6 values)
    - Can use Euler angles to provide orientation information where each angle
      accounts for a rotation around one of the primary axis (Provides the
      remaining 3 of the 6 values. This method is not going to be utilized in
      this class)
    - Orientation information can also be provided by the following three unit
      vectors: $^{A}\underline{x}_{B}, ^{A}\underline{y}_{B},
      ^{A}\underline{z}_{B}$
        - Each vector provides three values for a total of nine values,
          however, they are constrained by having their magnitudes equal to one
          due to being unit vectors and all three are perpendicular to each
          other so their dot products equal zero
    - The three unit vectors along with the vector pointing from the origin of
      one system to the origin of the other will be used in the class to
      completely define the position and orientation of one coordinate system to
      another ($^{A}\underline{V}_{A_{0} \rightarrow B_{0}}$,
      $^{A}\underline{x}_{B}, ^{A}\underline{y}_{B}, ^{A}\underline{z}_{B}$)

> ### Rotation Matrix and Example

> - Consider two coordinate systems A and B and point 1 where
    $^{A}\underline{P}_{B_{0}}, ^{A}\underline{x}_{B}, ^{A}\underline{y}_{B},
    ^{A}\underline{z}_{B} and ^{B}\underline{P}_{1}$ are given values and you
    need to find the location of point 1 defined in the A coordinate system
    ($^{A}\underline{P}_{1}$)
> - Breaking $^{B}\underline{P}_{1}$ into its component gives
    $^{B}\underline{P}_{1} = \left[ b_{1} \\ b_{2} \\ b_{3} \right]$
> - The vector from the origin of the B system to the point 1 can be defined in
    the A coordinate system as follows: $^{A}\underline{V}_{B_{0} \rightarrow
    1} = b_{1}^{A}\underline{x}_{B} + b_{2}^{A}\underline{y}_{B} +
    b_{3}^{A}\underline{z}_{B}$ &nbsp;&nbsp; or &nbsp;&nbsp;
    $^{A}\underline{V}_{B_{0} \rightarrow 1} = \left[ ^{A}\underline{x}_{B},
    ^{A}\underline{y}_{B}, ^{A}\underline{z}_{B} \right] \left[ b_{1} \\ b_{2}
    \\ b_{3} \right]$
> - Vector $^{A}\underline{P}_{1}$ can then be defined as
    $^{A}\underline{P}_{1} = ^{A}\underline{P}_{B_{0}} +
    ^{A}\underline{V}_{B_{0} \rightarrow 1}$ = $^{A}\underline{P}_{B_{0}} +
    \left[ ^{A}\underline{x}_{B}, ^{A}\underline{y}_{B}, ^{A}\underline{z}_{B}
    \right] \left[ b_{1} \\ b_{2} \\ b_{3} \right]$
>       - If we then define $^{A}_{B}R = \left[ ^{A}\underline{x}_{B},
          ^{A}\underline{y}_{B}, ^{A}\underline{z}_{B} \right]$ where
          $^{A}_{B}R$ is the 3x3 rotation matrix from system B to system A we
          can further simplify the previous result to $^{A}\underline{P}_{1} =  
          ^{A}\underline{P}_{B_{0}} + ^{A}_{B}R^{B}P_{1}$
> - To reverse the direction of a rotation matrix simply take the transpose of
    the original matrix ($^{A}_{B}R = (^{B}_{A}R)^{T}$)
>       - This is saying that $^{A}_{B}R = \left[ ^{A}\underline{x}_{B},
          ^{A}\underline{y}_{B}, ^{A}\underline{z}_{B} \right]$ $= \left[
          (^{B}\underline{x}_{A})^{T} \\ (^{B}\underline{y}_{A})^{T} \\
          (^{B}\underline{z}_{A})^{T} \right]$

> ### Transformation Matrix

> - Coordinate system transformations with rotation matrices can be further
    simpified by using homogenous coordinates and defining a transformation
    matrix as 

<div align="center">
<table class="image">
<tr><td><img src="./img/transformation_matrix_definition.png"
alt="Transformation Matrix Definition" title="Transformation Matrix
Definition" width="200" height="200"/>
</td></tr>
</table>
</div>

> - The coordinate transformation can then be re-written from
    $^{A}\underline{P}_{1} = ^{A}\underline{P}_{B_{0}} + ^{A}_{B}R^{B}P_{1}$ to
    $^{A}\underline{P}_{1} = (^{A}_{B}T)^{B}\underline{P}_{1}$
> - It is desired to reverse the direction of a transformation matrix (from $B
    \rightarrow A$ to $A \rightarrow B$)
>       - Start with the given transformation matrix we have knowledge of
          $^{A}_{B}R$ and $^{A}P_{B{0}}$
>       - For the new matrix we will need $^{B}_{A}R$ and $^{B}P_{A{0}}$
>       - It is known from the properties of rotation matrices as shown above
          that the rotation matrix in the reverse transforming direction is the
          transpose of the original rotation matrix
>           - $^{B}_{A}R$ = $(^{A}_{B}R)^{T}$
>       - The general equation for transforming a point (1) from coordinate
          system A to B is $^{B}P_{1} = ^{B}P_{A{0}} + ^{B}_{A}R^{A}P_{1}$
>       - Taking the above equation and using it to find coordinate system B's
          origin as seen from the A system gives the following equation
          $^{B}P_{B_{0}} = ^{B}P_{A_{0}} + ^{B}_{A}R^{A}P_{B_{0}}$ where
          $^{B}P_{B_{0}} = \underline{0}$ 
>           - Now solving for the desired $^{B}P_{A_{0}}$ gives $^{B}P_{A_{0}}
              = -^{B}_{A}R^{A}P_{B_{0}}$ &nbsp;&nbsp; or &nbsp;&nbsp;
              $^{B}P_{A_{0}} = -(^{A}_{B}R)^{T}^{A}P_{B_{0}}$
>       - Now the unknowns are in terms of the known values and the new
          transformation matrix can be written in the form shown above

<div align="center">
<table class="image">
<tr><td><img src="./img/reverse_transformation_matrix_definition.png"
alt="Reverse Transformation Matrix Definition" title="Reverse Transformation
Matrix Definition" width="300" height="200"/> 
</td></tr>
</table>
</div>

> ### Rotation Around a General Vector Passing Through the Origin 

> - The rotation matrix for a rotation, $\theta$, around a general vector,
    $\underline{m}$, passing through the origin is: 

<div align="center">
<table class="image">
<caption align="bottom">Figure taken from the book</caption>
<tr><td><img src="./img/rotation_general_transform_matrix.jpg"
alt="General Rotation Transformation Matrix" title="General Rotation
Transformation Matrix" width="400" height="100"/> 
</td></tr>
</table>
</div>

> - Where $v = 1 - cos(\theta)$, $s = sin(\theta)$ and $c = cos(\theta)$

>> #### Formula Derivation

>> - It is desired to find the rotation matrix from coordinate system A to
     coordinate system B after a rotation $\theta$ about a generic vector
     $\underline{m}$
>> - To begin consider a coordinate system C whose z-axis is along the vector
     $\underline{m}$ (the location of the x and y vectors will be arbitrary)
>> - The rotation matrix from C to A can then be defined as $^{A}_{C}R = \left[
     \begin{array} a_{x} & b_{x} & m_{x} \\ a_{y} & b_{y} & m_{y} \\ a_{z} &
     b_{z} & m_{z} \end{array} \right]$
>> - Now consider coordinate system D which is obtained by rotating coordinate
     system C about its z-axis by $\theta$ degrees
>> - The rotation matrix from D to C would then be defined as $^{C}_{D}R =
     \left[ \begin{array} cos(\theta) & -sin(\theta) & 0 \\ sin(\theta) &
     cos(\theta) & 0 \\ 0 & 0 & 1 \end{array} \right]$
>> - Taking note that coordinate system B will have the same relation to
     coordinate system D as coordinate system C has to coordinate system A, the
     relation $^{A}_{C}R = (^{B}_{D}R)$ exists
>> - The desired rotation matrix can now be found by a series of matrix
     multiplications: $^{A}_{B}R = (^{A}_{C}R) * (^{C}_{D}R) * (^{D}_{B}R)$

<div align="center">
<table class="image">
<tr><td><img src="./img/rotate_gen_matrix_intermediate_step.png"
alt="General Rotation Transformation Matrix Unsimplified" title="General
Rotation Transformation Matrix Unsimplified" width="900" height="100"/> 
</td></tr>
</table>
</div>

>> - Unfortunately we do not have values for $a_{x}, a_{y}, a_{z}$ or $b_{x},
     b_{y}$ and $b_{z}$ because we chose the x and y axes for coordinate system
     C arbitrarily and so we will need to find a way to cancel them out of the
     resultant matrix
>> - In order to simplify the terms in the rotation matrix $^{A}_{B}R$ we will
     use the geometric meanings of the rotation matrix with matrix $^{A}_{C}R$
>> - First each row in a rotation matrix represents a unit vector and so the
     dot product of one of the rows with itself equals one (using matrix
     $^{A}_{C}R$)
>>      - $a_{x}^{2} + b_{x}^{2} + m_{x}^{2} = 1$
>>      - $a_{x}^{2} + b_{x}^{2} = 1 - m_{x}^{2}$
>>      - This rule should simplify all of the terms along the diagonal of
          rotation matrix $^{A}_{B}R$ to the form $c(1-m_{i}^{2}) + m_{i}^{2}$
          &nbsp;&nbsp; or &nbsp;&nbsp; $c + m_{i}^{2}(1-c)$
>> - The second geometric meaning of the rotation matrix that is going to be
     utilized is that all of the rows in the matrix represent vectors that are
     orthogonal to one another and therefore their dot product will equal zero
>>      - $a_{X}a_{y} + b_{x}b_{y} + m_{x}m_{y} = 0$
>>      - $a_{X}a_{y} + b_{x}b_{y} = -m_{x}m_{y}$
>> - The last geometric meaning of the rotation matrix that we are going to use
     is that the columns of the matrix represent vectors chosen using the right
     hand rule and therefore the cross product of the first two columns equals
     the third column
>>      - $(a_{y}b_{z}-a_{z}b_{y})\hat{\imath} +
          (a_{x}b_{z}-a_{z}b_{x})\hat{\jmath} + (a_{x}b_{y}-a_{y}b_{x})\hat{k}$
          $= m_{x}\hat{\imath} + m_{y}\hat{\jmath} + m_{z}\hat{k}$
>> - Using the second two rules the formula for the rest of rotation matrix
     $^{A}_{B}R$ can be simplified to the general form shown at the beginning of
     this section

>> #### Common Rotations

>> - Rotation $\alpha$ around the x-axis: $^{A}_{B}R = \left[ \begin{array} 1
     & 0 & 0 \\ 0 & cos(\alpha) & -sin(\alpha) \\ 0 & sin(\alpha) & cos(\alpha)
     \end{array} \right]$
>> - Rotation $\beta$ around the y-axis: $^{A}_{B}R = \left[ \begin{array}
     cos(\beta) & 0 & sin(\beta) \\ 0 & 1 & 0 \\ -sin(\beta) & 0 & cos(\beta)
     \end{array} \right]$
>> - Rotation $\gamma$ around the z-axis: $^{A}_{B}R = \left[ \begin{array}
     cos(\gamma) & -sin(\gamma) & 0 \\ sin(\gamma) & cos(\gamma) & 0 \\ 0 & 0 &
     1 \end{array} \right]$

>> #### Find Vector and Rotation Angle from the Rotation Matrix

>> - For the rotation matrix about a general vector passing through the origin,
     using the notation $^{A}_{B}R = \left[ \begin{array} r_{11} & r_{12} &
     r_{13} \\ r_{21} & r_{22} & r_{23} \\ r_{31} & r_{32} & r_{33} \end{array}
     \right]$
>> - Adding all of the elements in the diagonal gives $r_{11} + r_{22} + r_{33}
     = m_{x}^{2}v + c + m_{y}^{2}v + c + m_{z}^{2}v + c$ where vector $m$ is a
     unit vector ($m_{x}^{2} + m_{y}^{2} + m_{z}^{2} = 1$)
>>      - $r_{11} + r_{22} + r_{33} = (m_{x}^{2} + m_{y}^{2} + m_{z}^{2})v + 3c$
>>      - $r_{11} + r_{22} + r_{33} = v - 3c = (1 - cos(\theta)) + 3cos(\theta)$
>>      - $r_{11} + r_{22} + r_{33} = 1 + 2 cos(\theta)$
>> - To find the values of the vector m use the equation of the form $r_{ji} -
     r_{ij} = m_{i}m_{j}v + m_{k}s - (m_{j}m_{i}v - m_{k}s)$ for $i \neq j \neq
     k$ and $i < j$
>>      - This simplifies to $r_{ji} - r_{ij} = 2m_{k}sin(\theta)$
>>      - Example $r_{21} - r_{12} = 2m_{z}sin(\theta)$
>>      - Exception is $r_{13} - r_{31} = 2m_{y}sin\theta$


## Links {#links}

- Links are rigid bodies that maintain orientation between two axes
- The two axes ($\underline{S}_{i}$, $\underline{S}_{j}$) contain a unique
  perpendicular between them ($\underline{a}_{ij}$) where $\underline{a}_{ij}$
  is defined as the link length
    - If $\underline{S}_{i}$ and $\underline{S}_{j}$ intersect, then the link
      length is zero
    - The length $\underline{a}_{ij}$ is positive if chosen in such that it
      points from $\underline{S}_{i}$ to $\underline{S}_{j}$
- The angle from $\underline{S}_{i}$ to $\underline{S}_{j}$ using the right
  hand rule with one's thumb on $\underline{a}_{ij}$ is defined as
  $\alpha_{ij}$, where $\alpha_{ij}$ is called the twist angle
- It is common to replace all of the links in a system with their equivalent
  kinematic link
    - Kinematic link is represented by drawing just the
      $\underline{S}_{i}$/$\underline{S}_{j}$ axes and the link length

<div align="center">
<table class="image">
<tr><td><img src="./img/phy_to_kinematic_link.png"
alt="Physical to Kinematic Link" title="Physical to Kinematic Link" width="300"
height="200"/> 
</td></tr>
</table>
</div>

- Two special link cases are spherical links and planar links
    - In spherical links $\underline{S}_{i}$ intersects $\underline{S}_{j}$ and
      $a_{ij} = 0$
    - In planar links $\underline{S}_{i}$ is parallel with $\underline{S}_{j}$
      and $\alpha_{ij} = 0$

> ### Standard Link Coordinate Systems

> - The standard link coordinate system for link ij has its origin at the
    intersection of $\underline{S}_{i}$ and $\underline{a}_{ij}$, it's x-axis
    along the vector $\underline{a}_{ij}$ and it's z-axis along the vector
    $\underline{S}_{i}$
>       - The y-axis is determined using the right hand rule
> - Figure taken from lecture powerpoint

<div align="center">
<table class="image">
<tr><td><img src="./img/standard_link_coordinate_system.png"
alt="Standard Link Coordinate System" title="Standard Link Coordinate System"
width="300" height="200"/> 
</td></tr>
</table>
</div>

## Joints {#joints}

- There are two main values that define a joint: the joint offset distance
  ($\underline{S}_{j}$) and the joint angle ($\theta_{j}$)
- The joint offset distance is the unique perpendicular between
  $\underline{a}_{ij}$ and $\underline{a}_{jk}$
    - The joint offset distance has no sense of direction and is therefore
      simply a scalar value not a vector
- The joint angle is defined by the right hand rule with thumb on
  $\underline{S}_{j}$ and sweeping from $\underline{a}_{ij}$ to
  $\underline{a}_{jk}$
- All joint pictures were taken from the lecture powerpoint

> ### Revolute Joint, R

> - Revolute joints only allow rotation between the links (1 degree of freedom)
> - Joint offset distance is fixed and joint angle is variable

<div align="center">
<table class="image">
<tr><td><img src="./img/revolute_joint.png"
alt="Revolute Joint" title="Revolute Joint" width="300"
height="200"/> 
</td></tr>
</table>
</div>

> ### Prismatic Joint, P

> - Prismatic joints only allow translation between the links (1 degree of
    freedom)
> - Joint offset distance is variable and joint angle is fixed

<div align="center">
<table class="image">
<tr><td><img src="./img/prismatic_joint.png"
alt="Prismatic Joint" title="Prismatic Joint" width="300"
height="200"/> 
</td></tr>
</table>
</div>

> ### Cylindrical Joint, C

> - Cylindrical joints allow translation and rotation between joints (2 degrees
    of freedom)
> - Joint offset distance is variable and joint angle is variable

<div align="center">
<table class="image">
<tr><td><img src="./img/cylindric_joint.png"
alt="Cylindric Joint" title="Cylindric Joint" width="300"
height="200"/> 
</td></tr>
</table>
</div>

> ### Screw Joint, H

> - Screw joints allow translation and rotation (1 degrees of freedom bc the
    two variables are not independent)
> - Both the joint offset distance and joint angle are variable but they are
    not independent of one another

<div align="center">
<table class="image">
<tr><td><img src="./img/screw_joint.png"
alt="Screw Joint" title="Screw Joint" width="300"
height="200"/> 
</td></tr>
</table>
</div>

> ### Plane Joint, E

> - Plane joints allow 2 degrees of translation and one degree of rotation (3
    degrees of freedom)
> - To make plane joints easier to analyze they are simplified to two prismatic
    joints and a revolute joint

<div align="center">
<table class="image">
<tr><td><img src="./img/plane_joint.png"
alt="Plane Joint" title="Plane Joint" width="600"
height="450"/> 
</td></tr>
</table>
</div>

> ### Hook Joint, T

> - Hook joints allow rotation around two axes (2 degrees of freedom)
> - A simplified view of hook joints is that it's a combination of two revolute
    joints
> - For a hook joint $a_{jk} =0$ and $\alpha_{ik} = 90 \deg$

<div align="center">
<table class="image">
<tr><td><img src="./img/hook_joint.png"
alt="Hook Joint" title="Hook Joint" width="400"
height="300"/> 
</td></tr>
</table>
</div>

> ### Spherical Joint, S

> - A spherical joint allows rotation about all three axes (3 degrees of
    freedom)
> - For analysis purposes spherical joints are replaced by three revolute joints
> - With spherical joints the $S_{i}$, $S_{j}$ and $S_{k}$ intersect resulting
    in $a_{ij} = a_{jk} = S_{j} = 0$

<div align="center">
<table class="image">
<tr><td><img src="./img/spherical_joint.png"
alt="Spherical Joint" title="Spherical Joint" width="600"
height="350"/> 
</td></tr>
</table>
</div>

## Kinematic Chains {#kinematic_chains}

- When labeling a kinematic chain of links start by defining the $S_{i}$
  vectors and then the $a_{ij}$ vectors
- Next you can define all of the twist angles $\alpha_{ij}$ and joint angles
  $\theta_{i}$

> ### Standard Fixed Coordinate System

> - The standard fixed coordinate system is used to define the location and
    orientation of the first link relative to the ground which in turn defines
    the rest of the links
> - The origin of the standard fixed coordinate system is at the intersection
    of $S_{1}$ and $a_{12}$
> - The z-axis of the standard fixed coordinate system ($z_{F}$) points along
    $S_{1}$ and the directions of the x and y axes are chosen at will as long
    as the system remains right handed ortho-normal
> - The angle from $x_{F}$ to $a_{12}$ is labeled $\phi_{1}$ instead of $\theta$

<div align="center">
<table class="image">
<tr><td><img src="./img/kinematic_chain.png"
alt="Kinematic Chain" title="Kinematic Chain" width="600"
height="350"/> 
</td></tr>
</table>
</div>

## Forward Analysis {#forward_analysis}

- The objective of forward analysis is to find the position and orientation of
  the end effector in the fixed standard coordinate system of a kinematic chain
  given the link lengths, twist angles, joint offset distances and joint angles

<div align="center">
<table class="image">
<tr><td><img src="./img/link2link_trans_matrix.png"
alt="General Link to Link Transformation Matrix" title="General Link to Link
Transformation Matrix" width="300" height="150"/> 
</td></tr>
</table>
</div>

- Where $c_{j}$ and $s_{j}$ are $cos(\theta_{j})$ and $sin(\theta_{j})$,
  $c_{ij}$ and $s_{ij}$ are $cos(\alpha_{ij})$ and $sin(\alpha_{ij})$ and
  $S_{j}$ is the joint offset distance
- The location and orientation of the last link as viewed from the fixed
  reference frame can then be found by the series of matrix multiplications:
  $^{F}_{6}T = ^{F}_{1}T ^{1}_{2}T ^{2}_{3}T ^{3}_{4}T ^{4}_{5}T ^{5}_{6}T$
    - $^{F}P_{tool} = ^{F}_{6}T ^{6}P_{tool}$

> ### General Link to Link Transformation Matrix Derivation

## Reverse Analysis {#reverse_analysis}

- The objective of reverse analysis is to find all of the variable joint
  parameters that will position the robot such that its tool has the desired
  position and orientation as viewed from the fixed reference frame

> __Iterative Technique__

> - For a standard 6 link robot with all revolute joints, the transformation
    matrix relating the fixed coordinate system to the last link can be found
    by the series of matrix multiplications: $^{F}_{6}T = ^{F}_{1}T ^{1}_{2}T
    ^{2}_{3}T ^{3}_{4}T ^{4}_{5}T ^{5}_{6}T$
>       - Each transformation matrix corresponds to a specific variable joint
          angle ($\phi_{1} \rightarrow \theta_{6}$)
> - The iterative technique consists of making a guess as to the variable joint
    angles then using forward analysis to find a $^{F}_{6}T$ matrix then that
    matrix is compared with the desired $^{F}_{6}T$ matrix
>       - Based on the comparison the guesses for the variable joint angles are
          adjusted and the process is repeated
> - This process can be optimized using an objective function $F(\phi_{1}
    \rightarrow \theta_{6})$
> - The iterative technique is not a very direct process for doing analysis and
    so this will not be the prefered technique for the class

> __Hypothetical Link Technique__

> - This technique consists of adding a hypothetical link to the kinematic
    chain that connects the last link (link 6) to the ground to make the chain
    a closed loop resulting in only 1 degree of freedom for the chain
> - For the new hypothetical link 7 we will need values for $a_{67}$ and
    $\alpha_{67}$ which we will be free to choose
>       - Convenient to choose $a_{67} = 0$ and $\alpha_{67} = 90^{\circ}$
          because then $^{F}S_{7} = -^{F}y_{6}$
> - This set up leaves three angles and three distances that need to be solved:
    $\alpha_{71}$, $\theta_{7}$, $\gamma_{1}$, $S_{7}$, $a_{71}$ and $S_{1}$
> - All vectors mentioned in the following process are unit vectors
> - The first step in solving for the unknowns is using the definition of dot
    product with vectors $^{F}\underline{S}_{7}$ and$^{F}\underline{S}_{1}$ to
    find $\alpha_{71}$
>       - $^{F}\underline{S}_{7} \cdot ^{F}\underline{S}_{1} = \|
          \underline{S}_{7} \| \| \underline{S}_{1} \| cos(\alpha_{71}) =
          cos(\alpha_{71})$
>            - Keeping in mind that $\underline{S}_{7}$ and $\underline{S}_{1}$
               are unit vectors therefore thier magnitudes are one
>       - If $\alpha_{71}$ is close to 0 or 180 degrees then a different set of
          steps from the ones that are about to be presented will need to be
          followed
> - The next step is to determine the $^{F}\underline{a}_{71}$ vector and this
    can be accomplished by taking the cross product of the $\underline{S}_{7}$
    and $\underline{S}_{1}$ vectors and then dividing by the magnitude of that
    cross product to ensure that the vector is unit length
>       - $^{F}\underline{a}_{71} = \frac{^{F}\underline{S}_{7} \times
          ^{F}\underline{S}_{1}}{\| ^{F}\underline{S}_{7} \times
          ^{F}\underline{S}_{1} \|}$
> - Now using the properties of dot products and cross products $\theta_{7}$
    and $\gamma_{1}$ can be determined where $\phi_{1} = \theta_{1} -
    \gamma_{1}$
>       - Both dot product and cross product definitions are needed because
          individually $sin^{-1}$ and $cos^{-1}$ give two different answers but
          when compared together only one answer emerges
>       - $cos(\theta_{7}) = (^{F}\underline{a}_{67}) \cdot
          ^{F}\underline{a}_{71}$
>       - $sin(\theta_{7}) = (^{F}\underline{a}_{67} \times
          ^{F}\underline{a}_{71}) \cdot ^{F}\underline{S}_{7}$
>       - $cos(\gamma_{1}) = (^{F}\underline{a}_{71}) \cdot
          ^{F}\underline{x}_{F}$
>       - $sin(\gamma_{1}) = (^{F}\underline{a}_{71} \times
          ^{F}\underline{x}_{F}) \cdot ^{F}\underline{S}_{1}$
> - Now that the three unknown angles and the direction of vector
    $^{F}\underline{a}_{71}$ has been obtained the three unknown distances need
    to be found: $S_{7}$, $a_{71}$ and $S_{1}$
> - To find these distances we will use the vector loop equation for the
    following closed loop:
>       - $^{F}\underline{P}_{6orig} + S_{7}(^{F}\underline{S}_{7}) +
          a_{71}(^{F}\underline{a}_{71}) + S_{1}(^{F}\underline{S}_{1}) =
          \underline{0}$
>       - Technically this is a series of 3 equations with 3 unknowns and
          therefore can be solved as is, however, this class includes a
          derivation of an equation for each unknown
> - To begin the derivation for an expression for $S_{7}$ we take the cross
    product of each term in the preceding equation with vector
    $\underline{S}_{1}$
>       - $(^{F}\underline{P}_{6orig} \times ^{F}\underline{S}_{1}) + S_{7}
          (^{F}\underline{S}_{7} \times ^{F}\underline{S}_{1})$ $+ a_{71}
          (^{F}\underline{a}_{71} \times ^{F}\underline{S}_{1}) + S_{1}
          (^{F}\underline{S}_{1} \times ^{F}\underline{S}_{1}) = \underline{0}$
>       - Note that the vector $^{F}\underline{S}_{1}$ crossed with itself is
          zero and so the last term goes away
>       - Also note that $^{F}\underline{S}_{7} \times ^{F}\underline{S}_{1}$
          is equivalent to $sin(\alpha_{71})^{F}\underline{a}_{71}$ by
          definition of how we set up the vectors
> - Now take the dot product of each remaining term of the expression with the
    vector $^{F}\underline{a}_{71}$
>       - $(^{F}\underline{P}_{6orig} \times ^{F}\underline{S}_{1}) \cdot
          ^{F}\underline{a}_{71} +
          S_{7}sin(\alpha_{71})(^{F}\underline{a}_{71}$ $\cdot
          ^{F}\underline{a}_{71}) + a_{71}(^{F}\underline{a}_{71} \times
          ^{F}\underline{S}_{1}) \cdot ^{F}\underline{a}_{71} = \underline{0}$
>       - First take note that when the dot product of the vector
          $^{F}\underline{a}_{71}$ is taken with itself it equals one and so
          all vectors in that term drop out
>       - Next take note that the cross product between
          $^{F}\underline{a}_{71}$ and $^{F}\underline{S}_{1}$ produces a
          result vector perpendicular to those two vectors and so when the dot
          product of that result vector and $^{F}\underline{a}_{71}$ is taken
          the result is zero and so the last term drops out of the above
          expression
> - The final expression is then only in terms of known values and can be
    rearranged to solve for $S_{7}$
>       - $S_{7} = \frac{(^{F}\underline{S}_{1} \times
          ^{F}\underline{P}_{6orig}) \cdot
          ^{F}\underline{a}_{71}}{sin\alpha_{71}}$

> - The same process is followed to find the other two unknown lengths and the
    resulting expression are as follows
>       - $a_{71} = \frac{(^{F}\underline{P}_{6orig} \times
          ^{F}\underline{S}_{1}) \cdot ^{F}\underline{S}_{7}}{sin\alpha_{71}}$
>       - $S_{1} = \frac{(^{F}\underline{P}_{6orig} \times
          ^{F}\underline{S}_{7}) \cdot ^{F}\underline{a}_{71}}{sin\alpha_{71}}$

>> __Special Case 1: $\underline{S}_{7}$ and $\underline{S}_{1}$ are Parallel__

>> - As mentioned above, problems are encountered when $\alpha_{71}$ is very
     close to either 0 or 180 degrees
>> - The first step to solving special case one is to set $S_{7}$ equal to zero
     ($S_{7} = 0$)
>> - The vector loop equation from above therefore simplifies to the following
     expression
>>      - $^{F}\underline{P}_{6orig} + a_{71} (^{F}\underline{a}_{71}) + S_{1}
          (^{F}\underline{S}_{1}) = \underline{0}$
>> - Now take the dot product of each term in the vector loop equation with
     vector $^{F}\underline{S}_{1}$
>>      - $^{F}\underline{P}_{6orig} \cdot ^{F}\underline{S}_{1} + a_{71}
          (^{F}\underline{a}_{71} \cdot ^{F}\underline{S}_{1}) + S_{1}
          (^{F}\underline{S}_{1} \cdot ^{F}\underline{S}_{1}) = \underline{0}$
>>      - The vectors $^{F}\underline{a}_{71}$ and $^{F}\underline{S}_{1}$ are
          perpendicular and so their dot product is zero and therefore the
          middle term goes away
>>      - The dot product of vector $^{F}\underline{S}_{1}$ with itself is one
          and so the vectors drop out of the last term in the expression
>> - Simplifying the above expression for the length $S_{1}$ gives the
     following expression
>>      - $S_{1} = - ^{F}\underline{P}_{6orig} \cdot ^{F}\underline{S}_{1}$
>> - Now we rearrange the vector loop equation so that the $a_{71}$ terms are
     all on one side
>>      - $-(^{F}\underline{P}_{6orig} + S_{1} (^{F}\underline{S}_{1})) =
          a_{71} (^{F}\underline{a}_{71})$
>> - From the expression the length can be found by recognizing that it
     represents the magnitude of the left hand side of the equation
>>      - $a_{71} = \| (^{F}\underline{P}_{6orig} + S_{1}
          (^{F}\underline{S}_{1})) \|$
>>      - If $a_{71} = 0$ then problems arise and the process has to move to
          special case 2
>> - Using the same expression above where the $a_{71}$ terms are isolated, the
     unit vector $^{F}\underline{a}_{71}$ can be found by dividing the left
     hand side of the equation by length $a_{71}$
>>      - $^{F}\underline{a}_{71} = \frac{-(^{F}\underline{P}_{6orig} + S_{1}
          (^{F}\underline{S}_{1}))}{a_{71}}$
>> - Now the same series of sin and cos equations as the normal case can be used
     to find the remaining angles $\theta_{7}$ and $\gamma_{1}$

>> __Special Case 2: $\underline{S}_{7}$ and $\underline{S}_{1}$ are Parallel
   and $a_{71} = 0$__

>> - If $\underline{S}_{7}$ and $\underline{S}_{1}$ are Parallel and $a_{71} =
     0$ then we set $S_{7} = 0$ and $\theta_{7} = 0$
>> - This makes $^{F}\underline{a}_{71} = ^{F}\underline{a}_{67}$
>> - The remaining value to find is the angle $\gamma_{1}$ which is found using
     sin and cos as it was for the normal case and special case one

> - The hypothetical link technique including the special cases can be
    summarized in the following flow chart taken from the lecture slides

<div align="center">
<table class="image">
<tr><td><img src="./img/hypothetical_link_flow.png"
alt="Hypothetical Link Flow Chart" title="Hypothetical Link Flow Chart"
width="800" height="700"/> 
</td></tr>
</table>
</div>

## Mobility {#mobility}

- Mobility is the determination of the degrees of freedom of the system
- For $n$ unconnected non-fixed bodies the mobility of the system is $M = 6n$
- For $n$ unconnected bodies with one fixed to ground the mobility of the
  system is $M = 6(n-1)$
- For a system of $n$ bodies with one fixed to the ground and the rest
  connected by $j$ joints the mobility of the system can be represented by $M =
  6(n-1) - \sum^{j}_{i=1} (6-f_{i})$
    - This equation does not hold for all cases but in general should be
      appliciable
- For a closed loop system the number of bodies is equivalent to the number of
  joints ($n = j$) and the mobility expression simplifies to $M =
  \sum^{n}_{i=1} f_{i} - 6$
- For an open loop robot there is one fewer joint than the number of bodies
  ($n-1 = j$) and the mobility expression simplifies to $M = \sum^{j}_{i=1}
  f_{i}$

## Planar Representation {#planar_representation}

- For convinence a 2D representation of a kinematic chain can be used instead
  of the 3D model
- When creating the planar representation simple lines will represent each link
  and each joint will be denoted with its shorthand letter
- In addition the grounded link can be denoted using the standard ground
  notation and the input and output angles of the system can be marked

<div align="center">
<table class="image">
<caption align="bottom">Figure From Lecture</caption>
<tr><td><img src="./img/planar_representation.png"
alt="Example Planar Representation" title="Example Planar Representation"
width="600" height="400"/> 
</td></tr>
</table>
</div>

## Equivalent Spherical Mechanisms {#equivalent_spherical_mechanisms}

- The equivalent spherical mechanism of a closed loop spatial mechanism will
  hold all twist angles constant and the $\underline{S}$ and $\underline{a}$
  vectors will remain parallel to their equivalents in the spatial mechanism,
  however translations will not be accounted for
    - The result is that any relations for the $\alpha$ and $\theta$ angles
      found in the spherical mechanism will also be valid in the closed loop
      spatial mechanism
- The $\underline{a}_{ij}$ vector is perpendicular to the plane formed by
  vectors $\underline{S}_{i}$ and $\underline{S}_{j}$
- The angle between the plane containing vectors $\underline{S}_{i}$ and
  $\underline{S}_{j}$ and the plane containing $\underline{S}_{j}$ and
  $\underline{S}_{k}$ is $\theta_{j}$

> __Create Equivalent Spherical Mechanism__

> - The first step to creating an equivalent spherical mechanism from a closed
    loop spatial mechanism is to take all of the $\underline{S}$ vectors and
    give them the same origin point
> - Now simply draw links lying on a sphere centered at the origin to hold the
    twist angles ($\alpha$'s) constant and connect them using revolute joints
    irregardless of what the joint was on the original closed loop spatial
    mechanism
>       - Prismatic joints become a revolute joint with a fixed joint angle
          $\theta$

<div align="center">
<table class="image">
<caption align="bottom">figure from lecture</caption>
<tr><td><img src="./img/spatial_to_spherical.png"
alt="spatial mechanism to spherical mechanism" title="spatial mechanism to
spherical mechanism" width="800" height="400"/> 
</td></tr>
</table>
</div>

> __Spherical Mechanism Groups__

> - The mobility of the spatial closed loop mechanism is 1 by definition and
    there are different categories of spherical mechanisms depending on what is
    their resultant mobility
> - The mobility of spherical mechanisms can be defined as $M_{spatial} =
    \sum^{j}_{i=1} f_{i} - 3$
> - Spherical mechanism groups are defined by their mobility
>       - Ex. Group 1 spherical mechanisms have $M = 1$
>       - Only goes up to group 4 because you end up with limitations on the
          ability to create a closed loop spatial mechanism with a mobility of
          one
>       - The spherical mechanism gets more difficult to solve for higher
          mobility in the mechanism (larger group number)

- The goal of the analysis now is to find all of the $\underline{a}$ and
  $\underline{S}$ vectors in the first coordinate system

> __Find $\mathbf{^{1}\underline{S}_{1}}$__

> - The first vector is already defined based on how we defined the standard
    coordinate systems
>       - $^{1}\underline{S}_{1} = \left[ 0 \\ 0 \\ 1 \right]$

> __Find $\mathbf{^{1}\underline{S}_{2}}$__

> - To find the direction of vector $\underline{S}_{2}$ in the first coordinate
    system we will use the rotation matrix that can be pulled from the
    transformation matrix derived in the forward analysis section
>       - $^{1}_{2}R =$ $\left[ \begin{array} c_{2} & -s_{2} & 0 \\ s_{2}c_{12}
          & c_{2}c_{12} & -s_{12} \\ s_{2}s_{12} & c_{2}s_{12} & c_{12}
          \end{array} \right]$
> - Using the rotation matrix the vector $\underline{S}_{2}$ can be found in
    the first coordinate system by the following expression
>       - $^{1}\underline{S}_{2} = ^{1}_{2}R ^{2}\underline{S}_{2} =$ $\left[
          \begin{array} c_{2} & -s_{2} & 0 \\ s_{2}c_{12} & c_{2}c_{12} &
          -s_{12} \\ s_{2}s_{12} & c_{2}s_{12} & c_{12} \end{array} \right]$
          $\left[ 0 \\ 0 \\ 1 \right]$ $= \left[ \begin{array} 0 \\ -s_{12} \\
          c_{12} \end{array} \right]$

> __Find $\mathbf{^{1}\underline{S}_{3}}$__

> - To find the orientation of the $\underline{S}_{3}$ vector in the first
    coordinate system we can use the expression
>       - $^{1}\underline{S}_{3} = ^{1}_{2}R^{2}_{3}R ^{3}\underline{S}_{3}$
>       - Note however that $^{2}_{3}R^{3}\underline{S}_{3}$ should give the
          same result vector as $^{1}\underline{S}_{2}$ with the indices
          increased by one
>       - $^{2}_{3}R^{3}\underline{S}_{3} =$ $\left[ \begin{array} 0 \\ -s_{23}
          \\ c_{23} \end{array} \right]$
> - When that vector is multiplied by $^{1}_{2}R$ matrix the following vector
    is the result
>       - $^{1}\underline{S}_{3} =$ $\left[ \begin{array} s_{23}s_{2} \\
          -(s_{12}c_{23} + c_{12}s_{23}c_{2}) \\ c_{12}c_{23} -
          s_{12}s_{23}c_{2} \end{array} \right]$

>>  __Single Subscript Notation__

>> - As can be imagined the result of the further vectors will become
     increasingly complicated and so a short hand notation has been developed
     to simplify the expressions

<div align="center">
<table class="image">
<tr><td><img src="./img/single_sub_notation.png"
alt="Single Subscript Notation" title="Single Subscript Notation" width="400"
height="400"/> 
</td></tr>
</table>
</div>

>> - For single subscript notation three different terms are created ($X$, $Y$,
     $Z$) and will have different meanings based on their subscript and whether
     or not they have a bar
>>      - $X \equiv ss_{\theta}$
>>      - $Y \equiv -(sc + csc_{\theta})$
>>      - $Z \equiv cc - ssc_{\theta}$
>> - For $S_{j}$, $\theta_{j}$ the single subscript notation will involve
     $\alpha_{ij}$ and $\alpha_{jk}$ and the order of the $\alpha$ angles
     depends on whether or not the $X$, $Y$, $Z$ terms have overbars
>>      - For no bar $\alpha_{ij}$ will be placed next to the $\theta_{j}$
          terms (the right side terms) and the angle $\alpha_{jk}$ will fill in
          the remaining terms
>>          - Notice $\alpha_{ij}$ is the first $\alpha$ term encountered in
              the figure when traveling in the no bar direction
>>      - With bar $\alpha_{jk}$ will be placed next to the $\theta_{j}$
          terms (the right side terms) and the angle $\alpha_{ij}$ will fill in
          the remaining terms
>>          - Notice $\alpha_{jk}$ is the first $\alpha$ term encountered in
              the figure when traveling in the bar direction
>> - The subscript in single subscript notation indicates which theta is
     included in its terms

> __Rewrite $\mathbf{^{1}\underline{S}_{3}}$__

> - With the formation of single subscript notation notice that the vector
    $^{1}\underline{S}_{3}$ can be rewritten as the following
>       - $^{1}\underline{S}_{3} =$ $\left[ \begin{array} \bar{X}_{2} \\
          \bar{Y}_{2} \\ \bar{Z}_{2} \end{array} \right]$

> __Find $\mathbf{^{1}\underline{S}_{4}}$__

> - The dirction of the vector $\underline{S}_{4}$ in the first coordinate
    system can be found by the multiplication of the series of rotation
    matrices
>       - $^{1}\underline{S}_{4} = ^{1}_{2}R^{2}_{3}R^{3}_{4}R
          ^{4}\underline{S}_{4}$
>       - Note that by similarity the expression for $\underline{S}_{4}$ in the
          second coordinate system is the same as the expression for
          $\underline{3}$ in the first coordinate system with subscripts
          increased by one
>           - $^{2}\underline{S}_{4} =$ $\left[ \begin{array} \bar{X}_{3} \\
          \bar{Y}_{3} \\ \bar{Z}_{3} \end{array} \right]$
> - When $^{2}\underline{S}_{4}$ is multiplied by the rotation matrix to
    transition to the first coordinate system the following expression emerges
>       - $^{1}\underline{S}_{4} = ^{1}_{2}R^{2}\underline{S}_{4} =$ $\left[
          \begin{array} \bar{X} c_{2} - \bar{Y} s_{2} \\ c_{12}(\bar{X} s_{2} +
          \bar{Y}c_{2}) - s_{12}\bar{Z} \\ s_{12}(\bar{X}s_{2} + \bar{Y}c_{2})
          + c_{12} \bar{Z} \end{array} \right]$

>> __Multi-Subscript Notation__

>> - Just like before a new notation is going to be introduced in order to make
     keeping track of the multitude of terms easier
>> - The general form for multiple notation is presented below
>>      - $X_{ab} = X_{a} c_{b} - Y_{a} s_{b}$
>>      - $Y_{ab} = c_{b,b \rightarrow 1} (X_{a} s_{b} + Y_{a} c_{b}) - s_{b,b
          \rightarrow 1}Z_{a}$
>>      - $Z_{ab} = s_{b,b \rightarrow 1} (X_{a} s_{b} + Y_{a} c_{b}) + c_{b,b
          \rightarrow 1}Z_{a}$
>> - In the above expressions the subscript a represents all but the last of
     the subscripts for that variable and b represents the last subscript
>>      - Ex. $X_{432} \rightarrow$ a = 43, b = 2
>>      - Ex. 2. $Z_{2345} \rightarrow$ a = 234, b = 5
>> - The subscript $b, b \rightarrow 1$ means that the subscript will be $b$
     and what ever the next number will be in the order of the subscripts
     whether that be ascending or descending
>>      - Ex. $X_{432} \rightarrow (b,b \rightarrow 1) = 21$
>>      - Ex. 2. $Z_{2345} \rightarrow (b,b \rightarrow 1) = 56$
>> - For double subscript notation the order $ij$ means the $X$, $Y$, $Z$ terms
     will not have bars and the order $ji$ means that they will have bars,
     where $i < j$

> __Rewrite $\mathbf{^{1}\underline{S}_{4}}$__

> - The term $^{1}\underline{S}_{4}$ can be simplified with the newly defined
    multisubscript notation to the following
>       - $^{1}\underline{S}_{4} =$ $\left[ \begin{array} X_{32} \\ Y_{32} \\
          Z_{32} \end{array} \right]$

> __Find $\mathbf{^{1}\underline{S}_{5}}$, $\mathbf{^{1}\underline{S}_{6}}$ and
  $\mathbf{^{1}\underline{S}_{7}}$__

> - Now that multi-subscript notation has been developed it is simple to
    represent the rest of the $S$ vectors in the first coordinate system
>       - $^{1}\underline{S}_{5} =$ $\left[ \begin{array} X_{432} \\ Y_{432} \\
          Z_{432} \end{array} \right]$
>       - $^{1}\underline{S}_{6} =$ $\left[ \begin{array} X_{5432} \\ Y_{5432}
          \\ Z_{5432} \end{array} \right]$
>       - $^{1}\underline{S}_{7} =$ $\left[ \begin{array} X_{65432} \\
          Y_{65432} \\ Z_{65432} \end{array} \right]$

> __Find $\mathbf{^{1}\underline{a}_{12}}$__

> - The vector $^{1}\underline{a}_{12}$ is already defined by how we set up the
    standard coordinate systems
>       - $^{1}\underline{a}_{12} =$ $\left[ \begin{array} 1 \\ 0 \\ 0
          \end{array} \right]$

> __Find $\mathbf{^{1}\underline{a}_{23}}$__

> - To find the orientation of the $\underline{a}_{23}$ in the first coordinate
    system we will use a the rotation matrix $^{1}_{2}R$
>       - $^{1}_{2}R =$ $\left[ \begin{array} c_{2} & -s_{2} & 0 \\ s_{2}c_{12}
          & c_{2}c_{12} & -s_{12} \\ s_{2}s_{12} & c_{2}s_{12} & c_{12}
          \end{array} \right]$
> - We can now find the desired vector in the first coordinate system
>       - $^{1}\underline{a}_{23} = ^{1}_{2}R^{2}\underline{a}_{23} =$ $\left[
          \begin{array} c_{2} \\ s_{2}c_{12} \\ s_{2}s_{12} \end{array}
          \right]$

> __Find $\mathbf{^{1}\underline{a}_{34}}$__

> - For the next a vector we can begin by noticing that rotating the
    $^{3}\underline{a}_{34}$ vector to the second coordinate system will have
    the same result as the last vector with all of the subscripts increased by
    one
>       - $^{2}\underline{a}_{34} =$ $\left[ \begin{array} c_{3} \\ s_{3}c_{23}
          \\ s_{3}s_{23} \end{array} \right]$
> - Now the rotation matrix will be used to find the orientation of the vector
    in the first coordinate system just like in the pervious case
>       - $^{1}\underline{a}_{34} = (^{1}_{2}R)^{2}\underline{a}_{34} =$
          $\left[ \begin{array} c_{2}c_{3} - s_{2}s_{3}c_{23} \\
          -s_{12}(s_{3}s_{23}) + c_{12}(s_{2}c_{3} + c_{2}s_{3}c_{23}) \\
          c_{12}(s_{3}s_{23}) + s_{12}(s_{2}c_{3} + c_{2}s_{3}c_{23})
          \end{array} \right]$

> __Double Subscript Notation for $\mathbf{\alpha}$ Terms__

> - Looking at the result vector $^{1}\underline{a}_{34}$ one would notice a
    similarity between it and the short hand notation used for the $S$ vectors,
    however, there are now thetas in the place of the alphas and vice versa and
    so we will now define a new set of notation
> - We will begin with the definitions for the new notation
>       - $U_{ij} = s_{i}s_{ij}$
>       - $V_{ij} = -(s_{j}c_{i} + c_{j}s_{i}c_{ij})$
>       - $W_{ij} = c_{j}c_{i} - s_{j}s_{i}c_{ij}$
> - Where $i$ does not have to be smaller than $j$, it just represents
    the order of the subscripts
> - The subscripts now represent the alpha contained by the notation instead of
    the theta like the previous notation

> __Rewrite $\mathbf{^{1}\underline{a}_{34}}$__

> - Using the newly defined notation the vector $^{1}\underline{a}_{34}$ can be
    rewritten
>       - $^{1}\underline{a}_{34} =$ $\left[ \begin{array} W_{32} \\
          -(U_{32}s_{12} + V_{32}c_{12}) \\ U_{32}c_{12} - V_{32}s_{12}
          \end{array} \right]$ $= \left[ \begin{array} W_{32} \\ -U_{321}^{*}
          \\ U_{321} \end{array} \right]$

> __Rewrite $\mathbf{^{1}\underline{a}_{45}}$ Through
  $\mathbf{^{1}\underline{a}_{67}$__

> - Rather than go through the process of defining the rest of the
    $\underline{a}$ vectors individually we note that they all follow the
    format of the above $\underline{a}$ vector and simply add a subscript for
    each successive vector
>       - $^{1}\underline{a}_{45} =$ $\left[ \begin{array} W_{432} \\
          -U_{4321}^{*} \\ U_{4321} \end{array} \right]$
>       - $^{1}\underline{a}_{56} =$ $\left[ \begin{array} W_{5432} \\
          -U_{54321}^{*} \\ U_{54321} \end{array} \right]$
>       - $^{1}\underline{a}_{67} =$ $\left[ \begin{array} W_{65432} \\
          -U_{654321}^{*} \\ U_{654321} \end{array} \right]$

> __Spherical Mechanism Equation Toolkit__

> - The next thing to do is to find expressions for each of the $\underline{S}$
    and $\underline{a}$ vectors for different spherical mechanism
    configurations. The process starts by looking at a spherical triangle and
    adds a link for analysis until a spherical heptagon is reached.
> - For each configuration the $\underline{S}$ vectors are rotated into
    different coordinate systems and these representations are equated with the
    $\underline{S}$ vectors found previously to create a "toolbox" of equations
    to use when solving problems.
>       - Note that each of these equations will be different for each
          spherical mechanism configuration (spherical quadralateral tools
          $\neq$ spherical hexagon tools)

>> Example results

>> - For a spherical triangle
>>      - $\bar{X}_{2} = s_{31}s_{1}$
>>      - $\bar{Y}_{2} = s_{32}c_{1}$
>>      - $\bar{Z}_{2} = c_{31}$

> - This process results in lots of equations and for brevity sake they will
    not be listed here. If needing the equations they are listed out in full in
    the appendix of the textbook

> __Solve $\mathbf{Ac_{\theta} + Bs_{\theta} + D = 0}$__

> - Problems of this form develop when attempting to solve group 1 spherical
    mechanisms
> - Two different methods were discussed in class where one is the "better"
    method

>>  Tan-Half Angle Method

>> - This method begins using the tangent half angle trig identity
>>      - $x_{1} = tan \left( \frac{\theta}{2} \right)$
>>      - $s_{\theta} = \frac{2x_{1}}{1+x_{1}^{2}}$
>>      - $c_{\theta} = \frac{1-x_{1}^{2}}{1+x_{1}^{2}}$
>> - Substituting these values into the original problem results in the
     following expression
>>      - $A \left( \frac{1-x_{1}^{2}}{1+x_{1}^{2}} \right) + B$ $\left(
          \frac{2x_{1}}{1+x_{1}^{2}} \right) + D = 0$
>> - After multiplying through by $\left( 1 + x_{1}^{2} \right)$ and regrouping
     by the x terms the following quadratic equation emerges
>>      - $x_{1}^{2} (D-A) + x_{1} (2B) + (D+A) = 0$
>>      - The quadratic formula can now be used to solve for x which can in
          turn be used to solve for $\theta$
>> - Potential problem points for this solution process are as follows:
>>      - The term under the radical can be negative leading to non-real
          solutions
>>          - This is a symptom of not having a feasible link configuration and
              not necessarily a problem with the solution method itself
>>      - There could be a divide by zero error if $D = A$
>>           - This is an issue with the solution method and not the mechanism
               itself

>> Trig Solution Method

>> - The second solution approach involves a few trig identities in its
     derivation
>> - The first step in the process is to divide each term in the equation by
     the root of $A^{2} + B^{2}$
>>      - $\frac{A}{\sqrt{A^{2}+B^{2}}} c_{\theta} +
          \frac{B}{\sqrt{A^{2}+B^{2}}} s_{\theta} +
          \frac{D}{\sqrt{A^{2}+B^{2}}} = 0$
>> - Now we note that the sum of the first two coefficients squared is
     equivalent to one due to the fact that it is adding together the
     components of the denominator
>>      - $\frac{A^{2}}{A^{2}+B^{2}} + \frac{B^{2}}{A^{2}+B^{2}} = 1$
>> - The next step is to turn the above fractions into sine and cosine by
     keeping in mind the following trig identity
>>      - $(s_{\gamma})^{2} + (c_{\gamma})^{2} = 1$
>> - We can therefore rewrite the fractions as follows
>>      - $\frac{A^{2}}{A^{2}+B^{2}} = (c_{\gamma})^{2}$
>>      - $\frac{B^{2}}{A^{2}+B^{2}} = (s_{\gamma})^{2}$
>>      - These definitions are used to determine the value of angle $\gamma$
>> - Using these new terms the original equation can be rewritten as follows
>>      - $c_{\gamma}c_{\theta} + s_{\gamma}s_{\theta} +
          \frac{D}{\sqrt{A^{2}+B^{2}}} = 0$
>>      - Note that the angle $\gamma$ has not much of a physical meaning but
          is just a term used in the solution process
>> - By moving the non-trig term to the other side of the equation the
     remaining trig terms form the difference between two angles identity
>>      - $c_{\gamma}c_{\theta} + s_{\gamma}s_{\theta} = -
          \frac{D}{\sqrt{A^{2}+B^{2}}} = cos(\theta - \gamma)$
>> - Now arccosine can be used to determine what the difference in the two
     angles are
>>      - $\theta - \gamma = cos^{-1} \left( - \frac{D}{\sqrt{A^{2}+B^{2}}}
          \right)$
>>      - If the link lengths are unfeasible then this is the step that will
          encounter problems as the argument in $cos^{-1}$ will not be between
          -1 and 1
>> - This will provide an A case and a B case and the corresponding $\theta$
     values can be found by the following
>>      - $\theta_{A} = (\theta - \gamma)_{A} + \gamma$
>>      - $\theta_{B} = (\theta - \gamma)_{B} + \gamma$
>> - This is considered the better solution approach as it only encounters
     problems for infeasible link lengths rather than also having a problem
     inherent to the solution approach

> __Spherical Pentagon Example__

> - For the example the following values are given
>       - $\alpha_{12}, \alpha_{23}, \alpha_{34}, \alpha_{45}, \alpha_{51}$
>       - $\theta_{4}, \theta_{5}$
> - The goal to solve for the following angles
>       - $\theta_{1}, \theta_{2}, \theta_{3}$
> - Any of the desired angles can be the first found angle and in this example
    we will start with finding $\theta_{2}$
> - When looking in the spherical equation "toolkit", the following expression
    is found that can be used to solve for $\theta_{2}$
>       - $Z_{45} = Z_{2}$
>       - The only unknown $\theta$ value in the above expression is the
          desired $\theta_{2}$
> - Only a single cosine expression was found for $\theta_{2}$ meaning that
    there will be A case and B case possibilities

## Group One Solution Process {#group_one_sol}

## Group Two Solution Process {#group_two_sol}

> __Form System of Two Equations__

>> Projection of Vector Loop Equation

>> Self-Scalar Product of Vector Loop Equation

>> Secondary Cosine Laws

>>> Dual Numbers

>>> Dual Angles

> __Solve $\mathbf{x^{2}_{3} \left( a_{i}x^{2}_{1} + b_{i}x_{1} + d_{i}
  \right)}$ $\mathbf{+ x_{3} \left( e_{i}x^{2}_{1} + f_{i}x_{1} + g_{i}
  \right)}$ $\mathbf{+ \left( h_{i}x^{2}_{1} + i_{i}x_{1} + j_{i} \right) = 0,
  \;\; i = 1,2}$__

>> Sylvester's Method

>> Bezout's Method
