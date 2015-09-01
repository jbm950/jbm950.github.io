__An Introduction to Automatic Differentiation__  
__Written by Louis B. Rall and George F. Corliss__  
__Published in Computational Differentiation: Techniques, Applications
and Tools: January 1996__  
<a href="http://www.eng.mu.edu/corlissg/Pubs/Papers/1996d.ps.gz"
target="_blank">Full Article Download</a>

## Table of Contents

- [1. What Is Automatic Differentiation](#what_is_auto_diff)
- [2. How and Why Does AD Work](#how_why_ad_work)
- [3. Higher Derivatives and Taylor Series](#higher_derivaties_and_taylor_series)

## 1. What Is Automatic Differentiation {#what_is_auto_diff}

- Automatic differentiation is also known as computational differentiation,
  algorithmic differentiation and differentiation of algorithms
- Automatic differentiation is NOT symbolic differentiation
    - Symbolic differentiation is the computer equivalent to solving for the
      formulas for the derivatives of a function by hand
    - Automatic differentiation generally requires less memory and CPU time
      than symbolic differentiation
- Automatic differentiation is NOT the divided differences approximation of
  derivatives
    - Divided differences are inherently inexact
    - Reducing the size of $\Delta x$ to reduce the truncation error can lead
      to cancelling of significant digits in the numerator

## 2. How and Why Does AD Work {#how_why_ad_work}

- Basic automatic differentiation works by systematically applying the chain
  rule for taking derivatives
- When using automatic differentiation a formula is transformed into a code
  list where each element in the list performs one basic operation
    - Ex. $f(x,y) = (x^{2} + y)(x+3y^{2})$ becomes
    - $t_{1} = x \\ t_{2} = y \\ t_{3} = t_{1}^{2} \\ t_{4} = t_{3} + t_{2} \\
      t_{5} = t_{2}^{2} \\ t_{6} = 3*t_{5} \\ t_{7} = t_{1} +t_{6} \\ t_{8} =
      t_{4} * t_{7} = f(x,y)$
- The derivate is found for each term in the code list using traditional rules of calculus
    - $t_{1} = x$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\nabla t_{1} = [1, 0]$
    - $t_{2} = y$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\nabla t_{2} = [0, 1]$
    - $t_{3} = t_{1}^{2}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\nabla t_{3} = 2*t_{1} * \nabla t_{1}$ yields [$2t_{1}$, 0]
    - $t_{4} = t_{3} + t_{2}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\nabla t_{4} = \nabla t_{3} + \nabla t_{2}$ yields [$2t_{1}$, 1]
    - $t_{5} = t_{2}^{2}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\nabla t_{5} = 2*t_{2} * \nabla t_{2}$ yields [0, $2t_{2}$]
    - $t_{6} = 3*t_{5}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\nabla t_{6} = 3*\nabla t_{5}$ yields [0, $6t_{2}$]
    - $t_{7} = t_{1} + t_{6}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\nabla t_{7} = \nabla t_{1} + \nabla t_{6}$ yields [1, $6t_{2}$]
    - $t_{8} = t_{4} * t_{7} = f(x,y)$ &nbsp;&nbsp;&nbsp;&nbsp; $\nabla t_{8} = \nabla t_{4} * t_{7} + t_{4} * \nabla t_{7}$ yields [$3t_{1}^{2} + 6t_{1}t_{2}^{2} + t_{2}$, $t_{1} + 6t_{1}^{2}t_{2} + 9t_{2}^{2}$] when simplified down to $t_{1}$'s and $t_{2}$'s
- The previous example is an example of forward mode automatic differentiation
    - Reverse mode is the other main mode used by automatic differentiation
      software and will be discussed in section 5 of this article

## 3. Higher Derivatives and Taylor Series {#higher_derivatives_and_taylor_series}
