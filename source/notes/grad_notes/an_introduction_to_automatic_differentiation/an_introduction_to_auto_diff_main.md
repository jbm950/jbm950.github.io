__An Introduction to Automatic Differentiation__  
__Written by Louis B. Rall and George F. Corliss__  
__Published in Computational Differentiation: Techniques, Applications
and Tools: January 1996__  
<a href="http://www.eng.mu.edu/corlissg/Pubs/Papers/1996d.ps.gz"
target="_blank">Full Article Download</a>

## Table of Contents

- [1. What Is Automatic Differentiation](#what_is_auto_diff)
- [2. How and Why Does AD Work](#how_why_ad_work)

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

-
