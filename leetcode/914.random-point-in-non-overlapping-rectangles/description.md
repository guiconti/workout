Given a list of __non-overlapping__&nbsp;axis-aligned rectangles `` rects ``, write a function `` pick `` which randomly and uniformily picks an __integer point__ in the space&nbsp;covered by the rectangles.

Note:

1.   An __integer point__&nbsp;is a point that has integer coordinates.&nbsp;
2.   A point&nbsp;on the perimeter&nbsp;of a rectangle is&nbsp;__included__ in the space covered by the rectangles.&nbsp;
3.   `` i ``th rectangle = `` rects[i] `` =&nbsp;`` [x1,y1,x2,y2] ``, where `` [x1, y1] ``&nbsp;are the integer coordinates of the bottom-left corner, and `` [x2, y2] ``&nbsp;are the integer coordinates of the top-right corner.
4.   length and width of each rectangle does not exceed `` 2000 ``.
5.   `` 1 &lt;= rects.length&nbsp;&lt;= 100 ``
6.   `` pick `` return a point as an array of integer coordinates&nbsp;`` [p_x, p_y] ``
7.   `` pick `` is called at most `` 10000 ``&nbsp;times.

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: 
</strong><span id="example-input-1-1">["Solution","pick","pick","pick"]
</span><span id="example-input-1-2">[[[[1,1,5,5]]],[],[],[]]</span>
<strong>Output: 
</strong><span id="example-output-1">[null,[4,1],[4,1],[3,3]]</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: 
</strong><span id="example-input-2-1">["Solution","pick","pick","pick","pick","pick"]
</span><span id="example-input-2-2">[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]</span>
<strong>Output: 
</strong><span id="example-output-2">[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]</span></pre>
</div>
<div>
<p><strong>Explanation of Input Syntax:</strong></p>
<p>The input is two lists:&nbsp;the subroutines called&nbsp;and their&nbsp;arguments.&nbsp;<code>Solution</code>'s&nbsp;constructor has one argument, the array of rectangles <code>rects</code>. <code>pick</code>&nbsp;has no arguments.&nbsp;Arguments&nbsp;are&nbsp;always wrapped with a list, even if there aren't any.</p>
</div>
</div>

<div>
<div>&nbsp;</div>
</div>