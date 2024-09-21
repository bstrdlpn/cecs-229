# cecs-229
Class programming problems for CSULB CECS 229 - Discrete Mathematics II

## PA1
This is a problem set which covers the following objectives:
  1. Find all integers in a specified range where $x \equiv a\mod m$
  2. Find the _b_-representation of a given integer
  3. Apply numerical algorithms for computing the sum of two numbers in binary representation
  4. Apply numerical algorithms for computing the product of two numbers in binary representation

### Problem 1 - Things I learned   
The **goal** of this function is to return a list of all integers that satisfy two conditions:
1. $x$ such that $x \equiv a\mod m$
2. $low\leq x\leq high$

Since the definition of congruent to $b\mod m$ states that all integers $x$ that are equivalent to $a$ under modulo $m$ must satisfy 

$$x-a=m\cdot k\ \text{for some integer k}$$ 

this means that all $x$ values may be given by 

$$x=mk+a$$  

This also means that if all $x$ values must be in the range $\text{[low,high]}$, then 

$$low\leq mk+a \leq high$$

#### What lower and upper bound does this place on $k$?
Solving the inequality to isolate $k$, this just means that $k$ is bound to values within the inequality 

$$\frac{\text{low}-a}{m}\leq k \leq \frac{\text{high}-a}{m}$$

The $k$ values are the values that are plugged back into our equation for $x$ to obtain all values congruent to $a\mod m$.

### Problem 2 - Things I learned
The **goal** of this function is to return a string of $n$ in desired $n_{base}$ from inputs $n_{10}$ and the desired base. I noticed that I could iteratively obtain each subsequent positional indexed value in the string by performing $n\mod b$ on the initial input values of `n=number` and `b=base`, and assigning the new n to be the quotient from floor dividing by the base. This algorithm works because any number $n$ can be broken down into powers of base $b$, and because of how numbers are represented positionally.

Given that a number $n$ can be represented as $n=d_k\cdot b^k + d_{k-1}\cdot b^{k-1}+\dots +d_1\cdot b^1+d_0\cdot b^0$ where $d_i$ are the digits in the base and $b^i$ are powers of the base, performing the algorithm yields the digits of the base. In the algorithm, $d_i$ is the remainder obtained from taking the quotient mod base:

So as an example:
For $n = 10$ and base $b = 8$:
1. $10\mod 8=2$ (so, $d_0=2$)
2. $1 \mod 8=1 (so, $d_1=1$)

Thus yielding the number $(12)_8$. Going by how numbers can be represented as powers of base b:

$$10=1\cdot 8^1 + 2\cdot 8^0$$
