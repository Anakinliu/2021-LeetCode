/**
 * lru design
 * @param operators int整型二维数组 the ops
 * @param k int整型 the k
 * @return int整型一维数组
 */


function LRU(operators, limit) {
    // 定义链表数据结构
    class Node {
        constructor(key, value, next = null) {
            this.key = key;
            this.value = value;
            this.next = next;
        }
    }
    // write code here
    // let i = 0;
    // head不计入链表总个数，其next指向第一个node
    let head = new Node(Number.MIN_VALUE, Number.MIN_VALUE);
    const resArr = [];
    // tail不计入链表总个数，其next指向最后一个node
    // let tail = new Node(Number.MIN_VALUE, Number.MIN_VALUE);

    // 打印链表
    // while (head) {
    //     console.log(head.value);
    //     head = head.next;
    // }
    // console.log(tail.next.value);
    for (const [op, k, v] of operators) {
        let temp = head.next;
        let pre = head;
        if (v) { // put
            while (temp) {
                // key已经存在
                if (temp.key === k) {
                    let node = new Node(k, v);
                    // 删除此节点
                    pre.next = temp.next;
                    // 插入新节点
                    let t = head.next;
                    head.next = node;
                    node.next = t;
                    break;
                }
                pre = pre.next;
                temp = temp.next;
            }

            if (temp === null) {  // key 不存在，插入这个key的节点时，需要判断整个链表是否是满的！
                let node = new Node(k, v);
                let t = head.next;
                head.next = node;
                node.next = t;
            }
        } else { // get操作
            while (temp) {
                // key存在
                if (temp.key === k) {
                    // console.log(temp.value);
                    resArr.push(temp.value);
                    let node = new Node(k, temp.value);
                    // 删除此节点
                    pre.next = temp.next;
                    // 插入新节点
                    let t = head.next;
                    head.next = node;
                    node.next = t;
                    break;
                }
                pre = pre.next;
                temp = temp.next;
            }
            // 没找到，返回-1
            if (temp === null) {
                // console.log(-1);
                resArr.push(-1);
            }
        }
        
        // 截断链表
        let i = 1;
        temp = head;
        while (i <= limit && temp) {
            temp = temp.next;
            i += 1;
        }
        if (temp) {
            temp.next = null;
        }
    }

    // while (head) {
    //     console.log(head.value);
    //     head = head.next;
    // }
    // console.log(tail.next.value);
    console.log(resArr);
    return resArr;
}

LRU([[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3);

module.exports = {
    LRU: LRU
};