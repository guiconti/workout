The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.

Given an integer array `` nums ``, return _the sum of __Hamming distances__ between all the pairs of the integers in_ `` nums ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [4,14,2]
<strong>Output:</strong> 6
<strong>Explanation:</strong> In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [4,14,4]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code>