__Nonlinear Programming: Theory and Algorithms__  
__Written by Mokhtar S. Bazaraa, Hanif D. Sherali and C.M. Shetty__  
__Published as a book: May 2006__  
<a href="http://www.amazon.com/Nonlinear-Programming-Algorithms-Mokhtar-Bazaraa/dp/0471486000"
target="_blank">Physical Book (Amazon Link)</a>

## Table of Contents

- [1. Introduction](#introduction)
- [2. Convex Sets](#convex_sets)
- [4. The Fritz John and Karush-Kuhn-Tucker Optimality Conditions](#fritz_john_and_KKT_optimality_conditions)

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
    - Multiple optimum's might exist and are called _alternative optimal
      solutions_

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

## 2. Convex Sets {#convex_sets}

### 2.1 Convex Hulls

> __Convex Sets__

> - A set is _convex_ if the line segment joining any two points in a set does
    not leave the boundary of the set (is also contained in the set)
>       - This can be stated mathematically as $\sum^{k}_{j=1}
          \lambda_{j}\mathbf{x}_{j}$ where $\sum^{k}_{j} \lambda_{j} = 1$,
          $\lambda_{j} \geq 0$ for $j = 1,...,k$ meaning the weighted averages
          of the __x__ values are also within the set
>           - These weighted averages are called _convex combinations_ of
              $\mathbf{x}_{1},...,\mathbf{x}_{k}$
>           - Getting rid of the non-negativity requirement for $\lambda$
              ($\lambda_{j} \geq 0$) results in the requirements for an _affine
              combination_
>           - The combination $\sum^{k}_{j=1} \lambda_{j}\mathbf{x}_{j}$ where
              the only requirement on $\lambda_{j}$ is that it is in $R$ is
              called a _linear combination_
> - Some properties of convex sets include
>       1. The intersection of two convex sets is convex ($S_{1} \cap S_{2}$ is
           convex)
>       2. The sum of two convex sets is convex ($S_{1} \oplus S_{2}$ is convex)
>       3. The difference of two convex sets is convex ($S_{1} \ominus S_{2}$
           is convex)

<div align="center">
<table class="image">
<caption align="bottom">Figure taken from the book</caption>
<tr><td><img src="./img/convex_sets.jpg"
alt="Convex Sets" title="Convex Sets" width="400" height="250"/> 
</td></tr>
</table>
</div>

> __Convex Hulls__

> - A convex hull is the intersection of all of the convex sets containing set
    S (the smallest convex set containing S) where S is an arbitrary set in
    $R^{n}$
>       - The convex hull is denoted _conv(S)_
>       - The convex hull is subject to the same mathematical constraints as
          the convex set: $\mathbf{x} = \sum^{k}_{j=1}
          \lambda_{j}\mathbf{x}_{j}$ where $\sum^{k}_{j} \lambda_{j} = 1$,
          $\lambda_{j} \geq 0$ for $j = 1,...,k$ for
          $\mathbf{x_{1}},...,\mathbf{x_{k}} \in S$
>           - An _affine hull_ of S is the collection of all affine
              combinations of points in S 
>           - A _linear hull_ of S is the collection of all linear combinations
              of points in S

> __Polytope and Simplex__

> - A _polytope_ is the convex hull of a finite number of points
    $\mathbf{x_{1}},...,\mathbf{x_{k+1}}$ in $R^{n}$
> - If $\mathbf{x_{2}} - \mathbf{x_{1}}, \mathbf{x_{3}} - \mathbf{x_{1}},...,
    \mathbf{x_{k+1}} - \mathbf{x_{1}}$ are linearlly independent then
    $\mathbf{x_{1}},...,\mathbf{x_{k+1}}$ are _affinely independent_
> - The convex hull of a set of affinely independent points
    (conv($\mathbf{x_{1}},...\mathbf{x_{k+1}}$)) is called a _simplex_ with
    vertices $\mathbf{x_{1}},...,\mathbf{x_{k+1}}$
>       - Maximum number of linearlly independent vectors in $R^{n}$ is n
          $\rightarrow$ no simplex in $R^{n}$ with more than n + 1 vertices

> __Carath&eacute;odory Theorem__

### 2.2 Closure and Interior of a Set

> __Neighborhood__

> - The neighborhood around a point is the area/volume surrounding that point
> - The neighborhood can be represented by the set $N_{\epsilon}(\mathbf{x}) =
    \left{ \mathbf{y}: ||\mathbf{y} - \mathbf{x}|| < \epsilon \right}$

> __Closure__

> - A point x is in the closure of a set S if $S \cap N_{\epsilon}(\mathbf{x})
    \neq \emptyset$ for EVERY $\epsilon > 0$
> - This mathematical definition is saying that point x is in the closure of S
    if there is an intersection of the area around the point and S as the
    radius of that area goes to zero
> - The closure of set S is represented by cl S
> - A _Closed_ set is a set where the set is equivalent to its closure (S = cl S)
>       - This includes both the interior of S and its boundary

> __Interior__

> - A point x is in the interior of a set S if $N_{\epsilon}(\mathbf{x})
    \subset S$ for SOME $\epsilon > 0$
> - The mathematical definition is saying that point x is in the interior of S
    if for some radius larger than zero the entirety of the neighborhood is
    enclosed in S, however, it is understood that as the radius increases it
    will eventually not be enclosed by S
> - The interior of set S is represented by int S
> - A _Solid_ set S $\subseteq$ $R^{n}$ is a set with a nonempty interior (int
    S $\neq$ $\emptyset$)
> - An _Open_ set is a set where the set is equal to its interior (S = int S)

> __Boundary__

> - A point x is in the boundary of a set S if $N_{\epsilon}(x)$ contains one
    point in S and one point not in S for every $\epsilon > 0$
> - The above definition is saying that point x is in the boundary of S if its
    neighborhood includes both a portion outside of set S and a portion inside
    of set S for any radius
> - The boundary of S is represented by $\partial$S
> - Set S is considered _Bounded_ if it can be contained by a ball of
    sufficiently large radius
> - Boundary points of any set and its complement are the same

- _Compact_ set is a set that is both closed and bounded
- The complement of an open set is a closed set and vice versa

- The line segment between a point in cl S and a point in int S, where S is a
  convex set with a nonempty interior, is within the interior of set S
  (excluding the endpoints)
- Corollaries from the line segment definition:
    1. If set S is convex then its interior is convex
    2. If set S is convex with a nonempty interior then its closure is convex
    3. If set S is convex with a nonempty interior then cl(int S) = cl S
    4. If set S is convex with a nonempty interior then int(cl S) = int S

### 2.3 Weierstrass's Theorem

> __Greatest Lower Bound and Least Upper Bound__

> - The _greatest lower bound_ of set S is the largest possible scalar $\alpha$
    such that $\alpha \leq x$ for $x \in S$
> - This means that the greatest lower bound is the point that reaches the
    lowest point of set S
> - The greatest lower bound is also refered to as the _infimum_ of set S and
    is denoted by $inf \left{ x: x \in S \right}$

> - The _least upper bound_ of set S is the smallest possible scalar $\alpha$
    such that $\alpha \geq x$ for $x \in S$
> - This means that the least upper bound is the point that matches the highest
    point of S but no higher
> - The least upper bound is also refered to as the _supremum_ of set S and is
    denoted by  $sup\left{ x: x \in S \right}$

> __Weierstrass's Theorem__

> - If set S is nonempty, closed and bounded (compact) and f is continuous on S
    then a minimum of $\left{ f(\mathbf{x}): \mathbf{x} \in S \right}$ exists

## 4. The Fritz John and Karush-Kuhn-Tucker Optimality Conditions {#fritz_john_and_KKT_optimality_conditions}

### 4.1 Unconstrained Problems

- The general form of an unconstrained problem is to minimize $f(\mathbf{x})$
  without any constraints on the vector $\mathbf{x}$

> __Minimum Values__

> - When minimizing a function $f(\mathbf{x})$ over $R^{n}$ with
    $\mathbf{\bar{x}} \in R^{n}$ the point $\mathbf{\bar{x}}$ is a _local
    minimum_ if there exists an $\epsilon$ neighborhood around
    $\mathbf{\bar{x}}$ such that $f(\mathbf{\bar{x}}) \leq f(\mathbf{x})$ for
    $\mathbf{x} \in N_{\epsilon}(\mathbf{\bar{x}})$
> - If the local minimum $\mathbf{\bar{x}}$ satisfies $f(\mathbf{\bar{x}}) <
    f(\mathbf{x})$ for $\mathbf{x} \in N_{\epsilon}(\mathbf{\bar{x}})$ where
    $\mathbf{x} \neq \mathbf{\bar{x}}$ then the value is refered to as a
    _strict local minimum_
> - Lastly if the optimal solution $\mathbf{\bar{x}}$ satisfies
    $f(\mathbf{\bar{x}}) \leq f(\mathbf{x})$ for all $\mathbf{x} \in R^{n}$
    then the value is refered to as a _global minimum_
>       - Note that all global minimums are also local minimums

> __Necessary and Sufficient Conditions__

> - Necessary conditions are conditions which must be satisfied for every local
    optimal solution, however, satisfying them does not prove that the point is
    a local optimal solution
> - Sufficient Conditions are conditions that, when satisfied, are enough to
    prove that a point is a local optimal solution

> __Descent Direction__
