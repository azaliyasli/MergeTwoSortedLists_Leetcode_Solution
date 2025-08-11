# 🟢 Merge Two Sorted Lists
**Problem link:** [Merge TWo Sorted List](https://leetcode.com/problems/merge-two-sorted-lists)

**Difficulty:** Easy

**Runtime:** 0 ms

**Memory Usage:** 17.9 MB

---

### 🧠 Approach
- Create a dummy node (mergedList) as a starting point.
- Use a lastNode pointer to keep track of the end of the merged list.
- While both lists are non-empty:
- Compare the val of the current nodes.
- Append the smaller one to the merged list.
- Move the pointer forward in the list from which a node was taken.
- Once one list is empty, attach the remaining nodes of the other list directly.
- Return mergedList.next (skipping the dummy head).

This approach runs in O(n + m) time, where n and m are the lengths of the two lists, and uses O(1) extra space.
