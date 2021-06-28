
//  Definition for a binary tree node.
 function TreeNode(val, left, right) {
     this.val = (val===undefined ? 0 : val)
     this.left = (left===undefined ? null : left)
     this.right = (right===undefined ? null : right)
 }
 
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
 var isBalanced = function(root) {
    function isBST(node){
        // 终止条件
        if (!node) {
            console.log('null', node);
            return {depth: 0, isB: true};
        }
        const left = isBST(node.left);
        const right = isBST(node.right);
        console.log(node.val, 'left: ', left.depth, 'right: ', right.depth);
        // 平衡需要满足：1. 此次调用的root的左右都是平衡的 2.左右高度之差小于2
        if (left.isB === false || right.isB === false) {
            console.log('1: ',left.val,roght.val)
            return {depth:0, isB: false};
        }
        if (Math.abs(left.depth - right.depth) > 1) {
            console.log('2: ', Math.abs(left.depth - right.depth), 'val: ', node.val)
            return {depth:0, isB:false};
        }
        // 此次调用的root是平衡的，返回树的深度为左右俩子树最大深度+1
        
        return {depth:Math.max(left.depth, right.depth) +1, isB:true};
    }
    return isBST(root).isB
};
 
const n1 = new TreeNode(9, null, null);
const n2 = new TreeNode(15, null, null);
const n3 = new TreeNode(7, null, null);
const n4 = new TreeNode(20, n2, n3);
const n5 = new TreeNode(3, n1, n4);

console.log(isBalanced(n5));