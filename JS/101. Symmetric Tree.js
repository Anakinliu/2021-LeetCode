
//  Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
    const check = function (a, b) {
        if (!a && b) {
            return false;
        }
        if (a && !b) {
            return false;
        }
        if (!a && !b) {
            return true;
        }
        return a.val === b.val && check(a.left, b.right) && check(a.right, b.left);
    }
    return check(root.left, root.right);
}
