var permute = function (nums) {
    let res = [];
    let N = nums.length;
    let visited = Array(N).fill(false);
    function hui(path) {
        if (path.length === N) {
            console.log(path);
            // 浅复制数组
            res.push(Array.from(path));
            return;
        }
        // 遍历visited数组
        for (let i = 0; i < N; i++) {
            if (!visited[i]) {
                path.push(nums[i])
                visited[i] = true;
                hui(path);
                // 执行到这里时
                path.pop();  // 状态还原
                visited[i] = false;  // 状态还原
            }
        }
    }
    hui([]);
    console.log(res);
};
// 为什么[1,2,3]下一个状态是[1,3,2]?
// 因为达到[1,2,3]状态时,执行path.pop(); 和visited[i] = false;
// 然后,返回到上一层调用,此时又执行了path.pop(); 和visited[i] = false;
// 但是,但是!此时i已经是1了,下一个循环,i就是2了,此时visited[2]为false,所以,此时会放入数字3,即path变为[1,3]!

permute([1, 2, 3])
permute([1])