You are given two strings `` a `` and `` b `` that consist of lowercase letters. In one operation, you can change any character in `` a `` or `` b `` to __any lowercase letter__.

Your goal is to satisfy __one__ of the following three conditions:

*   __Every__ letter in `` a `` is __strictly less__ than __every__ letter in `` b `` in the alphabet.
*   __Every__ letter in `` b `` is __strictly less__ than __every__ letter in `` a `` in the alphabet.
*   __Both__ `` a `` and `` b `` consist of __only one__ distinct letter.

Return _the __minimum__ number of operations needed to achieve your goal._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> a = "aba", b = "caa"
<strong>Output:</strong> 2
<strong>Explanation:</strong> Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> a = "dabadd", b = "cda"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The best way is to make condition 1 true by changing b to "eee".
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= a.length, b.length &lt;= 10<sup>5</sup></code>
*   `` a `` and `` b `` consist only of lowercase letters.