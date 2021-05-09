Given a&nbsp;string `` s `` and an array of integers `` cost `` where `` cost[i] ``&nbsp;is the cost of deleting the <code>i<sup>th</sup></code> character in `` s ``.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abaac", cost = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "abc", cost = [1,2,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You don't need to delete any character because there are no identical letters next to each other.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "aabaa", cost = [1,2,3,4,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Delete the first and the last character, getting the string ("aba").
</pre>

&nbsp;

__Constraints:__

*   `` s.length == cost.length ``
*   `` 1 &lt;= s.length, cost.length &lt;= 10^5 ``
*   `` 1 &lt;= cost[i] &lt;=&nbsp;10^4 ``
*   `` s `` contains only lowercase English letters.