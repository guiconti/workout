On the first row, we write a `` 0 ``. Now in every subsequent row, we look at the previous row and replace each occurrence of `` 0 `` with `` 01 ``, and each occurrence of `` 1 `` with `` 10 ``.

Given row `` N `` and index `` K ``, return the `` K ``-th indexed symbol in row `` N ``. (The values of `` K `` are 1-indexed.) (1 indexed).

<pre>
<strong>Examples:</strong>
<strong>Input:</strong> N = 1, K = 1
<strong>Output:</strong> 0

<strong>Input:</strong> N = 2, K = 1
<strong>Output:</strong> 0

<strong>Input:</strong> N = 2, K = 2
<strong>Output:</strong> 1

<strong>Input:</strong> N = 4, K = 5
<strong>Output:</strong> 1

<strong>Explanation:</strong>
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
</pre>

__Note:__

1.   `` N `` will be an integer in the range `` [1, 30] ``.
2.   `` K `` will be an integer in the range `` [1, 2^(N-1)] ``.