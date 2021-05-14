A string `` s `` is __nice__ if, for every letter of the alphabet that `` s `` contains, it appears __both__ in uppercase and lowercase. For example, `` "abABB" `` is nice because `` 'A' `` and `` 'a' `` appear, and `` 'B' `` and `` 'b' `` appear. However, `` "abA" `` is not because `` 'b' `` appears, but `` 'B' `` does not.

Given a string `` s ``, return _the longest __substring__ of `` s `` that is __nice__. If there are multiple, return the substring of the __earliest__ occurrence. If there are none, return an empty string_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "YazaAay"
<strong>Output:</strong> "aAa"
<strong>Explanation: </strong>"aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "Bb"
<strong>Output:</strong> "Bb"
<strong>Explanation:</strong> "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "c"
<strong>Output:</strong> ""
<strong>Explanation:</strong> There are no nice substrings.</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "dDzeE"
<strong>Output:</strong> "dD"
<strong>Explanation: </strong>Both "dD" and "eE" are the longest nice substrings.
As there are multiple longest nice substrings, return "dD" since it occurs earlier.</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 100 ``
*   `` s `` consists of uppercase and lowercase English letters.