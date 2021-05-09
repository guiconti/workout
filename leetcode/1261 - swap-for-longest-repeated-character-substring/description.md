Given a string `` text ``, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> text = "ababa"
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> text = "aaabaaa"
<strong>Output:</strong> 6
<strong>Explanation:</strong> Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> text = "aaabbaaa"
<strong>Output:</strong> 4
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> text = "aaaaa"
<strong>Output:</strong> 5
<strong>Explanation:</strong> No need to swap, longest repeated character substring is "aaaaa", length is 5.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> text = "abcdef"
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= text.length &lt;= 20000 ``
*   `` text `` consist of lowercase English characters only.