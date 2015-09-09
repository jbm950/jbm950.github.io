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
    $\mathbf{u_{k}}$
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
>       - $Y_{1},...,Y_{K}$, $U_{1},...,U_{k}$ and D are specified sets
>       - $\mathbf{\Psi}$ is a known function refered to as the _trajectory constraint
          function_
> - The problem then reduces to minimize an objective function ($\alpha (
    \mathbf{y_{0}}, \mathbf{y_{1}},...,\mathbf{y_{k}}, \mathbf{u_{1}},...,
    \mathbf{u_{k}})$) with the constraints $\mathbf{y_{k}} = \mathbf{y_{k-1}} +
    \mathbf{\Phi_{k}}(\mathbf{y_{k-1}}, \mathbf{u_{k}})$, $\mathbf{y_{k}} \in
    Y_{k}$, $\mathbf{u_{k}} \in U_{k}$, and $\mathbf{\Psi}
    (\mathbf{y_{0}},...,\mathbf{y_{k}},\mathbf{u_{1}},...,\mathbf{u_{k}}) \in D$
>       - This form fits the basic problem statement given in section 1.1

> __Continuous Optimal Control__

> - In the continuous optimal control problem the relationship between the
    state vector $\mathbf{y}$ and the control vector $\mathbf{u}$ is given by
    $\mathbf{\dot{y}}(t) = \mathbf{\Phi}[\mathbf{y}(t),\mathbf{u}(t)]$ over the
    planning horizon $t \in [0,T]$
> - The problem can then be stated as minimize $\int^{t}_{0} \alpha
    [\mathbf{y}(t), \mathbf{u}(t)] dt$ subject to the constraints
    $\mathbf{\dot{y}}(t) = \mathbf{\Phi}[\mathbf{y}(t),\mathbf{u}(t)]$,
    &nbsp;&nbsp; $\mathbf{y}(t) \in Y$ and $\mathbf{u}(t) \in U$ for $t \in
    [0,T]$ and $\mathbf{\Psi}(\mathbf{y},\mathbf{u}) \in D$
> - The problem can now be approximated by a discrete solution if the planning
    horizon [0, T] is subdivided into K intervals of duration $\Delta$ such
    that $K\Delta = T$
>       - $\mathbf{y}(k\Delta) = \mathbf{y}_{k}$ and $\mathbf{u}(k\Delta) =
          \mathbf{u}_{k}$ for k = 1, ..., K
> - The problem can now be restated as minimize $\sum^{K}_{k=1} \alpha
    (\mathbf{y_{k}}, \mathbf{u_{k}})$ subject to the constraints
    $\mathbf{y_{k}} = \mathbf{y_{k-1}} + \Delta\mathbf{\Phi} (\mathbf{y_{k-1}},
    \mathbf{u_{k}})$, $\mathbf{y_{k}} \in Y$, and $\mathbf{u_{k}} \in U$ for k
    = 1, ..., K and $\mathbf{\Psi} (\mathbf{y_{0},..., \mathbf{y_{k}},
    \mathbf{u_{1}},..., \mathbf{u_{k}}) \in D$
