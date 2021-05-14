A string is called a __happy prefix__ if is a __non-empty__ prefix which is also a suffix (excluding itself).

Given a string `` s ``, return _the __longest happy prefix__ of_ `` s ``. Return an empty string `` "" `` if no such prefix exists.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "level"
<strong>Output:</strong> "l"
<strong>Explanation:</strong> s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "ababab"
<strong>Output:</strong> "abab"
<strong>Explanation:</strong> "abab" is the largest prefix which is also suffix. They can overlap in the original string.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "leetcodeleet"
<strong>Output:</strong> "leet"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "a"
<strong>Output:</strong> ""
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s `` contains only lowercase English letters.