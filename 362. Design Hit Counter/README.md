# Problem: 362. Design Hit Counter
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
 

Example 1:

Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.
 

Constraints:

1 <= timestamp <= 2 * 109
All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
At most 300 calls will be made to hit and getHits.
 

Follow up: What if the number of hits per second could be huge? Does your design scale?

## Approach: 
The code above implements a HitCounter class that tracks the number of hits received within the last 300 seconds. It uses a deque (double-ended queue) data structure to store the timestamps of the hits.

The hit() method adds a new timestamp to the end of the deque.

The getHits() method removes all timestamps from the beginning of the deque that are older than 300 seconds ago, and then returns the length of the remaining deque, which represents the number of hits within the last 300 seconds.

## Complexity: 
The time complexity of the hit() method is O(1) because it performs a single append operation on the deque, which has a constant time complexity.

The time complexity of the getHits() method depends on the number of outdated timestamps in the deque. In the worst case, if all timestamps are outdated, it would have a linear time complexity of O(n), where n is the number of timestamps in the deque. However, in practice, the number of outdated timestamps is expected to be relatively small compared to the total number of hits, so the average time complexity of getHits() can be considered closer to O(1).

The space complexity of the HitCounter class is O(n), where n is the number of hits stored in the deque. The deque grows in size as more hits are recorded, and it retains all the timestamps until they become outdated.