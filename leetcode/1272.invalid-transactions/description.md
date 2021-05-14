A transaction is possibly invalid if:

*   the amount exceeds `` $1000 ``, or;
*   if it occurs within (and including) `` 60 `` minutes of another transaction with the __same name__ in a __different city__.

You are given an array of strings `` transaction `` where `` transactions[i] `` consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of `` transactions `` that are possibly invalid. You may return the answer in __any order__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
<strong>Output:</strong> ["alice,20,800,mtv","alice,50,100,beijing"]
<strong>Explanation:</strong> The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
<strong>Output:</strong> ["alice,50,1200,mtv"]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
<strong>Output:</strong> ["bob,50,1200,mtv"]
</pre>

&nbsp;

__Constraints:__

*   `` transactions.length &lt;= 1000 ``
*   Each `` transactions[i] `` takes the form `` "{name},{time},{amount},{city}" ``
*   Each `` {name} `` and `` {city} `` consist of lowercase English letters, and have lengths between `` 1 `` and `` 10 ``.
*   Each `` {time} `` consist of digits, and represent an integer between `` 0 `` and `` 1000 ``.
*   Each `` {amount} `` consist of digits, and represent an integer between `` 0 `` and `` 2000 ``.