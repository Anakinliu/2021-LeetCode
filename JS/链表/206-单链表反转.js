/**
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}
var reverseList = function (head) {
    let pre = null;
    let cur = head;
    while (cur) {
        let nxt = head.next;
        if (!nxt) {
            break;
        }
        cur.next = pre;
        pre = cur;
        cur = nxt;
    }
    return head;
};