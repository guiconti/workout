Implement the `` RandomizedCollection `` class:

*   `` RandomizedCollection() `` Initializes the `` RandomizedCollection `` object.
*   `` bool insert(int val) `` Inserts an item `` val `` into the multiset if not present. Returns `` true `` if the item was not present, `` false `` otherwise.
*   `` bool remove(int val) `` Removes an item `` val `` from the multiset if present. Returns `` true `` if the item was present, `` false `` otherwise. Note that if `` val `` has multiple occurrences in the multiset, we only remove one of them.
*   `` int getRandom() `` Returns a random element from the current multiset of elements (it's guaranteed that at least one element exists when this method is called). The probability of each element being returned is __linearly related__ to the number of same values the multiset contains.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
<strong>Output</strong>
[null, true, false, true, 2, true, 1]

<strong>Explanation</strong>
RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1);   // return True. Inserts 1 to the collection. Returns true as the collection did not contain 1.
randomizedCollection.insert(1);   // return False. Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
randomizedCollection.insert(2);   // return True. Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
randomizedCollection.getRandom(); // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
randomizedCollection.remove(1);   // return True. Removes 1 from the collection, returns true. Collection now contains [1,2].
randomizedCollection.getRandom(); // getRandom should return 1 and 2 both equally likely.
</pre>

&nbsp;

__Constraints:__

*   <code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code>
*   At most <code>10<sup>5</sup></code> calls will be made to `` insert ``, `` remove ``, and `` getRandom ``.
*   There will be __at least one__ element in the data structure when `` getRandom `` is called.

&nbsp;
__Follow up:__ Could you implement the functions of the class with each function works in __average__ `` O(1) `` time?