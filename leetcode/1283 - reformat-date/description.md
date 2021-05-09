Given a `` date `` string in the form&nbsp;`` Day Month Year ``, where:

*   `` Day ``&nbsp;is in the set `` {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"} ``.
*   `` Month ``&nbsp;is in the set `` {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"} ``.
*   `` Year ``&nbsp;is in the range `` [1900, 2100] ``.

Convert the date string to the format `` YYYY-MM-DD ``, where:

*   `` YYYY `` denotes the 4 digit year.
*   `` MM `` denotes the 2 digit month.
*   `` DD `` denotes the 2 digit day.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> date = "20th Oct 2052"
<strong>Output:</strong> "2052-10-20"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> date = "6th Jun 1933"
<strong>Output:</strong> "1933-06-06"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> date = "26th May 1960"
<strong>Output:</strong> "1960-05-26"
</pre>

&nbsp;

__Constraints:__

*   The given dates are guaranteed to be valid, so no error handling is necessary.