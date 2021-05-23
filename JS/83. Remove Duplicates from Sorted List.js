function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
// nxt 指向 val 与 pre 不同的位置，需要两个while 
var deleteDuplicates = function (head) {
    let pre = head;
    while (pre) {
      let nxt = pre.next;
      while (nxt && nxt.val === pre.val) {
        nxt = nxt.next;
      }
      pre.next = nxt;
      pre = nxt;
    }
    return head;
};

var deleteDuplicates = function (head) {
  let pre = head;
  while (pre) {
    if (pre.next && pre.next.val == pre.val) {
      pre.next = pre.next.next;
    } else {
      pre = pre.next;
    }
  }
  return head;
};
