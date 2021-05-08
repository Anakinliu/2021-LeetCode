
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */
 var hasPathSum = function(root, targetSum) {
    let has = false;
    function DFS(root, s) {

        if (root) {
            if (root.left === null && root.right === null) {
                if (root.val + s === targetSum) {
                    has = true;
                    return
                }
            }
            if (root.left) {
                DFS(root.left, root.val + s);
            }
            if (has) {
                return
            }
            if (root.right) {
                DFS(root.right, root.val + s);
            }
            if (has) {
                return
            }
        }
    }
    DFS(root, 0);
    return has;
};

hasPathSum(1,2);