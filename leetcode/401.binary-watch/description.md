A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

*   For example, the below binary watch reads `` "4:51" ``.

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/binarywatch.jpg" style="width: 500px; height: 500px;"/>

Given an integer `` turnedOn `` which represents the number of LEDs that are currently on, return _all possible times the watch could represent_. You may return the answer in __any order__.

The hour must not contain a leading zero.

*   For example, `` "01:00" `` is not valid. It should be `` "1:00" ``.

The minute must be consist of two digits and may contain a leading zero.

*   For example, `` "10:2" `` is not valid. It should be `` "10:02" ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> turnedOn = 1
<strong>Output:</strong> ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
</pre>

__Example 2:__

<pre><strong>Input:</strong> turnedOn = 9
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= turnedOn &lt;= 10 ``