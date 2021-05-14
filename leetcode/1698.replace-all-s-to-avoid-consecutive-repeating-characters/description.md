Given a string&nbsp;`` s ``<var>&nbsp;</var>containing only lower case English letters&nbsp;and the '?'&nbsp;character, convert __all __the '?' characters into lower case letters such that the final string does not contain any __consecutive repeating&nbsp;__characters.&nbsp;You __cannot __modify the non '?' characters.

It is __guaranteed __that there are no consecutive repeating characters in the given string __except __for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them.&nbsp;It can be shown that an answer is always possible with the given constraints.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "?zs"
<strong>Output:</strong> "azs"
<strong>Explanation</strong>: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "ubv?w"
<strong>Output:</strong> "ubvaw"
<strong>Explanation</strong>: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "j?qg??b"
<strong>Output:</strong> "jaqgacb"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "??yw?ipkj?"
<strong>Output:</strong> "acywaipkja"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length&nbsp;&lt;= 100 ``
*   `` s `` contains&nbsp;only lower case English letters and `` '?' ``.