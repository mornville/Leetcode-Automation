# 116. Detect Pattern of Length M Repeated K or More Times
### Difficulty: Easy
Given an array of positive integers arr,  find a pattern of length m that is repeated k or more times. <br/> A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions. <br/> Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false. <br/>   <br/><b>- Example</b> 1: <br/> Input: arr = [1,2,4,4,4,4], m = 1, k = 3 <br/> Output: true <br/> Explanation: The pattern (4) of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less. <br/> <br/><b>- Example</b> 2: <br/> Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2 <br/> Output: true <br/> Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times. Another valid pattern (2,1) is also repeated 2 times. <br/> <br/><b>- Example</b> 3: <br/> Input: arr = [1,2,1,2,1,3], m = 2, k = 3 <br/> Output: false <br/> Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times. <br/> <br/><b>- Example</b> 4: <br/> Input: arr = [1,2,3,1,2], m = 2, k = 2 <br/> Output: false <br/> Explanation: Notice that the pattern (1,2) exists twice but not consecutively, so it doesn't count. <br/> <br/><b>- Example</b> 5: <br/> Input: arr = [2,2,2,2], m = 2, k = 3 <br/> Output: false <br/> Explanation: The only pattern of length 2 is (2,2) however it's repeated only twice. Notice that we do not count overlapping repetitions. <br/>   Constraints: <br/> 2 <= arr.length <= 100 <br/> 1 <= arr[i] <= 100 <br/> 1 <= m <= 100 <br/> 2 <= k <= 100