Given a string `` date `` representing a <a href="https://en.wikipedia.org/wiki/Gregorian_calendar" target="_blank">Gregorian calendar</a> date formatted as `` YYYY-MM-DD ``, return the day number of the year.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> date = "2019-01-09"
<strong>Output:</strong> 9
<strong>Explanation:</strong> Given date is the 9th day of the year in 2019.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> date = "2019-02-10"
<strong>Output:</strong> 41
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> date = "2003-03-01"
<strong>Output:</strong> 60
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> date = "2004-03-01"
<strong>Output:</strong> 61
</pre>

&nbsp;

__Constraints:__

*   `` date.length == 10 ``
*   `` date[4] == date[7] == '-' ``, and all other `` date[i] ``'s are digits
*   `` date `` represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.