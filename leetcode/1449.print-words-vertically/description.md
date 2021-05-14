Given a string `` s ``.&nbsp;Return&nbsp;all the words vertically in the same order in which they appear in `` s ``.  
Words are returned as a list of strings, complete with&nbsp;spaces when is necessary. (Trailing spaces are not allowed).  
Each word would be put on only one column and that in one column there will be only one word.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "HOW ARE YOU"
<strong>Output:</strong> ["HAY","ORO","WEU"]
<strong>Explanation: </strong>Each word is printed vertically. 
 "HAY"
&nbsp;"ORO"
&nbsp;"WEU"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "TO BE OR NOT TO BE"
<strong>Output:</strong> ["TBONTB","OEROOE","   T"]
<strong>Explanation: </strong>Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "CONTEST IS COMING"
<strong>Output:</strong> ["CIC","OSO","N M","T I","E N","S G","T"]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 200 ``
*   `` s ``&nbsp;contains only upper case English letters.
*   It's guaranteed that there is only one&nbsp;space between 2 words.