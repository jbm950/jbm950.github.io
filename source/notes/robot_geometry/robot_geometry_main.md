# Robot Geometry
**Taught by: Dr. Carl Crane**  
**Taken: FS 2015**  
**Text: Kinematic Analysis of Robot Manipulators**  
*by: C. Crane and J. Duffy*

## Table of Contents

- [Coordinate Systems](#coord_sys)
- [Coordinate Transformations](#coord_trans)

## Coordinate Systems {#coord_sys}

- A single coordinate system (A) defined by $\underline{x}_{A},
  \underline{y}_{A}, \underline{z}_{A}$ and $A_{0}$
- $A_{0}$ is the origin of the A coordinate system
- $\underline{x}_{A}, \underline{y}_{A}, \underline{z}_{A}$ are all unit
  vectors and are dimensionless because they represent direction not length
- In $^{B}\underline{x}_{A}$ the B represents what coordinate system the values
  are being given for and the A represents that the vector is the unit vector
  in the x direction in the A coordinate system

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

- Used to determine the position of a point from one coordinate system to another
    - Ex. point 1 may be defined in coordinate system B and it is desired to
      know the location of point 1 in coordinate system A
- To completely define the location and orientation from one coordinate system
  to another 6 values are needed (6 degrees of freedom)
