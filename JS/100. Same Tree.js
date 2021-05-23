
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
    const inorder = function(a,b) {
        if (!a && !b) {
            return true;
        }
        if (a && b) {
            return a.val === b.val && (a.left, b.left) && (a.right, b.right);
        }
        return false;
    }
    inorder(p, q);
};