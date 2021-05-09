Given an integer `` n ``, your task is to count how many strings of length `` n `` can be formed under the following rules:

*   Each character is a lower case vowel&nbsp;(`` 'a' ``, `` 'e' ``, `` 'i' ``, `` 'o' ``, `` 'u' ``)
*   Each vowel&nbsp;`` 'a' `` may only be followed by an `` 'e' ``.
*   Each vowel&nbsp;`` 'e' `` may only be followed by an `` 'a' ``&nbsp;or an `` 'i' ``.
*   Each vowel&nbsp;`` 'i' `` __may not__ be followed by another `` 'i' ``.
*   Each vowel&nbsp;`` 'o' `` may only be followed by an `` 'i' `` or a&nbsp;`` 'u' ``.
*   Each vowel&nbsp;`` 'u' `` may only be followed by an `` 'a'. ``

Since the answer&nbsp;may be too large,&nbsp;return it modulo `` 10^9 + 7. ``

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> All possible strings are: "a", "e", "i" , "o" and "u".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 10
<strong>Explanation:</strong> All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
</pre>

__Example 3:&nbsp;__

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 68</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 2 * 10^4 ``