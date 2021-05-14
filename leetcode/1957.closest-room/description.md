There is a hotel with `` n `` rooms. The rooms are represented by a 2D integer array `` rooms `` where <code>rooms[i] = [roomId<sub>i</sub>, size<sub>i</sub>]</code> denotes that there is a room with room number <code>roomId<sub>i</sub></code> and size equal to <code>size<sub>i</sub></code>. Each <code>roomId<sub>i</sub></code> is guaranteed to be __unique__.

You are also given `` k `` queries in a 2D array `` queries `` where <code>queries[j] = [preferred<sub>j</sub>, minSize<sub>j</sub>]</code>. The answer to the <code>j<sup>th</sup></code> query is the room number `` id `` of a room such that:

*   The room has a size of __at least__ <code>minSize<sub>j</sub></code>, and
*   <code>abs(id - preferred<sub>j</sub>)</code> is __minimized__, where `` abs(x) `` is the absolute value of `` x ``.

If there is a __tie__ in the absolute difference, then use the room with the __smallest__ such `` id ``. If there is __no such room__, the answer is `` -1 ``.

Return _an array _`` answer ``_ of length _`` k ``_ where _`` answer[j] ``_ contains the answer to the _<code>j<sup>th</sup></code>_ query_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
<strong>Output:</strong> [3,-1,3]
<strong>Explanation: </strong>The answers to the queries are as follows:
Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
<strong>Output:</strong> [2,1,3]
<strong>Explanation: </strong>The answers to the queries are as follows:
Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size of 3 is at least 3. The answer is 2.
Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
Query = [2,5]: Room number 3 is the only room with a size of at least 5. The answer is 3.</pre>

&nbsp;

__Constraints:__

*   `` n == rooms.length ``
*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   `` k == queries.length ``
*   <code>1 &lt;= k &lt;= 10<sup>4</sup></code>
*   <code>1 &lt;= roomId<sub>i</sub>, preferred<sub>j</sub> &lt;= 10<sup>7</sup></code>
*   <code>1 &lt;= size<sub>i</sub>, minSize<sub>j</sub> &lt;= 10<sup>7</sup></code>
*   &nbsp;