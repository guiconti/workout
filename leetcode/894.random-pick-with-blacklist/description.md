Given a blacklist `` blacklist `` containing unique integers from `` [0, n) ``, write a function to return a uniform random integer from `` [0, n) `` which is __NOT__ in `` blacklist ``.

Optimize it such that it minimizes the call to system’s `` Math.random() ``.

__Note:__

1.   `` 1 &lt;= n &lt;= 1000000000 ``
2.   `` 0 &lt;= blacklist.length &lt; min(100000, n) ``
3.   `` [0, n) `` does NOT include n. See <a href="https://en.wikipedia.org/wiki/Interval_(mathematics)" target="_blank">interval notation</a>.

__Example 1:__

<pre>
<strong>Input: 
</strong><span id="example-input-1-1">["Solution","pick","pick","pick"]
</span><span id="example-input-1-2">[[1,[]],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,0,0,0]</span>
</pre>

__Example 2:__

<pre>
<strong>Input: 
</strong><span id="example-input-2-1">["Solution","pick","pick","pick"]
</span><span id="example-input-2-2">[[2,[]],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-2">[null,1,1,1]</span>
</pre>

__Example 3:__

<pre>
<strong>Input: 
</strong><span id="example-input-3-1">["Solution","pick","pick","pick"]
</span><span id="example-input-3-2">[[3,[1]],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-3">[null,0,0,2]</span>
</pre>

__Example 4:__

<pre>
<strong>Input: 
</strong><span id="example-input-4-1">["Solution","pick","pick","pick"]
</span><span id="example-input-4-2">[[4,[2]],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-4">[null,1,3,1]</span>
</pre>

__Explanation of Input Syntax:__

The input is two lists: the subroutines called and their arguments. `` Solution ``'s constructor has two arguments, `` n `` and the blacklist `` blacklist ``. `` pick `` has no arguments. Arguments are always wrapped with a list, even if there aren't any.