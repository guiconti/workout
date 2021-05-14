Given a string `` s `` formed by digits (`` '0' `` - `` '9' ``)&nbsp;and `` '#' ``&nbsp;.&nbsp;We want to map `` s `` to English lowercase characters as follows:

*   Characters (`` 'a' `` to `` 'i') `` are&nbsp;represented by&nbsp;(`` '1' `` to&nbsp;`` '9' ``)&nbsp;respectively.
*   Characters (`` 'j' `` to `` 'z') `` are represented by (`` '10#' ``&nbsp;to&nbsp;`` '26#' ``)&nbsp;respectively.&nbsp;

Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "10#11#12"
<strong>Output:</strong> "jkab"
<strong>Explanation:</strong> "j" -&gt; "10#" , "k" -&gt; "11#" , "a" -&gt; "1" , "b" -&gt; "2".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "1326#"
<strong>Output:</strong> "acz"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "25#"
<strong>Output:</strong> "y"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
<strong>Output:</strong> "abcdefghijklmnopqrstuvwxyz"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 1000 ``
*   `` s[i] `` only contains digits letters (`` '0' ``-`` '9' ``) and `` '#' ``&nbsp;letter.
*   `` s `` will be valid string&nbsp;such that mapping is always possible.