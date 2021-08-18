function TreeNode(val, left, right) {
    this.val = val || 0;
    this.left = left || null;
    this.right = right || null;
}

// 题目要求:输入两组数字,每组组内数字不重复,分别表示前序和中序遍历序列,构建出二叉树

// 普通二叉树
// let preArr = [1, 2, 4, 7, 3, 5, 6, 8];
// let inArr = [4, 7, 2, 1, 5, 3, 8, 6];、
// 全左树
// let preArr = [1, 2, 3, 4];
// let inArr = [4, 3, 2, 1];
// 全右数树
// let preArr = [1, 2, 3, 4];
// let inArr = [1, 2, 3, 4];
// 错误输入
// let preArr = [1, 2, 4, 3, 5, 7, 6, 8];
// let inArr = [4, 7, 2, 1, 5, 3, 8, 6];
/**
 *
 * @param {*} preSeg  一个子树的先序片段
 * @param {*} inSeg  一个子树的中序片段
 * @returns 构建完成后的子树的根节点
 */
function build(preSeg, inSeg) {
    if (preSeg.length !== inSeg.length) {
        throw Error('输入有误');
    }
    if (preSeg.length === 1) {
        // 叶子节点,不必找左右子树了
        return new TreeNode(preSeg[0]);
    }
    if (preSeg.length === 0) {
        return null;
    }
    let rootVal = preSeg[0];

    let inorderEndIdx = inSeg.indexOf(rootVal);
    // 构造子树根节点
    let rootNode = new TreeNode(rootVal);
    // slice可能会超过inArr长度,但是对Js的slice来说,没关系,结果是空数组,所以不用进行判断是否越界

    // 传入左子树的先序遍历和中序遍历片段,返回的就是左孩子
    rootNode.left = build(
        preSeg.slice(1, 1 + inorderEndIdx),
        inSeg.slice(0, inorderEndIdx)
    );
    // 传入右子树的先序遍历和中序遍历片段,返回的就是右孩子
    rootNode.right = build(
        preSeg.slice(1 + inorderEndIdx, preSeg.length),
        inSeg.slice(inorderEndIdx + 1, inSeg.length)
    );
    return rootNode;
}

let root = build(preArr, inArr)
console.dir(root);