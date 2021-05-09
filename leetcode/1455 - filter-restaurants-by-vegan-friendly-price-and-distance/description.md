Given the array `` restaurants `` where &nbsp;<code>restaurants[i] = [id<sub>i</sub>, rating<sub>i</sub>, veganFriendly<sub>i</sub>, price<sub>i</sub>, distance<sub>i</sub>]</code>. You have to filter the restaurants using three filters.

The `` veganFriendly `` filter will be either _true_ (meaning you should only include restaurants with <code>veganFriendly<sub>i</sub></code> set to true)&nbsp;or _false_&nbsp;(meaning you can include any restaurant). In addition, you have the filters&nbsp;`` maxPrice `` and `` maxDistance ``&nbsp;which&nbsp;are the maximum value for price and distance of restaurants you should consider respectively.

Return the array of restaurant ___IDs___ after filtering, ordered by __rating__ from highest to lowest. For restaurants with the same rating, order them by ___id___ from highest to lowest. For simplicity <code>veganFriendly<sub>i</sub></code> and `` veganFriendly `` take value _1_ when it is _true_, and _0_ when it is _false_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
<strong>Output:</strong> [3,1,5] 
<strong>Explanation: 
</strong>The restaurants are:
Restaurant 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
Restaurant 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
Restaurant 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
Restaurant 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
Restaurant 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1] 
After filter restaurants with veganFriendly = 1, maxPrice = 50 and maxDistance = 10 we have restaurant 3, restaurant 1 and restaurant 5 (ordered by rating from highest to lowest). 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10
<strong>Output:</strong> [4,3,2,1,5]
<strong>Explanation:</strong> The restaurants are the same as in example 1, but in this case the filter veganFriendly = 0, therefore all restaurants are considered.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3
<strong>Output:</strong> [4,5]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;=&nbsp;restaurants.length &lt;= 10^4 ``
*   `` restaurants[i].length == 5 ``
*   <code>1 &lt;=&nbsp;id<sub>i</sub>, rating<sub>i</sub>, price<sub>i</sub>, distance<sub>i </sub>&lt;= 10^5</code>
*   `` 1 &lt;=&nbsp;maxPrice,&nbsp;maxDistance &lt;= 10^5 ``
*   <code>veganFriendly<sub>i</sub></code> and&nbsp;`` veganFriendly ``&nbsp;are&nbsp;0 or 1.
*   All <code>id<sub>i</sub></code> are distinct.