There are `` n `` children standing in a line. Each child is assigned a rating value given in the integer array `` ratings ``.

You are giving candies to these children subjected to the following requirements:

*   Each child must have at least one candy.
*   Children with a higher rating get more candies than their neighbors.

Return _the minimum number of candies you need to have to distribute the candies to the children_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> ratings = [1,0,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> ratings = [1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
</pre>

&nbsp;

__Constraints:__

*   `` n == ratings.length ``
*   <code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code>
*   <code>0 &lt;= ratings[i] &lt;= 2 * 10<sup>4</sup></code>