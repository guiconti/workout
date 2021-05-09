Return the number of permutations of 1 to `` n `` so that prime numbers are at prime indices (1-indexed.)

_(Recall that an integer&nbsp;is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers&nbsp;both smaller than it.)_

Since the answer may be large, return the answer __modulo `` 10^9 + 7 ``__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 12
<strong>Explanation:</strong> For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 100
<strong>Output:</strong> 682289015
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 100 ``