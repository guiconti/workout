Two strings are considered __close__ if you can attain one from the other using the following operations:

*   Operation 1: Swap any two __existing__ characters.	
    
    *   For example, <code>a<u>b</u>cd<u>e</u> -&gt; a<u>e</u>cd<u>b</u></code>
    
    
    
*   Operation 2: Transform __every__ occurrence of one __existing__ character into another __existing__ character, and do the same with the other character.	
    
    *   For example, <code><u>aa</u>c<u>abb</u> -&gt; <u>bb</u>c<u>baa</u></code> (all `` a ``'s turn into `` b ``'s, and all `` b ``'s turn into `` a ``'s)
    
    
    

You can use the operations on either string as many times as necessary.

Given two strings, `` word1 `` and `` word2 ``, return `` true ``_ if _`` word1 ``_ and _`` word2 ``_ are __close__, and _`` false ``_ otherwise._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> word1 = "abc", word2 = "bca"
<strong>Output:</strong> true
<strong>Explanation:</strong> You can attain word2 from word1 in 2 operations.
Apply Operation 1: "a<u>bc</u>" -&gt; "a<u>cb</u>"
Apply Operation 1: "<u>a</u>c<u>b</u>" -&gt; "<u>b</u>c<u>a</u>"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> word1 = "a", word2 = "aa"
<strong>Output:</strong> false
<strong>Explanation: </strong>It is impossible to attain word2 from word1, or vice versa, in any number of operations.
</pre>

__Example 3:__

<strong>Input:</strong> word1 = "cabbba", word2 = "abbccc"
    <strong>Output:</strong> true
    <strong>Explanation:</strong> You can attain word2 from word1 in 3 operations.
    Apply Operation 1: "ca<u>b</u>bb<u>a</u>" -&gt; "ca<u>a</u>bb<u>b</u>"
    Apply Operation 2: "<u>c</u>aa<u>bbb</u>" -&gt; "<u>b</u>aa<u>ccc</u>"
    Apply Operation 2: "<u>baa</u>ccc" -&gt; "<u>abb</u>ccc"

__Example 4:__

<pre>
<strong>Input:</strong> word1 = "cabbba", word2 = "aabbss"
<strong>Output:</strong> false
<strong>Explanation: </strong>It is impossible to attain word2 from word1, or vice versa, in any amount of operations.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= word1.length, word2.length &lt;= 10<sup>5</sup></code>
*   `` word1 `` and `` word2 `` contain&nbsp;only lowercase English letters.