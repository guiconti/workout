You are given an integer array `` score `` of size `` n ``, where `` score[i] `` is the score of the <code>i<sup>th</sup></code> athlete in a competition. All the scores are guaranteed to be __unique__.

The athletes are __placed__ based on their scores, where the <code>1<sup>st</sup></code> place athlete has the highest score, the <code>2<sup>nd</sup></code> place athlete has the <code>2<sup>nd</sup></code> highest score, and so on. The placement of each athlete determines their rank:

*   The <code>1<sup>st</sup></code> place athlete's rank is `` "Gold Medal" ``.
*   The <code>2<sup>nd</sup></code> place athlete's rank is `` "Silver Medal" ``.
*   The <code>3<sup>rd</sup></code> place athlete's rank is `` "Bronze Medal" ``.
*   For the <code>4<sup>th</sup></code> place to the <code>n<sup>th</sup></code> place athlete, their rank is their placement number (i.e., the <code>x<sup>th</sup></code> place athlete's rank is `` "x" ``).

Return an array `` answer `` of size `` n `` where `` answer[i] `` is the __rank__ of the <code>i<sup>th</sup></code> athlete.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> score = [5,4,3,2,1]
<strong>Output:</strong> ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
<strong>Explanation:</strong> The placements are [1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup>, 4<sup>th</sup>, 5<sup>th</sup>].</pre>

__Example 2:__

<pre>
<strong>Input:</strong> score = [10,3,8,9,4]
<strong>Output:</strong> ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
<strong>Explanation:</strong> The placements are [1<sup>st</sup>, 5<sup>th</sup>, 3<sup>rd</sup>, 2<sup>nd</sup>, 4<sup>th</sup>].

</pre>

&nbsp;

__Constraints:__

*   `` n == score.length ``
*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= score[i] &lt;= 10<sup>6</sup></code>
*   All the values in `` score `` are __unique__.