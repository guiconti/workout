The power of an integer `` x `` is defined as the number of steps needed to transform&nbsp;`` x `` into `` 1 `` using the following steps:

*   if `` x `` is even then `` x = x / 2 ``
*   if `` x `` is odd then `` x = 3 * x + 1 ``

For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --&gt; 10 --&gt; 5 --&gt; 16 --&gt; 8 --&gt; 4 --&gt; 2 --&gt; 1).

Given three integers `` lo ``, `` hi `` and `` k ``. The task is to sort all integers in the interval `` [lo, hi] `` by the power value in __ascending order__, if two or more integers have __the same__ power value sort them by __ascending order__.

Return the `` k-th `` integer in the range `` [lo, hi] `` sorted by the power value.

Notice that for any&nbsp;integer `` x `` `` (lo &lt;= x &lt;= hi) `` it is __guaranteed__ that `` x `` will transform into `` 1 `` using these steps and that the power of `` x `` is will __fit__ in 32 bit signed integer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> lo = 12, hi = 15, k = 2
<strong>Output:</strong> 13
<strong>Explanation:</strong> The power of 12 is 9 (12 --&gt; 6 --&gt; 3 --&gt; 10 --&gt; 5 --&gt; 16 --&gt; 8 --&gt; 4 --&gt; 2 --&gt; 1)
The power of 13 is 9
The power of 14 is 17
The power of 15 is 17
The interval sorted by the power value [12,13,14,15]. For k = 2 answer is the second element which is 13.
Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> lo = 1, hi = 1, k = 1
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> lo = 7, hi = 11, k = 4
<strong>Output:</strong> 7
<strong>Explanation:</strong> The power array corresponding to the interval [7, 8, 9, 10, 11] is [16, 3, 19, 6, 14].
The interval sorted by power is [8, 10, 11, 7, 9].
The fourth number in the sorted array is 7.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> lo = 10, hi = 20, k = 5
<strong>Output:</strong> 13
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> lo = 1, hi = 1000, k = 777
<strong>Output:</strong> 570
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= lo &lt;= hi &lt;= 1000 ``
*   `` 1 &lt;= k &lt;= hi - lo + 1 ``