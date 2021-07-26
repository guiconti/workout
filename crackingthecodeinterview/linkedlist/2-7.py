def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    currentNodeA = headA
    sizeA = 0
    currentNodeB = headB
    sizeB = 0
    while currentNodeA or currentNodeB:
      if currentNodeA:
        sizeA += 1
        currentNodeA = currentNodeA.next
      if currentNodeB:
        sizeB += 1
        currentNodeB = currentNodeB.next
    
    biggestListNode = headA
    smallestListNode = headB
    difference = abs(sizeA - sizeB)
    if sizeB > sizeA:
      biggestListNode = headB
      smallestListNode = headA
    for i in range(difference):
      biggestListNode = biggestListNode.next
    while biggestListNode != smallestListNode:
      biggestListNode = biggestListNode.next
      smallestListNode = smallestListNode.next
    return biggestListNode