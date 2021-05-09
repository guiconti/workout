Given an array&nbsp;`` arr `` of 4 digits, find the latest 24-hour time that can be made using each digit __exactly once__.

24-hour times are formatted as `` "HH:MM" ``, where `` HH ``&nbsp;is between&nbsp;`` 00 ``&nbsp;and&nbsp;`` 23 ``, and&nbsp;`` MM ``&nbsp;is between&nbsp;`` 00 ``&nbsp;and&nbsp;`` 59 ``. The earliest 24-hour time is `` 00:00 ``, and the latest is `` 23:59 ``.

Return _the latest 24-hour time&nbsp;in&nbsp;`` "HH:MM" `` format_.&nbsp; If no valid time can be made, return an empty string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,2,3,4]
<strong>Output:</strong> "23:41"
<strong>Explanation:</strong>&nbsp;The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [5,5,5,5]
<strong>Output:</strong> ""
<strong>Explanation:</strong>&nbsp;There are no valid 24-hour times as "55:55" is not valid.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [0,0,0,0]
<strong>Output:</strong> "00:00"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [0,0,1,0]
<strong>Output:</strong> "10:00"
</pre>

&nbsp;

__Constraints:__

*   `` arr.length == 4 ``
*   `` 0 &lt;= arr[i] &lt;= 9 ``