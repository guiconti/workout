An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the `` UndergroundSystem `` class:

*   `` void checkIn(int id, string stationName, int t) ``
    
    *   A customer with a card ID equal to `` id ``, checks in at the station `` stationName `` at time `` t ``.
    *   A customer can only be checked into one place at a time.
    
    
    
*   `` void checkOut(int id, string stationName, int t) ``
    
    *   A customer with a card ID equal to `` id ``, checks out from the station `` stationName `` at time `` t ``.
    
    
    
*   `` double getAverageTime(string startStation, string endStation) ``
    
    *   Returns the average time it takes to travel from `` startStation `` to `` endStation ``.
    *   The average time is computed from all the previous traveling times from `` startStation `` to `` endStation `` that happened __directly__, meaning a check in at `` startStation `` followed by a check out from `` endStation ``.
    *   The time it takes to travel from `` startStation `` to `` endStation `` __may be different__ from the time it takes to travel from `` endStation `` to `` startStation ``.
    *   There will be at least one customer that has traveled from `` startStation `` to `` endStation `` before `` getAverageTime `` is called.
    
    
    

You may assume all calls to the `` checkIn `` and `` checkOut `` methods are consistent. If a customer checks in at time <code>t<sub>1</sub></code> then checks out at time <code>t<sub>2</sub></code>, then <code>t<sub>1</sub> &lt; t<sub>2</sub></code>. All events happen in chronological order.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

<strong>Output</strong>
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

<strong>Explanation</strong>
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);  // Customer 45 "Leyton" -&gt; "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20);  // Customer 27 "Leyton" -&gt; "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22); // Customer 32 "Paradise" -&gt; "Cambridge" in 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.00000. One trip "Paradise" -&gt; "Cambridge", (14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000. Two trips "Leyton" -&gt; "Waterloo", (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);  // Customer 10 "Leyton" -&gt; "Waterloo" in 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.00000. Three trips "Leyton" -&gt; "Waterloo", (10 + 12 + 14) / 3 = 12
</pre>

__Example 2:__

<pre>
<strong>Input</strong>
["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
[[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]

<strong>Output</strong>
[null,null,null,5.00000,null,null,5.50000,null,null,6.66667]

<strong>Explanation</strong>
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8); // Customer 10 "Leyton" -&gt; "Paradise" in 8-3 = 5
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.00000, (5) / 1 = 5
undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16); // Customer 5 "Leyton" -&gt; "Paradise" in 16-10 = 6
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.50000, (5 + 6) / 2 = 5.5
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30); // Customer 2 "Leyton" -&gt; "Paradise" in 30-21 = 9
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 6.66667, (5 + 6 + 9) / 3 = 6.66667
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= id, t &lt;= 10<sup>6</sup></code>
*   `` 1 &lt;= stationName.length, startStation.length, endStation.length &lt;= 10 ``
*   All strings consist of uppercase and lowercase English letters and digits.
*   There will be at most <code>2 * 10<sup>4</sup></code> calls __in total__ to `` checkIn ``, `` checkOut ``, and `` getAverageTime ``.
*   Answers within <code>10<sup>-5</sup></code> of the actual value will be accepted.