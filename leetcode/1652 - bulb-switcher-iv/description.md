There is a room with `` n `` bulbs, numbered from `` 0 `` to `` n - 1 ``, arranged in a row from left to right. Initially, all the bulbs are __turned off__.

Your task is to obtain the configuration represented by `` target `` where `` target[i] `` is `` '1' `` if the <code>i<sup>th</sup></code> bulb is turned on and is `` '0' `` if it is turned off.

You have a switch to flip the state of the bulb, a flip operation is defined as follows:

*   Choose __any__ bulb (index `` i ``) of your current configuration.
*   Flip each bulb from index `` i `` to index `` n - 1 ``.

When any bulb is flipped it means that if it is `` '0' `` it changes to `` '1' `` and if it is `` '1' `` it changes to `` '0' ``.

Return _the __minimum__ number of flips required to form_ `` target ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> target = "10111"
<strong>Output:</strong> 3
<strong>Explanation: </strong>Initial configuration "00000".
flip from the third bulb:  "00000" -&gt; "00111"
flip from the first bulb:  "00111" -&gt; "11000"
flip from the second bulb:  "11000" -&gt; "10111"
We need at least 3 flip operations to form target.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> target = "101"
<strong>Output:</strong> 3
<strong>Explanation: </strong>"000" -&gt; "111" -&gt; "100" -&gt; "101".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> target = "00000"
<strong>Output:</strong> 0
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> target = "001011101"
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= target.length &lt;= 10<sup>5</sup></code>
*   `` target[i] `` is either `` '0' `` or `` '1' ``.