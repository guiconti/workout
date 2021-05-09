Given a string `` s ``, partition `` s `` such that every substring of the partition is a palindrome.

Return _the minimum cuts needed_ for a palindrome partitioning of `` s ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "aab"
<strong>Output:</strong> 1
<strong>Explanation:</strong> The palindrome partitioning ["aa","b"] could be produced using 1 cut.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "a"
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "ab"
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 2000 ``
*   `` s `` consists of lower-case English letters only.