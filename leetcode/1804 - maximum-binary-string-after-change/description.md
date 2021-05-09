You are given a binary string `` binary `` consisting of only `` 0 ``'s or `` 1 ``'s. You can apply each of the following operations any number of times:

*   Operation 1: If the number contains the substring `` "00" ``, you can replace it with `` "10" ``.	
    
    *   For example, <code>"<u>00</u>010" -&gt; "<u>10</u>010</code>"
    
    
    
*   Operation 2: If the number contains the substring `` "10" ``, you can replace it with `` "01" ``.	
    
    *   For example, <code>"000<u>10</u>" -&gt; "000<u>01</u>"</code>
    
    
    

_Return the __maximum binary string__ you can obtain after any number of operations. Binary string `` x `` is greater than binary string `` y `` if `` x ``'s decimal representation is greater than `` y ``'s decimal representation._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> binary = "000110"
<strong>Output:</strong> "111011"
<strong>Explanation:</strong> A valid transformation sequence can be:
"0001<u>10</u>" -&gt; "0001<u>01</u>" 
"<u>00</u>0101" -&gt; "<u>10</u>0101" 
"1<u>00</u>101" -&gt; "1<u>10</u>101" 
"110<u>10</u>1" -&gt; "110<u>01</u>1" 
"11<u>00</u>11" -&gt; "11<u>10</u>11"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> binary = "01"
<strong>Output:</strong> "01"
<strong>Explanation:</strong>&nbsp;"01" cannot be transformed any further.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= binary.length &lt;= 10<sup>5</sup></code>
*   `` binary `` consist of `` '0' `` and `` '1' ``.