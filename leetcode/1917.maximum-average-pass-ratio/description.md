There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array `` classes ``, where <code>classes[i] = [pass<sub>i</sub>, total<sub>i</sub>]</code>. You know beforehand that in the <code>i<sup>th</sup></code> class, there are <code>total<sub>i</sub></code> total students, but only <code>pass<sub>i</sub></code> number of students will pass the exam.

You are also given an integer `` extraStudents ``. There are another `` extraStudents `` brilliant students that are __guaranteed__ to pass the exam of any class they are assigned to. You want to assign each of the `` extraStudents `` students to a class in a way that __maximizes__ the __average__ pass ratio across __all__ the classes.

The __pass ratio__ of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The __average pass ratio__ is the sum of pass ratios of all the classes divided by the number of the classes.

Return _the __maximum__ possible average pass ratio after assigning the _`` extraStudents ``_ students. _Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.

&nbsp;

__Example 1:__

<strong>Input:</strong> classes = [[1,2],[3,5],[2,2]], extraStudents = 2
    <strong>Output:</strong> 0.78333
    <strong>Explanation:</strong> You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

__Example 2:__

<strong>Input:</strong> classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
    <strong>Output:</strong> 0.53485

&nbsp;

__Constraints:__

*   <code>1 &lt;= classes.length &lt;= 10<sup>5</sup></code>
*   `` classes[i].length == 2 ``
*   <code>1 &lt;= pass<sub>i</sub> &lt;= total<sub>i</sub> &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= extraStudents &lt;= 10<sup>5</sup></code>