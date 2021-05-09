You are given a string `` num ``, representing a large integer, and an integer `` k ``.

We call some integer __wonderful__ if it is a __permutation__ of the digits in `` num `` and is __greater in value__ than `` num ``. There can be many wonderful integers. However, we only care about the __smallest-valued__ ones.

*   For example, when `` num = "5489355142" ``:	
    
    *   The 1<sup>st</sup> smallest wonderful integer is `` "5489355214" ``.
    *   The 2<sup>nd</sup> smallest wonderful integer is `` "5489355241" ``.
    *   The 3<sup>rd</sup> smallest wonderful integer is `` "5489355412" ``.
    *   The 4<sup>th</sup> smallest wonderful integer is `` "5489355421" ``.
    
    
    

Return _the __minimum number of adjacent digit swaps__ that needs to be applied to _`` num ``_ to reach the _<code>k<sup>th</sup></code>___ smallest wonderful__ integer_.

The tests are generated in such a way that <code>k<sup>th</sup></code>&nbsp;smallest wonderful integer exists.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = "5489355142", k = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The 4<sup>th</sup> smallest wonderful number is "5489355421". To get this number:
- Swap index 7 with index 8: "5489355<u>14</u>2" -&gt; "5489355<u>41</u>2"
- Swap index 8 with index 9: "54893554<u>12</u>" -&gt; "54893554<u>21</u>"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = "11112", k = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong> The 4<sup>th</sup> smallest wonderful number is "21111". To get this number:
- Swap index 3 with index 4: "111<u>12</u>" -&gt; "111<u>21</u>"
- Swap index 2 with index 3: "11<u>12</u>1" -&gt; "11<u>21</u>1"
- Swap index 1 with index 2: "1<u>12</u>11" -&gt; "1<u>21</u>11"
- Swap index 0 with index 1: "<u>12</u>111" -&gt; "<u>21</u>111"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> num = "00123", k = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The 1<sup>st</sup> smallest wonderful number is "00132". To get this number:
- Swap index 3 with index 4: "001<u>23</u>" -&gt; "001<u>32</u>"
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= num.length &lt;= 1000 ``
*   `` 1 &lt;= k &lt;= 1000 ``
*   `` num `` only consists of digits.