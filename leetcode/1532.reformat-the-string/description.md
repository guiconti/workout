Given alphanumeric string `` s ``. (__Alphanumeric string__ is a string consisting of lowercase English letters and digits).

You have to find a permutation of&nbsp;the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return _the reformatted string_ or return __an empty string__ if it is impossible to reformat the string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "a0b1c2"
<strong>Output:</strong> "0a1b2c"
<strong>Explanation:</strong> No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> ""
<strong>Explanation:</strong> "leetcode" has only characters so we cannot separate them by digits.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "1229857369"
<strong>Output:</strong> ""
<strong>Explanation:</strong> "1229857369" has only digits so we cannot separate them by characters.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "covid2019"
<strong>Output:</strong> "c2o0v1i9d"
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "ab123"
<strong>Output:</strong> "1a2b3"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 500 ``
*   `` s `` consists of only lowercase English letters and/or digits.