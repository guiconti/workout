Given a string `` s ``, sort it in decreasing order based on the frequency of characters, and return _the sorted string_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "tree"
<strong>Output:</strong> "eert"
<strong>Explanation:</strong> 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "cccaaa"
<strong>Output:</strong> "aaaccc"
<strong>Explanation:</strong> Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "Aabb"
<strong>Output:</strong> "bbAa"
<strong>Explanation:</strong> "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code>
*   `` s `` consists of English letters and digits.