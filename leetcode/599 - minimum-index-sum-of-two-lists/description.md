Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their __common interest__ with the __least list index sum__. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
<strong>Output:</strong> ["Shogun"]
<strong>Explanation:</strong> The only restaurant they both like is "Shogun".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
<strong>Output:</strong> ["Shogun"]
<strong>Explanation:</strong> The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
<strong>Output:</strong> ["KFC","Burger King","Tapioca Express","Shogun"]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
<strong>Output:</strong> ["KFC","Burger King","Tapioca Express","Shogun"]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> list1 = ["KFC"], list2 = ["KFC"]
<strong>Output:</strong> ["KFC"]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= list1.length, list2.length &lt;= 1000 ``
*   `` 1 &lt;= list1[i].length, list2[i].length &lt;= 30 ``
*   `` list1[i] `` and `` list2[i] `` consist of spaces `` ' ' `` and English letters.
*   All the stings of `` list1 `` are __unique__.
*   All the stings of `` list2 ``&nbsp;are __unique__.