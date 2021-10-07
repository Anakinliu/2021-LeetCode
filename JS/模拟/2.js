/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    let jin = 0;
    let sum = 0;
    // let res = [];
    let head = new ListNode();
    let tail = head;
    while (l1 || l2) {
        sum = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + jin;
        let node = new ListNode(sum % 10);
        tail.next = node;
        tail = node;
        jin = sum > 9 ? 1 : 0;
        l1 = l1 ? l1.next : null;
        l2 = l2 ? l2.next : null;
    }
    if (jin) {
        let node = new ListNode(1);
        tail.next = node;
    }
    return head.next;
};