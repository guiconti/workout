Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return _the deserialized_ `` NestedInteger ``.

Each element is either an integer or a list whose elements may also be integers or other lists.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "324"
<strong>Output:</strong> 324
<strong>Explanation:</strong> You should return a NestedInteger object which contains a single integer 324.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "[123,[456,[789]]]"
<strong>Output:</strong> [123,[456,[789]]]
<strong>Explanation:</strong> Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code>
*   `` s `` consists of digits, square brackets `` "[]" ``, negative sign `` '-' ``, and commas `` ',' ``.
*   `` s `` is the serialization of valid `` NestedInteger ``.