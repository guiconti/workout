A string `` s `` is called __good__ if there are no two different characters in `` s `` that have the same __frequency__.

Given a string `` s ``, return_ the __minimum__ number of characters you need to delete to make _`` s ``_ __good__._

The __frequency__ of a character in a string is the number of times it appears in the string. For example, in the string `` "aab" ``, the __frequency__ of `` 'a' `` is `` 2 ``, while the __frequency__ of `` 'b' `` is `` 1 ``.

&nbsp;

__Example 1:__

<strong>Input:</strong> s = "aab"
    <strong>Output:</strong> 0
    <strong>Explanation:</strong> s is already good.

__Example 2:__

<pre>
<strong>Input:</strong> s = "aaabbbcc"
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "ceabaacb"
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s ``&nbsp;contains only lowercase English letters.