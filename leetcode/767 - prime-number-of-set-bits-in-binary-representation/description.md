Given two integers `` L `` and `` R ``, find the count of numbers in the range `` [L, R] `` (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of `` 1 ``s present when written in binary. For example, `` 21 `` written in binary is `` 10101 `` which has 3 set bits. Also, 1 is not a prime.)

__Example 1:__  

<pre>
<b>Input:</b> L = 6, R = 10
<b>Output:</b> 4
<b>Explanation:</b>
6 -&gt; 110 (2 set bits, 2 is prime)
7 -&gt; 111 (3 set bits, 3 is prime)
9 -&gt; 1001 (2 set bits , 2 is prime)
10-&gt;1010 (2 set bits , 2 is prime)
</pre>

__Example 2:__  

<pre>
<b>Input:</b> L = 10, R = 15
<b>Output:</b> 5
<b>Explanation:</b>
10 -&gt; 1010 (2 set bits, 2 is prime)
11 -&gt; 1011 (3 set bits, 3 is prime)
12 -&gt; 1100 (2 set bits, 2 is prime)
13 -&gt; 1101 (3 set bits, 3 is prime)
14 -&gt; 1110 (3 set bits, 3 is prime)
15 -&gt; 1111 (4 set bits, 4 is not prime)
</pre>

__Note:__  

1.   `` L, R `` will be integers `` L &lt;= R `` in the range `` [1, 10^6] ``.
2.   `` R - L `` will be at most 10000.