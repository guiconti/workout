Given a binary string `` s `` and an integer `` k ``.

Return `` true `` _if every binary code of length_ `` k `` _is a substring of_ `` s ``. Otherwise, return `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "00110110", k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "00110", k = 2
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "0110", k = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "0110", k = 2
<strong>Output:</strong> false
<strong>Explanation:</strong> The binary code "00" is of length 2 and doesn't exist in the array.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "0000000001011100", k = 4
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code>
*   `` s[i] `` is either `` '0' `` or `` '1' ``.
*   `` 1 &lt;= k &lt;= 20 ``