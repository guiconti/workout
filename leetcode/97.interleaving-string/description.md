Given strings `` s1 ``, `` s2 ``, and `` s3 ``, find whether `` s3 `` is formed by an __interleaving__ of `` s1 `` and `` s2 ``.

An __interleaving__ of two strings `` s `` and `` t `` is a configuration where they are divided into __non-empty__ substrings such that:

*   <code>s = s<sub>1</sub> + s<sub>2</sub> + ... + s<sub>n</sub></code>
*   <code>t = t<sub>1</sub> + t<sub>2</sub> + ... + t<sub>m</sub></code>
*   `` |n - m| &lt;= 1 ``
*   The __interleaving__ is <code>s<sub>1</sub> + t<sub>1</sub> + s<sub>2</sub> + t<sub>2</sub> + s<sub>3</sub> + t<sub>3</sub> + ...</code> or <code>t<sub>1</sub> + s<sub>1</sub> + t<sub>2</sub> + s<sub>2</sub> + t<sub>3</sub> + s<sub>3</sub> + ...</code>

__Note:__ `` a + b `` is the concatenation of strings `` a `` and `` b ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg" style="width: 561px; height: 203px;"/>

<pre>
<strong>Input:</strong> s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s1 = "", s2 = "", s3 = ""
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= s1.length, s2.length &lt;= 100 ``
*   `` 0 &lt;= s3.length &lt;= 200 ``
*   `` s1 ``, `` s2 ``, and `` s3 `` consist of lowercase English letters.

&nbsp;

__Follow up:__ Could you solve it using only `` O(s2.length) `` additional memory space?