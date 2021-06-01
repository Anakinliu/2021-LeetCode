
//  Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
//  Input: head = [1,2,3,4,5], n = 2
//  Output: [1,2,3,5]
var removeNthFromEnd = function (head, n) {
    let hh = new ListNode();
    hh.next = head;
    let slow = hh;
    let fast = hh;
    while (n >= 0) {
        fast = fast.next;
        n -= 1;
    }
    while (fast) {
        fast = fast.next;
        slow = slow.next;
    }
    slow.next = fast;
    return hh.next;
};