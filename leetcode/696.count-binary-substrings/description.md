Give a binary string `` s ``, return the number of non-empty substrings that have the same number of `` 0 ``'s and `` 1 ``'s, and all the `` 0 ``'s and all the `` 1 ``'s in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "00110011"
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "10101"
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s[i] `` is either `` '0' `` or `` '1' ``.