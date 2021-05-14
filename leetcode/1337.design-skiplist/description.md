Design a Skiplist without using any built-in libraries.

_A Skiplist is a data structure that takes&nbsp;O(log(n)) time&nbsp;to `` add ``, `` erase `` and `` search ``. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be&nbsp;comparatively short and the idea behind Skiplists are just simple linked lists._

_For example:&nbsp;we have a Skiplist containing `` [30,40,50,60,70,90] `` and we want to add `` 80 `` and `` 45 `` into it. The&nbsp;Skiplist works this way:_

<img alt="" src="https://assets.leetcode.com/uploads/2019/09/27/1506_skiplist.gif" style="width: 960px; height: 332px;"/>

  
<small>Artyom Kalinin \[CC BY-SA 3.0\], via <a href="https://commons.wikimedia.org/wiki/File:Skip_list_add_element-en.gif" target="_blank" title="Artyom Kalinin [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons">Wikimedia Commons</a></small>

_You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, `` add ``&nbsp;,&nbsp;`` erase ``&nbsp;and `` search&nbsp; ``can be faster than O(n).&nbsp;It can be proven&nbsp;that the average time complexity for each operation is O(log(n)) and space complexity is O(n)._

To be specific, your design should include these functions:

*   `` bool search(int target) `` : Return whether&nbsp;the `` target `` exists in the Skiplist&nbsp;or not.
*   `` void add(int num) ``:&nbsp;Insert a value into the SkipList.&nbsp;
*   `` bool erase(int num) ``: Remove a value in&nbsp;the Skiplist.&nbsp;If `` num ``&nbsp;does not exist in the Skiplist, do nothing and return false. If there exists multiple `` num `` values, removing&nbsp;any one of them is fine.

See more about Skiplist :&nbsp;<a href="https://en.wikipedia.org/wiki/Skip_list" target="_blank">https://en.wikipedia.org/wiki/Skip\_list</a>

Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

&nbsp;

__Example:__

<pre>
Skiplist skiplist = new Skiplist();

skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // return false.
skiplist.add(4);
skiplist.search(1);   // return true.
skiplist.erase(0);    // return false, 0 is not in skiplist.
skiplist.erase(1);    // return true.
skiplist.search(1);   // return false, 1 has already been erased.</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= num, target&nbsp;&lt;= 20000 ``
*   At most `` 50000 ``&nbsp;calls will be made to `` search ``, `` add ``, and `` erase ``.