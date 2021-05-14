A __happy string__ is a string that:

*   consists only of letters of the set `` ['a', 'b', 'c'] ``.
*   `` s[i] != s[i + 1] ``&nbsp;for all values of `` i `` from `` 1 `` to `` s.length - 1 `` (string is 1-indexed).

For example, strings __"abc", "ac", "b"__ and __"abcbabcbcb"__ are all happy strings and strings __"aa", "baa"__ and&nbsp;__"ababbc"__ are not happy strings.

Given two integers `` n `` and `` k ``, consider a list of all happy strings of length `` n `` sorted in lexicographical order.

Return _the kth string_ of this list or return an __empty string__&nbsp;if there are less than `` k `` happy strings of length `` n ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 1, k = 3
<strong>Output:</strong> "c"
<strong>Explanation:</strong> The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1, k = 4
<strong>Output:</strong> ""
<strong>Explanation:</strong> There are only 3 happy strings of length 1.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 3, k = 9
<strong>Output:</strong> "cab"
<strong>Explanation:</strong> There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 2, k = 7
<strong>Output:</strong> ""
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 10, k = 100
<strong>Output:</strong> "abacbabacb"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10 ``
*   `` 1 &lt;= k &lt;= 100 ``

<div id="vidyowebrtcscreenshare_is_installed">&nbsp;</div>