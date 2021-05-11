function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function (l1, l2) {
    let pre = new ListNode();
    const head = pre;
    let l1Temp = l1;
    let l2Temp = l2;
    while (l1Temp && l2Temp) {
        // const node = new ListNode();
        if (l1Temp.val < l2Temp.val) {
            pre.next = l1Temp;
            l1Temp = l1Temp.next;
        } else {
            pre.next = l2Temp;
            l2Temp = l2Temp.next;
        }
        pre = pre.next;
    }
    pre.next = l1Temp || l2Temp;
    return head.next;
};
