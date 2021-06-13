
//Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
// 我TM直接三个指针
var swapPairs = function (head) {
    const hh = new ListNode();
    hh.next = head;
    let a = b = c = hh;
    while (c.next) {
        if (a.next) {
            b = a.next;
        } else {
            break;
        }
        if (b.next) {
            c = b.next;
        } else {
            break;
        }
        b.next = c.next;
        c.next = b;
        a.next = c;
        a = c = b;
    }
    return hh.next;
};