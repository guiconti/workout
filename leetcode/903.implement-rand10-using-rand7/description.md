Given the __API__ `` rand7() `` that generates a uniform random integer in the range `` [1, 7] ``, write a function `` rand10() `` that generates a uniform random integer in the range `` [1, 10] ``. You can only call the API `` rand7() ``, and you shouldn't call any other API. Please __do not__ use a language's built-in random API.

Each test case will have one __internal__ argument `` n ``, the number of times that your implemented function `` rand10() `` will be called while testing. Note that this is __not an argument__ passed to `` rand10() ``.

__Follow up:__

*   What is the <a href="https://en.wikipedia.org/wiki/Expected_value" target="_blank">expected value</a>&nbsp;for the number of calls to&nbsp;`` rand7() ``&nbsp;function?
*   Could you minimize the number of calls to `` rand7() ``?

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> [2]
</pre>

__Example 2:__

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> [2,8]
</pre>

__Example 3:__

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> [3,8,10]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>