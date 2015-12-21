__Numerical Methods in Engineering With Python 3__  

__Written by Jaan Kiusalaas__  
__Book Published: 2013__  
<a href="http://www.amazon.com/Numerical-Methods-Engineering-Python-3/dp/1107033853"
target="_blank">Physical Book (Amazon Link)</a>

## Table of Contents

- [2. Systems of Linear Algebraic Equations](#systems_linear_eqns)

## 2. Systems of Linear Algebraic Equations {#systems_linear_eqns}

- [2.1 Introduction](#intro2)
- [2.2 Gauss Elimination Method](#gauss_elim)

### 2.1 Introduction {#intro2}

- This section deals with solving equations of the form
  $\mathbf{A}\underline{x} = \underline{b}$
    - Where $\underline{x}$ is a vector of unknowns, $\mathbf{A}$ is the
      coefficient matrix to the unknowns and $\underline{b}$ is a vector of
      constants

> __Augmented Coefficient Matrix__

> - The augmented coefficient matrix is a useful representation of the
    equations for computation purposes

<div align="center">
<table class="image">
<tr><td><img src="./img/augmentcoefmatrix.png"
alt="Augmented Coefficient Matrix" title="Augmented Coefficient Matrix"
width="400" height="400"/>
</td></tr>
</table>
</div>

> __Uniqueness of Solution__

> - A unique solution will result if the determinant of the A matrix is
    non-singular ($\| A \| \neq 0$)
>       - Means that the rows and columns are linearly independent
>       - Example
>           - $2x + y = 3$ &nbsp; (1)
>           - $4x + 2y = 6$ &nbsp; (2)
>           - eqn (1) * 2 = eqn (2) therefore the equations are not linearly
              independent
>           - (example taken from book)
> - A singular coefficient matrix results in infinite solutions or no solution

> __Ill Conditioning__

> - Ill conditioning occurs when the coefficient matrix is almost singular ($\|
    A \|$ is very small)
> - When the coefficient matrix is ill conditioned small changes in the
    coefficients result in large changes in the solutions
>       - This means that round off errors that coincide with numerical
          computation can have very large effects on the solution
>       - Example
>           - Case 1
>              - $2x + y = 3$
>              - $2x + 1.001y = 0$
>                   - $x = 1501.5$
>                   - $y = -3000$
>           - Case 2
>              - $2x + y = 3$
>              - $2x + 1.002y = 0$
>                   - $x = 751.5$
>                   - $y = -1500$
>           - A small change in the y coefficient in the second equation
              resulted in a large change in the solution 
>           - (example taken from book)

> - The comparison for "smallness" of the determinant of the coefficient matrix
    will be the matrix norm ($||A||$)
>       - $\| A \| \, << \, || A ||$ means that the determinant of A is small
> - There are different matrix norms that can be used for this purpose

>> __Euclidan Norm__

>> - $|| A ||_{e} = \sqrt{\sum^{n}_{i=1} \sum^{n}_{j=1} (A_{ij})^{2}}$

>> __Infinity Norm/Row-Sum Norm__

>> - $|| A ||_{\infty} = max_{1 \leq i \leq n} \sum^{n}_{j=1} \| A_{ij} \|$

>> __Matrix Condition Number__

>> - The matrix condition number is a formal measuring of the condition of a
     matrix and can be found as follows
>>      - $cond(A) = || A || \, || A^{-1} ||$
>> - A matrix condition number around one means that the matrix is well
     conditioned, condition number is $\infty$ for a singular matrix, and in
     general a larger condition number means the matrix is less well
     conditioned
>>      - $cond(A) = 1$ (Well conditioned)
>>      - $cond(A) = \infty$ (Singular Matrix)
>>      - $cond(A) \uparrow$ (Matrix is less well conditioned)
>> - The matrix condition number is not a unique value but rather depends on
     which matrix norm is used
>> - The matrix condition number can be computationally expensive to calculate
     for large matrices and so the magnitude of the determinant is compared to
     the magnitude of the elements of the coefficient matrix and similar
     magnitude signifies a well conditioned matrix

> __Methods of Solution__

>> __Direct Methods__

>> - Change the original equations into equivalent equations that are easier to
     solve and yield the same solution
>>      - Can change $\| A \|$
>> - Achieved by performing "elementary operations"
>>      1. Exchange 2 equations (changes sign of $\| A \|$)
>>      2. Multiply an equation by a non-zero constant (multiplies $\| A \|$ by
           the same constant)
>>      3. Multiply an equation by a non-zero constant and subtract it from
           another equation (no change to $\| A \|$)

>> __Indirect Methods__

>> - Start with a guess for a solution to the system and then iterate until the
     solution converges
>> - Generally less efficient than direct methods due to large number of
     iterations, however, can have computational advantages if the coefficient
     matrix is large and sparse

> __Triangular Matrices__

> - Triangular matrices consist of zeros below or above the leading diagonal

>> __Upper Triangular Matrix__

>> - An upper triangular matrix, U, consists entirely of zeros below the
     leading diagonal and numbers with no restrictions above the leading
     diagonal
>>      - Example $U =$ $\left[ \begin{array} U_{11} & U_{12} \\ 0 & U_{22}
          \end{array} \right]$

>> __Lower Triangular Matrix__

>> - A lower triangular matrix, L, consists entirely of zeros above the leading
     diagonal and numbers with no restrictions below the leading diagonal
>>      - Example $L =$ $\left[ \begin{array} L_{11} & 0 \\ L_{21} & L_{22}
          \end{array} \right]$

> __Forward/Back Substitution__

> - When the coefficient matrix is a triangular matrix the solution can be
    obtained easily by solving each equation individually for one unknown at a
    time

>> __Forward Substitution__

>> - In forward substitution the solution process begins at the first row of
     the matrices
>> - Example
>>      - $\left[ \begin{array} L_{11} & 0 \\ L_{21} & L_{22} \end{array}
          \right]$ $\left[ x_{1} \\ x_{2} \right]$ $= \left[ c_{1} \\ c_{2}
          \right]$
>>      - $x_{1} = c_{1} / L_{11}$
>>      - $x_{2} = (c_{2} - L_{21} x_{1}) / L_{22}$

>> __Back Substitution__

>> - In back substitution the solution process begins with the last row of the matrices
>> - Example
>>      - $\left[ \begin{array} U_{11} & U_{12} \\ 0 & U_{22} \end{array}
          \right]$ $\left[ x_{1} \\ x_{2} \right]$ $= \left[ c_{1} \\ c_{2}
          \right]$
>>      - $x_{2} = c_{2} / U_{22}$
>>      - $x_{1} = (c_{1} - U_{12} x_{2}) / U_{11}$

### 2.2 Gauss Elimination Method {#gauss_elim}
