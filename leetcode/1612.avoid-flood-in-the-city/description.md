Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the `` nth `` lake, the `` nth `` lake becomes full of water. If it rains over a lake which is __full of water__, there will be a __flood__. Your goal is to avoid the flood in any lake.

Given an integer array `` rains `` where:

*   `` rains[i] &gt; 0 `` means there will be rains over the `` rains[i] `` lake.
*   `` rains[i] == 0 `` means there are no rains this day and you can choose __one lake__ this day and __dry it__.

Return _an array `` ans ``_ where:

*   `` ans.length == rains.length ``
*   `` ans[i] == -1 `` if `` rains[i] &gt; 0 ``.
*   `` ans[i] `` is the lake you choose to dry in the `` ith `` day&nbsp;if `` rains[i] == 0 ``.

If there are multiple valid answers return __any__ of them. If it is impossible to avoid flood return __an empty array__.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes. (see example 4)

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> rains = [1,2,3,4]
<strong>Output:</strong> [-1,-1,-1,-1]
<strong>Explanation:</strong> After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> rains = [1,2,0,0,2,1]
<strong>Output:</strong> [-1,-1,2,1,-1,-1]
<strong>Explanation:</strong> After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> rains = [1,2,0,1,2]
<strong>Output:</strong> []
<strong>Explanation:</strong> After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> rains = [69,0,0,0,69]
<strong>Output:</strong> [-1,69,1,1,-1]
<strong>Explanation:</strong> Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1] or [-1,x,y,69,-1] is acceptable where 1 &lt;= x,y &lt;= 10^9
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> rains = [10,20,20]
<strong>Output:</strong> []
<strong>Explanation:</strong> It will rain over lake 20 two consecutive days. There is no chance to dry any lake.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= rains.length &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= rains[i] &lt;= 10<sup>9</sup></code>