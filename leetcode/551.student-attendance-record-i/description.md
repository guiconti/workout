You are given a string `` s `` representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

*   `` 'A' ``: Absent.
*   `` 'L' ``: Late.
*   `` 'P' ``: Present.

The student is eligible for an attendance award if they meet __both__ of the following criteria:

*   The student was absent (`` 'A' ``) for __strictly__ fewer than 2 days __total__.
*   The student was __never__ late (`` 'L' ``) for 3 or more __consecutive__ days.

Return `` true ``_ if the student is eligible for an attendance award, or _`` false ``_ otherwise_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "PPALLP"
<strong>Output:</strong> true
<strong>Explanation:</strong> The student has fewer than 2 absences and was never late 3 or more consecutive days.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "PPALLL"
<strong>Output:</strong> false
<strong>Explanation:</strong> The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 1000 ``
*   `` s[i] `` is either `` 'A' ``, `` 'L' ``, or `` 'P' ``.