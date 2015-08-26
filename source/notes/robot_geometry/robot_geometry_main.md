# Robot Geometry
**Taught by: Dr. Carl Crane**  
**Taken: FS 2015**  
**Text: Kinematic Analysis of Robot Manipulators**  
*by: C. Crane and J. Duffy*

## Table of Contents

- [Coordinate Systems](#coord_sys)
- [Coordinate Transformations](#coord_trans)
- [Homogeneous Coordinates](#homogeneous_coordinates)

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

## Homogeneous Coordinates {#homogeneous_coordinates}

- Four coordinates to define a vector (X, Y, Z, w)
    - X = $\frac{x}{w}$
    - Y = $\frac{y}{w}$
    - Z = $\frac{z}{w}$
- Advantage of using homogeneous coordinates is that as w goes to zero the
  vectors point to infinity therefore there are unique vectors that point to
  infinity

> ### Transformation Matrix

> - Coordinate system transformations with rotation matrices can be further simpified by using a transformation matrix that is defined as 

<div align="center">
<table class="image">
<tr><td><img src="./img/transformation_matrix_definition.png"
alt="Transformation Matrix Definition" title="Transformation Matrix
Definition" width="200" height="200"/>
</td></tr>
</table>
</div>

- The coordinate transformation can then be re-written from
  $^{A}\underline{P}_{1} = ^{A}\underline{P}_{B_{0}} + ^{A}_{B}R^{B}P_{1}$ to
  $^{A}\underline{P}_{1} = (^{A}_{B}T)^{B}\underline{P}_{1}$
