__Nonlinear Programming: Theory and Algorithms__  
__Written by Mokhtar S. Bazaraa, Hanif D. Sherali and C.M. Shetty__  
__Published as a book: May 2006__  
<a href="http://www.amazon.com/Nonlinear-Programming-Algorithms-Mokhtar-Bazaraa/dp/0471486000"
target="_blank">Physical Book (Amazon Link)</a>

## Table of Contents

- [1. Introduction](#introduction)

## Notation

- Vectors = boldface lowercase Roman letters (__x__, __y__, __z__)
    - All vectors are column vectors unless stated otherwise
- n-dimensional _real Euclidean space_ denoted as $R^{n}$
    - Composed of all real vectors of dimension _n_
- Matrices = boldface capital Roman letters (__A__, __B__)
- Scalar valued functions and scalars = lowercase Roman or Greek letters (f, g,
  $\lambda$)
- Vector values functions = boldface lowercase Roman or Greek letters (__g__,
  __$\mathbf{\psi}$__)
- Point to set maps = boldface capital Roman letters (__A__, __B__)

## 1. Introduction {#introduction}

### 1.1 Problem Statement and Basic Definitions

- General nonlinear programming problem set up as minimize function
  $f(\mathbf{x})$ subject to $g_{i}(\mathbf{x}) \leq 0$ for $i = 1,...,m$ and
  $h_{i}(\mathbf{x}) = 0$ for $i = 1,...,\el$ and $x \in X$
    - Function _f_ is the _objective function_ or _criterion function_
    - The $g_{i}(\mathbf{x}) \leq 0$ constraints are refered to as the
      _inequality constraints_
    - The $h_{i}(\mathbf{x}) = 0$ constraints are refered to as the _equality
      constraints_
    - Set $X$ might contain constraints on the variables
- A vector __x__, where __x__ $\in X$, that satisfies all of the constraints is
  called a _feasible solution_
- The collection of all feasible solutions form the _feasible region_
- The feasible solution, $\mathbf{\bar{x}}$, that is smaller than all the other
  feasible solutions ($f(\mathbf{x}) \geq f(\mathbf{\bar{x}})$) is called the
  _optimal solution_
    - Multiple optimum's might exist and are called _alternative optimal solutions_

### 1.2 Illustrative Examples

> __Discrete Optimal Control__

> - A problem is divided into K individual periods where $\mathbf{y_{k-1}}$ is
    the _state vector_ at the beginning of a period and is changed to
    $\mathbf{y_{k}}$ at the end of the period by the _control vector_
    $\mathbf{x_{k}}$
>       - The new state vector is determined by the following relationship:
          $\mathbf{y_{k}} = \mathbf{y_{k-1}} +
          \mathbf{\Phi_{k}}(\mathbf{y_{k-1}}, \mathbf{u_{k}})$ for k = 1,...,K
> - From the initial state $\mathbf{y_{0}}$ the sequence of controls
    ($\mathbf{u_{1}},...,\mathbf{u_{K}}$) resulting in a sequence of state
    vectors ($\mathbf{y_{1}},...,\mathbf{y_{K}}$) is refered to as the
    _trajectory_
> - Sequence of state and control vectors ($\mathbf{u_{1}},...,\mathbf{u_{K}}$
    and $\mathbf{y_{0}},\mathbf{y_{1}},...,\mathbf{y_{K}}$) are _admissible_ or
    _feasible_ if they satisfy $\mathbf{y_{k}} \in \mathbf{Y_{k}}$,
    $\mathbf{u_{k}} \in \mathbf{U_{k}}$ for k = 1,...,K and
    $\mathbf{\Psi}(\mathbf{y_{0}},...,\mathbf{y_{K}},
    \mathbf{u_{1}},...,\mathbf{u_{K}}) \in D$

