You are given a license key represented as a string `` s `` that consists of only alphanumeric characters and dashes. The string is separated into `` n + 1 `` groups by `` n `` dashes. You are also given an integer `` k ``.

We want to reformat the string `` s `` such that each group contains exactly `` k `` characters, except for the first group, which could be shorter than `` k `` but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return _the reformatted license key_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "5F3Z-2e-9-w", k = 4
<strong>Output:</strong> "5F3Z-2E9W"
<strong>Explanation:</strong> The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "2-5g-3-J", k = 2
<strong>Output:</strong> "2-5G-3J"
<strong>Explanation:</strong> The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s `` consists of English letters, digits, and dashes `` '-' ``.
*   <code>1 &lt;= k &lt;= 10<sup>4</sup></code>