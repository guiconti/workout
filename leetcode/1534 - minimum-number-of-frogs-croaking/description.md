Given the string `` croakOfFrogs ``, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed.&nbsp;_Return the minimum number of _different_ frogs to finish all the croak in the given string._

A valid "croak"&nbsp;means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’&nbsp;__sequentially__.&nbsp;The frogs have to print all five letters to finish a croak.&nbsp;If the given string is not a combination of valid&nbsp;"croak"&nbsp;return -1.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> croakOfFrogs = "croakcroak"
<strong>Output:</strong> 1 
<strong>Explanation:</strong> One frog yelling "croak<strong>"</strong> twice.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> croakOfFrogs = "crcoakroak"
<strong>Output:</strong> 2 
<strong>Explanation:</strong> The minimum number of frogs is two.&nbsp;
The first frog could yell "<strong>cr</strong>c<strong>oak</strong>roak".
The second frog could yell later "cr<strong>c</strong>oak<strong>roak</strong>".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> croakOfFrogs = "croakcrook"
<strong>Output:</strong> -1
<strong>Explanation:</strong> The given string is an invalid combination of "croak<strong>"</strong> from different frogs.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> croakOfFrogs = "croakcroa"
<strong>Output:</strong> -1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;=&nbsp;croakOfFrogs.length &lt;= 10^5 ``
*   All characters in the string are: `` 'c' ``, `` 'r' ``, `` 'o' ``, `` 'a' `` or `` 'k' ``.