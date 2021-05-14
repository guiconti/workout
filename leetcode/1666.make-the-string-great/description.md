Given a string `` s `` of lower and upper case English letters.

A good string is a string which doesn't have&nbsp;__two adjacent characters__ `` s[i] `` and `` s[i + 1] `` where:

*   `` 0 &lt;= i &lt;= s.length - 2 ``
*   `` s[i] `` is a lower-case letter and `` s[i + 1] `` is the same letter but in upper-case&nbsp;or __vice-versa__.

To make the string good, you can choose __two adjacent__ characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return _the string_ after making it good. The answer is guaranteed to be unique under the given constraints.

__Notice__ that an empty string is also good.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "leEeetcode"
<strong>Output:</strong> "leetcode"
<strong>Explanation:</strong> In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "abBAcC"
<strong>Output:</strong> ""
<strong>Explanation:</strong> We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --&gt; "aAcC" --&gt; "cC" --&gt; ""
"abBAcC" --&gt; "abBA" --&gt; "aA" --&gt; ""
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "s"
<strong>Output:</strong> "s"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 100 ``
*   `` s `` contains only lower and upper case English letters.