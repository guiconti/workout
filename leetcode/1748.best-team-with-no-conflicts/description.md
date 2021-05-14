You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the __sum__ of scores of all the players in the team.

However, the basketball team is not allowed to have __conflicts__. A __conflict__ exists if a younger player has a __strictly higher__ score than an older player. A conflict does __not__ occur between players of the same age.

Given two lists, `` scores `` and `` ages ``, where each `` scores[i] `` and `` ages[i] `` represents the score and age of the <code>i<sup>th</sup></code> player, respectively, return _the highest overall score of all possible basketball teams_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> scores = [1,3,5,10,15], ages = [1,2,3,4,5]
<strong>Output:</strong> 34
<strong>Explanation:</strong>&nbsp;You can choose all the players.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> scores = [4,5,6,5], ages = [2,1,2,1]
<strong>Output:</strong> 16
<strong>Explanation:</strong>&nbsp;It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> scores = [1,2,3,5], ages = [8,9,10,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong>&nbsp;It is best to choose the first 3 players. 
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= scores.length, ages.length &lt;= 1000 ``
*   `` scores.length == ages.length ``
*   <code>1 &lt;= scores[i] &lt;= 10<sup>6</sup></code>
*   `` 1 &lt;= ages[i] &lt;= 1000 ``