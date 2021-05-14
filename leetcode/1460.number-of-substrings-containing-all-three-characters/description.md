Given a string `` s ``&nbsp;consisting only of characters _a_, _b_ and _c_.

Return the number of substrings containing __at least__&nbsp;one occurrence of all these characters _a_, _b_ and _c_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abcabc"
<strong>Output:</strong> 10
<strong>Explanation:</strong> The substrings containing&nbsp;at least&nbsp;one occurrence of the characters&nbsp;<em>a</em>,&nbsp;<em>b</em>&nbsp;and&nbsp;<em>c are "</em>abc<em>", "</em>abca<em>", "</em>abcab<em>", "</em>abcabc<em>", "</em>bca<em>", "</em>bcab<em>", "</em>bcabc<em>", "</em>cab<em>", "</em>cabc<em>" </em>and<em> "</em>abc<em>" </em>(<strong>again</strong>)<em>. </em>
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aaacb"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substrings containing&nbsp;at least&nbsp;one occurrence of the characters&nbsp;<em>a</em>,&nbsp;<em>b</em>&nbsp;and&nbsp;<em>c are "</em>aaacb<em>", "</em>aacb<em>" </em>and<em> "</em>acb<em>".</em><em> </em>
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "abc"
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 3 &lt;= s.length &lt;= 5 x 10^4 ``
*   `` s ``&nbsp;only consists of&nbsp;_a_, _b_ or _c&nbsp;_characters.