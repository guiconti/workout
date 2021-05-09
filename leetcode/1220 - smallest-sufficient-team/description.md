In a project, you have a list of required skills `` req_skills ``, and a list of people. The <code>i<sup>th</sup></code> person `` people[i] `` contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in `` req_skills ``, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

*   For example, `` team = [0, 1, 3] `` represents the people with skills `` people[0] ``, `` people[1] ``, and `` people[3] ``.

Return _any sufficient team of the smallest possible size, represented by the index of each person_. You may return the answer in __any order__.

It is __guaranteed__ an answer exists.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
<strong>Output:</strong> [0,2]
</pre>

__Example 2:__

<pre><strong>Input:</strong> req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
<strong>Output:</strong> [1,2]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= req_skills.length &lt;= 16 ``
*   `` 1 &lt;= req_skills[i].length &lt;= 16 ``
*   `` req_skills[i] `` consists of lowercase English letters.
*   All the strings of `` req_skills `` are __unique__.
*   `` 1 &lt;= people.length &lt;= 60 ``
*   `` 0 &lt;= people[i].length &lt;= 16 ``
*   `` 1 &lt;= people[i][j].length &lt;= 16 ``
*   `` people[i][j] `` consists of lowercase English letters.
*   All the strings of `` people[i] `` are __unique__.
*   Every skill in `` people[i] `` is a skill in `` req_skills ``.
*   It is guaranteed a sufficient team exists.