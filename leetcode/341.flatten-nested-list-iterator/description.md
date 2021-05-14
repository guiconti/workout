You are given a nested list of integers `` nestedList ``. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the `` NestedIterator `` class:

*   `` NestedIterator(List&lt;NestedInteger&gt; nestedList) `` Initializes the iterator with the nested list `` nestedList ``.
*   `` int next() `` Returns the next integer in the nested list.
*   `` boolean hasNext() `` Returns `` true `` if there are still some integers in the nested list and `` false `` otherwise.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nestedList = [[1,1],2,[1,1]]
<strong>Output:</strong> [1,1,2,1,1]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nestedList = [1,[4,[6]]]
<strong>Output:</strong> [1,4,6]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nestedList.length &lt;= 500 ``
*   The values of the integers in the nested list is in the range <code>[-10<sup>6</sup>, 10<sup>6</sup>]</code>.