Given a string `` s `` and a string array `` dictionary ``, return _the longest string in the dictionary that can be formed by deleting some of the given string characters_. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
<strong>Output:</strong> "apple"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "abpcplea", dictionary = ["a","b","c"]
<strong>Output:</strong> "a"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 1000 ``
*   `` 1 &lt;= dictionary.length &lt;= 1000 ``
*   `` 1 &lt;= dictionary[i].length &lt;= 1000 ``
*   `` s `` and `` dictionary[i] `` consist of lowercase English letters.