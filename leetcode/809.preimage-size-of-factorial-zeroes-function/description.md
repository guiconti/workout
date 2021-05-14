Let `` f(x) `` be the number of zeroes at the end of `` x! ``. (Recall that `` x! = 1 * 2 * 3 * ... * x ``, and by convention, `` 0! = 1 ``.)

For example, `` f(3) = 0 `` because 3! = 6 has no zeroes at the end, while `` f(11) = 2 `` because 11! = 39916800 has 2 zeroes at the end. Given `` K ``, find how many non-negative integers `` x `` have the property that `` f(x) = K ``.

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> K = 0
<strong>Output:</strong> 5
<strong>Explanation:</strong> 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

<strong>Example 2:</strong>
<strong>Input:</strong> K = 5
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no x such that x! ends in K = 5 zeroes.
</pre>

__Note:__

*   `` K `` will be an integer in the range `` [0, 10^9] ``.