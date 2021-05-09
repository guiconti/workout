You are given a string `` word `` that consists of digits and lowercase English letters.

You will replace every non-digit character with a space. For example, `` "a123bc34d8ef34" `` will become `` " 123&nbsp; 34 8&nbsp; 34" ``. Notice that you are left with some integers that are separated by at least one space: `` "123" ``, `` "34" ``, `` "8" ``, and `` "34" ``.

Return _the number of __different__ integers after performing the replacement operations on _`` word ``.

Two integers are considered different if their decimal representations __without any leading zeros__ are different.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> word = "a<u>123</u>bc<u>34</u>d<u>8</u>ef<u>34</u>"
<strong>Output:</strong> 3
<strong>Explanation: </strong>The three different integers are "123", "34", and "8". Notice that "34" is only counted once.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> word = "leet<u>1234</u>code<u>234</u>"
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> word = "a<u>1</u>b<u>01</u>c<u>001</u>"
<strong>Output:</strong> 1
<strong>Explanation: </strong>The three integers "1", "01", and "001" all represent the same integer because
the leading zeros are ignored when comparing their decimal values.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= word.length &lt;= 1000 ``
*   `` word `` consists of digits and lowercase English letters.