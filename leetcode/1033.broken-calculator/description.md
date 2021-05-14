On a broken calculator that has a number showing on its display, we can perform two operations:

*   __Double__: Multiply the number on the display by 2, or;
*   __Decrement__: Subtract 1 from the number on the display.

Initially, the calculator is displaying the number `` X ``.

Return the minimum number of operations needed to display the number `` Y ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>X = <span id="example-input-1-1">2</span>, Y = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>Use double operation and then decrement operation {2 -&gt; 4 -&gt; 3}.
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>X = <span id="example-input-2-1">5</span>, Y = <span id="example-input-2-2">8</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<strong>Explanation: </strong>Use decrement and then double {5 -&gt; 4 -&gt; 8}.
</pre>

__Example 3:__

<pre>
<strong>Input: </strong>X = <span id="example-input-3-1">3</span>, Y = <span id="example-input-3-2">10</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation: </strong> Use double, decrement and double {3 -&gt; 6 -&gt; 5 -&gt; 10}.
</pre>

__Example 4:__

<pre>
<strong>Input: </strong>X = <span id="example-input-4-1">1024</span>, Y = <span id="example-input-4-2">1</span>
<strong>Output: </strong><span id="example-output-4">1023</span>
<strong>Explanation: </strong>Use decrement operations 1023 times.
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= X &lt;= 10^9 ``
2.   `` 1 &lt;= Y &lt;= 10^9 ``