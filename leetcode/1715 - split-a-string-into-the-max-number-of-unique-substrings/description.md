Given a string&nbsp;`` s ``<var>,</var>&nbsp;return _the maximum&nbsp;number of unique substrings that the given string can be split into_.

You can split string&nbsp;`` s `` into any list of&nbsp;__non-empty substrings__, where the concatenation of the substrings forms the original string.&nbsp;However, you must split the substrings such that all of them are __unique__.

A __substring__ is a contiguous sequence of characters within a string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "ababccc"
<strong>Output:</strong> 5
<strong>Explanation</strong>: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aba"
<strong>Output:</strong> 2
<strong>Explanation</strong>: One way to split maximally is ['a', 'ba'].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "aa"
<strong>Output:</strong> 1
<strong>Explanation</strong>: It is impossible to split the string any further.
</pre>

&nbsp;

__Constraints:__

*   
    
    `` 1 &lt;= s.length&nbsp;&lt;= 16 ``
    
    
*   
    
    `` s `` contains&nbsp;only lower case English letters.
    
    