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

> - The rotation matrix for a rotation, $\theta$, around a general vector, m,
    passing through the origin is: 

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
     coordinate system B after a rotation $\theta$ about a generic vector m
>> - To begin consider a coordinate system C whose z-axis is along the vector m
     (the location of the x and y vectors will be arbitrary)
>> - The rotation matrix from C to A can then be defined as $^{A}_{C}R = \left[
     \begin{array} a_{x} & b_{x} & m_{x} \\ a_{y} & b_{y} & m_{y} \\ a_{z} &
     b_{z} & m_{z} \end{array} \right]$
>> - Now consider coordinate system D which is obtained by rotating coordinate
     system C about its z-axis by $\theta$ degrees
>> - The rotation matrix from D to C would then be defined as $^{C}_{D}R = \left[
     \begin{array} cos(\theta) & -sin(\theta) & 0 \\ sin(\theta) & cos(\theta) & 0 \\ 0 &
     0 & 1 \end{array} \right]$
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

## Links {#links}

- Links are rigid bodies that maintain orientation between two axes
- The two axes ($S_{i}$, $S_{j}$) contain a unique perpendicular between them
  ($a_{ij}$) where $a_{ij}$ is defined as the link length
    - If $S_{i}$ and $S_{j}$ intersect, then the link length is zero
    - The length $a_{ij}$ is positive if chosen in such that it points from
      $S_{i}$ to $S_{j}$
- The angle from $S_{i}$ to $S_{j}$ using the right hand rule with one's thumb
  on $a_{ij}$ is defined as $\alpha_{ij}$, where $\alpha_{ij}$ is called the
  twist angle
- It is common to replace all of the links in a system with their equivalent
  kinematic link
    - Kinematic link is represented by drawing just the $S_{i}$/$S_{j}$ axes
      and the link length

<div align="center">
<table class="image">
<tr><td><img src="./img/phy_to_kinematic_link.png"
alt="Physical to Kinematic Link" title="Physical to Kinematic Link" width="300"
height="200"/> 
</td></tr>
</table>
</div>

- Two special link cases are spherical links and planar links
    - In spherical links $S_{i}$ intersects $S_{j}$ and $a_{ij} = 0$
    - In planar links $S_{i}$ is parallel with $S_{j}$ and $\alpha_{ij} = 0$

## Joints {#joints}
