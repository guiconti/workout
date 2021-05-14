Given a string `` s ``&nbsp;of lowercase letters, you need to find the maximum number of __non-empty__ substrings of&nbsp;`` s ``&nbsp;that meet the following conditions:

1.   The substrings do not overlap, that is for any two substrings `` s[i..j] `` and `` s[k..l] ``, either `` j &lt; k `` or `` i &gt; l ``&nbsp;is true.
2.   A substring that contains a certain character&nbsp;`` c ``&nbsp;must also contain all occurrences of `` c ``.

Find _the maximum number of substrings that meet the above conditions_. If there are multiple solutions with the same number of substrings, _return the one with minimum total length.&nbsp;_It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in __any__ order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "adefaddaccc"
<strong>Output:</strong> ["e","f","ccc"]
<b>Explanation:</b>&nbsp;The following are all the possible substrings that meet the conditions:
[
&nbsp; "adefaddaccc"
&nbsp; "adefadda",
&nbsp; "ef",
&nbsp; "e",
  "f",
&nbsp; "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "abbaccd"
<strong>Output:</strong> ["d","bb","cc"]
<b>Explanation: </b>Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 10^5 ``
*   `` s ``&nbsp;contains only lowercase English letters.