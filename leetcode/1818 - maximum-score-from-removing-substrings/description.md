You are given a string `` s `` and two integers `` x `` and `` y ``. You can perform two types of operations any number of times.

*   Remove substring `` "ab" `` and gain `` x `` points.	
    
    *   For example, when removing `` "ab" `` from <code>"c<u>ab</u>xbae"</code> it becomes `` "cxbae" ``.
    
    
    
*   Remove substring `` "ba" `` and gain `` y `` points.	
    
    *   For example, when removing `` "ba" `` from <code>"cabx<u>ba</u>e"</code> it becomes `` "cabxe" ``.
    
    
    

Return _the maximum points you can gain after applying the above operations on_ `` s ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "cdbcbbaaabab", x = 4, y = 5
<strong>Output:</strong> 19
<strong>Explanation:</strong>
- Remove the "ba" underlined in "cdbcbbaaa<u>ba</u>b". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaa<u>ab</u>". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcb<u>ba</u>a". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbc<u>ba</u>". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aabbaaxybbaabb", x = 5, y = 4
<strong>Output:</strong> 20
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= x, y &lt;= 10<sup>4</sup></code>
*   `` s `` consists of lowercase English letters.