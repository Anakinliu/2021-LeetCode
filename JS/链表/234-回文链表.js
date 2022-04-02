function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

let n1 = new ListNode(1)

let n2 = new ListNode(2)
let n3 = new ListNode(2)
let n4 = new ListNode(2)

n1.next = n2;
n2.next = n3;
n3.next = n4;

// 傻瓜版本，遍历后放到数组里，再检查数组回文
var isPalindrome = function (head) {
    const valueArray = [];
    let node = head;
    while (node) {
        valueArray.push(node.val);
        node = node.next;
    }
    let left = 0;
    let right = valueArray.length - 1;
    while (left <= right) {
        if (valueArray[left] !== valueArray[right]) {
            return false
        }
        left += 1;
        right -= 1;
    }
    return true;
};
// 用函数调用栈作为后序遍历栈，来判断是否回文
var isPalindrome2 = function (head) {
    let isP = true;
    let n2 = head;
    function postorder(node) {
        if (!node || !isP) {
            return;
        }
        postorder(node.next);
        console.log(node.val, ", ", n2.val);

        if (node.val !== n2.val) {
            isP = false;
        }
        n2 = n2.next;

    }
    postorder(head, head);
    return isP;
}
// 函数调用栈版本的答案
var isPalindrome3 = function (head) {
    let n2 = head;
    function postorder(node) {
        if (!node) {
            return true;
        }
        let res = postorder(node.next);
        console.log(node.val, ", ", n2.val);
        // 用if比用&&慢了十倍？？？
        // if (res && node.val !== n2.val) {
        //     res = false;
        // }
        res = res && (node.val === n2.val);
        n2 = n2.next;
        return res;

    }
    return postorder(head, head);
}
console.log(isPalindrome3(n1));
