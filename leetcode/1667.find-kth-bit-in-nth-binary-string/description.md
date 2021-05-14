Given two positive integers&nbsp;`` n ``&nbsp;and `` k ``,&nbsp;the binary string&nbsp;&nbsp;<code>S<sub>n</sub></code>&nbsp;is formed as follows:

*   <code>S<sub>1</sub>&nbsp;= "0"</code>
*   <code>S<sub><span style="font-size: 10.8333px;">i</span></sub>&nbsp;=&nbsp;S<sub><span style="font-size: 10.8333px;">i-1</span></sub>&nbsp;+ "1" + reverse(invert(S<sub><span style="font-size: 10.8333px;">i-1</span></sub>))</code>&nbsp;for&nbsp;`` i &gt; 1 ``

Where&nbsp;`` + ``&nbsp;denotes the concatenation operation,&nbsp;`` reverse(x) ``&nbsp;returns the reversed string 

<font face="monospace">x,</font>

&nbsp;and&nbsp;`` invert(x) ``&nbsp;inverts all the bits in 

<font face="monospace">x</font>

 (0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

*   <code>S<sub>1&nbsp;</sub>= "0"</code>
*   <code>S<sub>2&nbsp;</sub>= "0<strong>1</strong>1"</code>
*   <code>S<sub>3&nbsp;</sub>= "011<strong>1</strong>001"</code>
*   <code>S<sub>4</sub> = "0111001<strong>1</strong>0110001"</code>

Return _the_ <code>k<sup>th</sup></code> _bit_ _in_&nbsp;<code>S<sub>n</sub></code>. It is guaranteed that&nbsp;`` k ``&nbsp;is valid for the given&nbsp;`` n ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> "0"
<strong>Explanation: </strong>S<sub>3</sub>&nbsp;is "<strong><u>0</u></strong>111001". The first bit is "0".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 4, k = 11
<strong>Output:</strong> "1"
<strong>Explanation: </strong>S<sub>4</sub>&nbsp;is "0111001101<strong><u>1</u></strong>0001". The 11th bit is "1".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 1, k = 1
<strong>Output:</strong> "0"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 2, k = 3
<strong>Output:</strong> "1"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 20 ``
*   <code>1 &lt;= k &lt;= 2<sup>n</sup> - 1</code>