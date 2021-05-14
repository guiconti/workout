You are given a string `` time `` in the form of ``  hh:mm ``, where some of the digits in the string are hidden (represented by `` ? ``).

The valid times are those inclusively between `` 00:00 `` and `` 23:59 ``.

Return _the latest valid time you can get from_ `` time ``_ by replacing the hidden_ _digits_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> time = "2?:?0"
<strong>Output:</strong> "23:50"
<strong>Explanation:</strong> The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> time = "0?:3?"
<strong>Output:</strong> "09:39"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> time = "1?:22"
<strong>Output:</strong> "19:22"
</pre>

&nbsp;

__Constraints:__

*   `` time `` is in the format `` hh:mm ``.
*   It is guaranteed that you can produce a valid time from the given string.