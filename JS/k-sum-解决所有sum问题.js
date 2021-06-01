// @ybmlk
// 递归
var fourSum = function(nums, target) {
    nums.sort((a, b) => a - b);
    const result = [];
    
    // k represents N-sum, 
    // if k = 3 : 3Sum, if k = 4 : 4Sum, if k = 5, 5Sum; 
    function recurse(arr, tar, res, k) {
        // 递归结束条件，达到 2-sum 问题
        if(k === 2) {
            twoSum(arr, tar, res);
            return;
        }
        // 缩减问题
        for(let i = 0; i < arr.length; i++) {
            while(arr[i] === arr[i-1]) i++;
            recurse(arr.slice(i+1), tar - arr[i], [...res, arr[i]], k-1);
        }
    }
    
    function twoSum(arr, tar, res) {
        let low = 0, high = arr.length-1;
        while(low < high) {
            const sum = arr[low] + arr[high];
            if(sum === tar)  {
                result.push([...res, arr[low], arr[high]]);
                while(arr[low] === arr[low+1]) low++;
                while(arr[high] === arr[high-1]) high--;
                low++;
                high--;
            } else if(sum < tar) low++;
            else high--;
        }
    }
    
    recurse(nums, target, [], 4)
    return result
};
