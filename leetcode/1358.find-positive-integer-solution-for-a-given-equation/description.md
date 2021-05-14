Given a callable function `` f(x, y) `` __with a hidden formula__ and a value `` z ``, reverse engineer the formula and return _all positive integer pairs _`` x ``_ and _`` y ``_ where _`` f(x,y) == z ``. You may return the pairs in any order.

While the exact formula is hidden, the function is monotonically increasing, i.e.:

*   `` f(x, y) &lt; f(x + 1, y) ``
*   `` f(x, y) &lt; f(x, y + 1) ``

The function interface is defined like this:

<pre>
interface CustomFunction {
public:
  // Returns some positive integer f(x, y) for two positive integers x and y based on a formula.
  int f(int x, int y);
};
</pre>

We will judge your solution as follows:

*   The judge has a list of `` 9 `` hidden implementations of `` CustomFunction ``, along with a way to generate an __answer key__ of all valid pairs for a specific `` z ``.
*   The judge will receive two inputs: a `` function_id `` (to determine which implementation to test your code with), and the target `` z ``.
*   The judge will call your `` findSolution `` and compare your results with the __answer key__.
*   If your results match the __answer key__, your solution will be `` Accepted ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> function_id = 1, z = 5
<strong>Output:</strong> [[1,4],[2,3],[3,2],[4,1]]
<strong>Explanation:</strong> The hidden formula for function_id = 1 is f(x, y) = x + y.
The following positive integer values of x and y make f(x, y) equal to 5:
x=1, y=4 -&gt; f(1, 4) = 1 + 4 = 5.
x=2, y=3 -&gt; f(2, 3) = 2 + 3 = 5.
x=3, y=2 -&gt; f(3, 2) = 3 + 2 = 5.
x=4, y=1 -&gt; f(4, 1) = 4 + 1 = 5.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> function_id = 2, z = 5
<strong>Output:</strong> [[1,5],[5,1]]
<strong>Explanation:</strong> The hidden formula for function_id = 2 is f(x, y) = x * y.
The following positive integer values of x and y make f(x, y) equal to 5:
x=1, y=5 -&gt; f(1, 5) = 1 * 5 = 5.
x=5, y=1 -&gt; f(5, 1) = 5 * 1 = 5.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= function_id &lt;= 9 ``
*   `` 1 &lt;= z &lt;= 100 ``
*   It is guaranteed that the solutions of `` f(x, y) == z `` will be in the range `` 1 &lt;= x, y &lt;= 1000 ``.
*   It is also guaranteed that `` f(x, y) `` will fit in 32 bit signed integer if `` 1 &lt;= x, y &lt;= 1000 ``.