Given the array `` favoriteCompanies `` where `` favoriteCompanies[i] `` is the list of favorites companies for the `` ith `` person (__indexed from 0__).

_Return the indices of people whose list of favorite companies is not a __subset__ of any other list of favorites companies_. You must return the indices&nbsp;in increasing order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
<strong>Output:</strong> [0,1,4] 
<strong>Explanation:</strong> 
Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
<strong>Output:</strong> [0,1] 
<strong>Explanation:</strong> In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
<strong>Output:</strong> [0,1,2,3]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;=&nbsp;favoriteCompanies.length &lt;= 100 ``
*   `` 1 &lt;=&nbsp;favoriteCompanies[i].length &lt;= 500 ``
*   `` 1 &lt;=&nbsp;favoriteCompanies[i][j].length &lt;= 20 ``
*   All strings in `` favoriteCompanies[i] `` are __distinct__.
*   All lists of favorite companies are __distinct__, that is, If we sort alphabetically each list then `` favoriteCompanies[i] != favoriteCompanies[j]. ``
*   All strings consist of lowercase English letters only.