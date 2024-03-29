Your car starts at position 0 and speed +1 on an infinite number line.&nbsp; (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following:&nbsp;`` position += speed, speed *= 2 ``.

When you get an instruction "R", your car does the following: if your speed is positive then&nbsp;`` speed = -1 ``&nbsp;, otherwise&nbsp;`` speed = 1 ``.&nbsp; (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0-&gt;1-&gt;3-&gt;3, and your speed goes to 1-&gt;2-&gt;4-&gt;-1.

Now for some target position, say the __length__ of the shortest sequence of instructions to get there.

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> 
target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The shortest instruction sequence is "AA".
Your position goes from 0-&gt;1-&gt;3.
</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> 
target = 6
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
The shortest instruction sequence is "AAARA".
Your position goes from 0-&gt;1-&gt;3-&gt;7-&gt;7-&gt;6.
</pre>

&nbsp;

__Note: __

*   `` 1 &lt;= target &lt;= 10000 ``.