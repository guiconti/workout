Suppose you have `` n `` integers labeled `` 1 `` through `` n ``. A permutation of those `` n `` integers `` perm `` (__1-indexed__) is considered a __beautiful arrangement__ if for every `` i `` (`` 1 &lt;= i &lt;= n ``), __either__ of the following is true:

*   `` perm[i] `` is divisible by `` i ``.
*   `` i `` is divisible by `` perm[i] ``.

Given an integer `` n ``, return _the __number__ of the __beautiful arrangements__ that you can construct_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<b>Explanation:</b> 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 15 ``