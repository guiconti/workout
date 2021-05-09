A query word matches a given `` pattern `` if we can insert __lowercase__ letters to the pattern word so that it equals the `` query ``. (We may insert each character at any position, and may insert 0 characters.)

Given a list of `` queries ``, and a `` pattern ``, return an `` answer `` list of booleans, where `` answer[i] `` is true if and only if `` queries[i] `` matches the `` pattern ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>queries = <span id="example-input-1-1">["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]</span>, pattern = <span id="example-input-1-2">"FB"</span>
<strong>Output: </strong><span id="example-output-1">[true,false,true,true,false]</span>
<strong>Explanation: </strong>
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".</pre>

__Example 2:__

<pre>
<strong>Input: </strong>queries = <span id="example-input-2-1">["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]</span>, pattern = <span id="example-input-2-2">"FoBa"</span>
<strong>Output: </strong><span id="example-output-2">[true,false,true,false,false]</span>
<strong>Explanation: </strong>
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
</pre>

__Example 3:__

<pre>
<strong>Input: </strong>queries = <span id="example-input-3-1">["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]</span>, pattern = <span id="example-input-3-2">"FoBaT"</span>
<strong>Output: </strong><span id="example-output-3">[false,true,false,false,false]</span>
<strong>Explanation: </strong>
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= queries.length &lt;= 100 ``
2.   `` 1 &lt;= queries[i].length &lt;= 100 ``
3.   `` 1 &lt;= pattern.length &lt;= 100 ``
4.   All strings consists only of lower and upper case English letters.