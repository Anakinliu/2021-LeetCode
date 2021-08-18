function ListNode(val, nxt) {
    this.val = val || 0;
    this.nxt = nxt || null;
}

let n1 = new ListNode(2);
let n2 = new ListNode(4);
let n3 = new ListNode(6);

n1.nxt = n2;
n2.nxt = n3;

function zhengXu(head) {
    while (head) {
        console.log(head.val);
        head = head.nxt;
    }
}
zhengXu(n1);

function niXu(head) {
    let stack = [];
    while (head) {
        stack.push(head.val);
        head = head.nxt;
    }
    while (stack.length) {
        console.log(stack.pop());
    }
}
niXu(n1);

// 递归本质是一个栈结构
function niXuRecur(head) {
    if (!head) {
        return;
    }
    niXu(head.nxt);
    console.log(head.val);
}
niXuRecur(n1);