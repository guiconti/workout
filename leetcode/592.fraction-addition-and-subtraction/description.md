Given a string `` expression `` representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an <a href="https://en.wikipedia.org/wiki/Irreducible_fraction" target="_blank">irreducible fraction</a>. If your final result is an integer, say `` 2 ``, you need to change it to the format of a fraction that has a denominator `` 1 ``. So in this case, `` 2 `` should be converted to `` 2/1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> expression = "-1/2+1/2"
<strong>Output:</strong> "0/1"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> expression = "-1/2+1/2+1/3"
<strong>Output:</strong> "1/3"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> expression = "1/3-1/2"
<strong>Output:</strong> "-1/6"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> expression = "5/3+1/3"
<strong>Output:</strong> "2/1"
</pre>

&nbsp;

__Constraints:__

*   The input string only contains `` '0' `` to `` '9' ``, `` '/' ``, `` '+' `` and `` '-' ``. So does the output.
*   Each fraction (input and output) has the format `` ±numerator/denominator ``. If the first input fraction or the output is positive, then `` '+' `` will be omitted.
*   The input only contains valid __irreducible fractions__, where the __numerator__ and __denominator__ of each fraction will always be in the range `` [1, 10] ``. If the denominator is `` 1 ``, it means this fraction is actually an integer in a fraction format defined above.
*   The number of given fractions will be in the range `` [1, 10] ``.
*   The numerator and denominator of the __final result__ are guaranteed to be valid and in the range of __32-bit__ int.