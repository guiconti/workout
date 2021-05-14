There is a donuts shop that bakes donuts in batches of `` batchSize ``. They have a rule where they must serve __all__ of the donuts of a batch before serving any donuts of the next batch. You are given an integer `` batchSize `` and an integer array `` groups ``, where `` groups[i] `` denotes that there is a group of `` groups[i] `` customers that will visit the shop. Each customer will get exactly one donut.

When a group visits the shop, all customers of the group must be served before serving any of the following groups. A group will be happy if they all get fresh donuts. That is, the first customer of the group does not receive a donut that was left over from the previous group.

You can freely rearrange the ordering of the groups. Return _the __maximum__ possible number of happy groups after rearranging the groups._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> batchSize = 3, groups = [1,2,3,4,5,6]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can arrange the groups as [6,2,4,5,1,3]. Then the 1<sup>st</sup>, 2<sup>nd</sup>, 4<sup>th</sup>, and 6<sup>th</sup> groups will be happy.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> batchSize = 4, groups = [1,3,2,5,2,2,1,6]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= batchSize &lt;= 9 ``
*   `` 1 &lt;= groups.length &lt;= 30 ``
*   <code>1 &lt;= groups[i] &lt;= 10<sup>9</sup></code>