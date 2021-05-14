You are given the array `` paths ``, where <code>paths[i] = [cityA<sub>i</sub>, cityB<sub>i</sub>]</code> means there exists a direct path going from <code>cityA<sub>i</sub></code> to <code>cityB<sub>i</sub></code>. _Return the destination city, that is, the city without any path outgoing to another city._

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
<strong>Output:</strong> "Sao Paulo" 
<strong>Explanation:</strong> Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -&gt; "New York" -&gt; "Lima" -&gt; "Sao Paulo".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> paths = [["B","C"],["D","B"],["C","A"]]
<strong>Output:</strong> "A"
<strong>Explanation:</strong> All possible trips are:&nbsp;
"D" -&gt; "B" -&gt; "C" -&gt; "A".&nbsp;
"B" -&gt; "C" -&gt; "A".&nbsp;
"C" -&gt; "A".&nbsp;
"A".&nbsp;
Clearly the destination city is "A".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> paths = [["A","Z"]]
<strong>Output:</strong> "Z"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= paths.length &lt;= 100 ``
*   `` paths[i].length == 2 ``
*   <code>1 &lt;= cityA<sub>i</sub>.length, cityB<sub>i</sub>.length &lt;= 10</code>
*   <code>cityA<sub>i</sub> != cityB<sub>i</sub></code>
*   All strings consist of lowercase and uppercase English letters and the space character.