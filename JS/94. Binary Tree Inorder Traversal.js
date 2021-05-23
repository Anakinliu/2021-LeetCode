function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
// 递归版
var inorderTraversal = function (root) {
  const result = [];
  const doTrav = function (root) {
    if (root) {
      doTrav(root.left);
      result.push(root.val);
      doTrav(root.right);
    }
  }
  return result;
};
// 迭代版
var inorderTraversal2 = function (root) {
  let stash=[];
  let result=[];
  while(stash.length||root){
      if(root){  // 放入当前节点的所有左的左的左。。。
          stash.push(root);
          root=root.left;
      }else{  // 访问最左的，并放入右节点
          root = stash.pop();
          result.push(root.val);
          root=root.right;
      }
  }
  return result;
};
