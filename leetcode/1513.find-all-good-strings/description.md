Given the strings `` s1 `` and `` s2 `` of size `` n `` and the string `` evil ``, return _the number of __good__ strings_.

A __good__ string has size `` n ``, it is alphabetically greater than or equal to `` s1 ``, it is alphabetically smaller than or equal to `` s2 ``, and it does not contain the string `` evil `` as a substring. Since the answer can be a huge number, return this __modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2, s1 = "aa", s2 = "da", evil = "b"
<strong>Output:</strong> 51 
<strong>Explanation:</strong> There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da".&nbsp;
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
<strong>Output:</strong> 0 
<strong>Explanation:</strong> All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 2, s1 = "gx", s2 = "gz", evil = "x"
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` s1.length == n ``
*   `` s2.length == n ``
*   `` s1 &lt;= s2 ``
*   `` 1 &lt;= n &lt;= 500 ``
*   `` 1 &lt;= evil.length &lt;= 50 ``
*   All strings consist of lowercase English letters.