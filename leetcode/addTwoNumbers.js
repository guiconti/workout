/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  const answer = new ListNode(0);
  let currentAnswerNode = answer;
  let exceededSum = 0;
  
  while (l1 !== null || l2 !== null || exceededSum > 0) {
    if (l1 !== null) {
      currentAnswerNode.val += l1.val;
      l1 = l1.next;
    }
    if (l2 !== null) {
      currentAnswerNode.val += l2.val;
      l2 = l2.next;
    }
    currentAnswerNode.val += exceededSum;
    exceededSum = 0;
    if (currentAnswerNode.val / 10 >= 1) {
      exceededSum = Math.floor(currentAnswerNode.val / 10);
      currentAnswerNode.val = currentAnswerNode.val % 10;
    }
    if (l1 !== null || l2 !== null || exceededSum > 0) {
      currentAnswerNode.next = new ListNode(0);
      currentAnswerNode = currentAnswerNode.next;
    }
  }
  return answer;
};