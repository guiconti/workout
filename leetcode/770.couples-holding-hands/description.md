N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A _swap_ consists of choosing __any__ two people, then they stand up and switch seats. 

The people and seats are represented by an integer from `` 0 `` to `` 2N-1 ``, the couples are numbered in order, the first couple being `` (0, 1) ``, the second couple being `` (2, 3) ``, and so on with the last couple being `` (2N-2, 2N-1) ``.

The couples' initial seating is given by `` row[i] `` being the value of the person who is initially sitting in the i-th seat.

__Example 1:__  

<pre>
<b>Input:</b> row = [0, 2, 1, 3]
<b>Output:</b> 1
<b>Explanation:</b> We only need to swap the second (row[1]) and third (row[2]) person.
</pre>

__Example 2:__  

<pre>
<b>Input:</b> row = [3, 2, 0, 1]
<b>Output:</b> 0
<b>Explanation:</b> All couples are already seated side by side.
</pre>

__Note:__

1.    `` len(row) `` is even and in the range of `` [4, 60] ``.
2.    `` row `` is guaranteed to be a permutation of `` 0...len(row)-1 ``.