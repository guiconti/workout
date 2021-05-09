In a special ranking system,&nbsp;each voter gives a rank from highest to lowest to all teams participated in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

Given an array of strings `` votes `` which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return _a string of all teams_ __sorted__ by the ranking system.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> votes = ["ABC","ACB","ABC","ACB","ACB"]
<strong>Output:</strong> "ACB"
<strong>Explanation:</strong> Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and was ranked third by 3 voters.
Team C was ranked second by 3 voters and was ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team and team B is the third.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> votes = ["WXYZ","XYZW"]
<strong>Output:</strong> "XWYZ"
<strong>Explanation:</strong> X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position. 
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
<strong>Output:</strong> "ZMNAGUEDSJYLBOPHRQICWFXTVK"
<strong>Explanation:</strong> Only one voter so his votes are used for the ranking.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
<strong>Output:</strong> "ABC"
<strong>Explanation:</strong> 
Team A was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team B was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team C was ranked first by 2 voters, second by 2 voters and third by 2 voters.
There is a tie and we rank teams ascending by their IDs.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> votes = ["M","M","M","M"]
<strong>Output:</strong> "M"
<strong>Explanation:</strong> Only team M in the competition so it has the first rank.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= votes.length &lt;= 1000 ``
*   `` 1 &lt;= votes[i].length &lt;= 26 ``
*   `` votes[i].length ==&nbsp;votes[j].length `` for&nbsp;`` 0 &lt;= i, j &lt; votes.length ``.
*   `` votes[i][j] `` is an English __upper-case__ letter.
*   All characters of `` votes[i] `` are unique.
*   All the characters&nbsp;that occur&nbsp;in `` votes[0] `` __also&nbsp;occur__&nbsp;in `` votes[j] `` where `` 1 &lt;= j &lt; votes.length ``.