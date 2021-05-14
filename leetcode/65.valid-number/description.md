A __valid number__ can be split up into these components (in order):

1.   A __decimal number__ or an __integer__.
2.   (Optional) An `` 'e' `` or `` 'E' ``, followed by an __integer__.

A __decimal number__ can be split up into these components (in order):

1.   (Optional) A sign character (either `` '+' `` or `` '-' ``).
2.   One of the following formats:	
    
    1.   At least one digit, followed by a dot `` '.' ``.
    2.   At least one digit, followed by a dot `` '.' ``, followed by at least one digit.
    3.   A dot `` '.' ``, followed by at least one digit.
    
    
    

An __integer__ can be split up into these components (in order):

1.   (Optional) A sign character (either `` '+' `` or `` '-' ``).
2.   At least one digit.

For example, all the following are valid numbers: `` ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"] ``, while the following are not valid numbers: `` ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"] ``.

Given a string `` s ``, return `` true ``_ if _`` s ``_ is a __valid number___.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "0"
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "e"
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "."
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = ".1"
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 20 ``
*   `` s `` consists of only English letters (both uppercase and lowercase), digits (`` 0-9 ``), plus `` '+' ``, minus `` '-' ``, or dot `` '.' ``.