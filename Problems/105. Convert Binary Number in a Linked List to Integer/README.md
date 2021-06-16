# 105. Convert Binary Number in a Linked List to Integer
### Difficulty: Easy
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number. <br/> Return the decimal value of the number in the linked list. <br/>   <br/><b>- Example</b> 1: <br/> Input: head = [1,0,1] <br/> Output: 5 <br/> Explanation: (101) in base 2 = (5) in base 10 <br/> <br/><b>- Example</b> 2: <br/> Input: head = [0] <br/> Output: 0 <br/> <br/><b>- Example</b> 3: <br/> Input: head = [1] <br/> Output: 1 <br/> <br/><b>- Example</b> 4: <br/> Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0] <br/> Output: 18880 <br/> <br/><b>- Example</b> 5: <br/> Input: head = [0,0] <br/> Output: 0 <br/>   Constraints: <br/> The Linked List is not empty. <br/> Number of nodes will not exceed 30. <br/> Each node's value is either 0 or 1.