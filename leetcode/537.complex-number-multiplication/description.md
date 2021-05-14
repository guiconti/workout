A <a href="https://en.wikipedia.org/wiki/Complex_number" target="_blank">complex number</a> can be represented as a string on the form <code>"<strong>real</strong>+<strong>imaginary</strong>i"</code> where:

*   `` real `` is the real part and is an integer in the range `` [-100, 100] ``.
*   `` imaginary `` is the imaginary part and is an integer in the range `` [-100, 100] ``.
*   <code>i<sup>2</sup> == -1</code>.

Given two complex numbers `` num1 `` and `` num2 `` as strings, return _a string of the complex number that represents their multiplications_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num1 = "1+1i", num2 = "1+1i"
<strong>Output:</strong> "0+2i"
<strong>Explanation:</strong> (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num1 = "1+-1i", num2 = "1+-1i"
<strong>Output:</strong> "0+-2i"
<strong>Explanation:</strong> (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
</pre>

&nbsp;

__Constraints:__

*   `` num1 `` and `` num2 `` are valid complex numbers.