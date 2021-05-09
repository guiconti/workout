We define the string `` s `` to be the infinite wraparound string of `` "abcdefghijklmnopqrstuvwxyz" ``, so `` s `` will look like this:

*   `` "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...." ``.

Given a string `` p ``, return _the number of __unique non-empty substrings__ of _`` p ``_ are present in _`` s ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> p = "a"
<strong>Output:</strong> 1
Explanation: Only the substring "a" of p is in s.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> p = "cac"
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two substrings ("a", "c") of p in s.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> p = "zab"
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= p.length &lt;= 10<sup>5</sup></code>
*   `` p `` consists of lowercase English letters.