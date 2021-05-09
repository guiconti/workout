We define `` str = [s, n] `` as the string `` str `` which consists of the string `` s `` concatenated `` n `` times.

*   For example, `` str == ["abc", 3] =="abcabcabc" ``.

We define that string `` s1 `` can be obtained from string `` s2 `` if we can remove some characters from `` s2 `` such that it becomes `` s1 ``.

*   For example, `` s1 = "abc" `` can be obtained from <code>s2 = "ab<strong><u>dbe</u></strong>c"</code> based on our definition by removing the bolded underlined characters.

You are given two strings `` s1 `` and `` s2 `` and two integers `` n1 `` and `` n2 ``. You have the two strings `` str1 = [s1, n1] `` and `` str2 = [s2, n2] ``.

Return _the maximum integer _`` m ``_ such that _`` str = [str2, m] ``_ can be obtained from _`` str1 ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre><strong>Input:</strong> s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s1.length, s2.length &lt;= 100 ``
*   `` s1 `` and `` s2 `` consist of lowercase English letters.
*   <code>1 &lt;= n1, n2 &lt;= 10<sup>6</sup></code>