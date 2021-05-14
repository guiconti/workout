Given an integer `` n ``, return _the number of strings of length _`` n ``_ that consist only of vowels (_`` a ``_, _`` e ``_, _`` i ``_, _`` o ``_, _`` u ``_) and are __lexicographically sorted__._

A string `` s `` is __lexicographically sorted__ if for all valid `` i ``, `` s[i] `` is the same as or comes before `` s[i+1] `` in the alphabet.

&nbsp;

__Example 1:__

<strong>Input:</strong> n = 1
    <strong>Output:</strong> 5
    <strong>Explanation:</strong> The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

__Example 2:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 15
<strong>Explanation:</strong> The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 33
<strong>Output:</strong> 66045
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 50 ``&nbsp;