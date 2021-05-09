Given a number&nbsp;`` s `` in their binary representation. Return the number of steps to reduce it to 1 under the following rules:

*   
    
    If the current number is even, you have to divide it by 2.
    
    
*   
    
    If the current number is odd, you have to add 1 to it.
    
    

It's guaranteed that you can always reach to one for all testcases.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "1101"
<strong>Output:</strong> 6
<strong>Explanation:</strong> "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14.&nbsp;
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.&nbsp; 
Step 5) 4 is even, divide by 2 and obtain 2.&nbsp;
Step 6) 2 is even, divide by 2 and obtain 1.&nbsp; 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "10"
<strong>Output:</strong> 1
<strong>Explanation:</strong> "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.&nbsp; 
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "1"
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length&nbsp;&lt;= 500 ``
*   `` s `` consists of characters '0' or '1'
*   `` s[0] == '1' ``