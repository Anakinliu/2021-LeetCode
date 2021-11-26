/*
* @param { number[] } nums
* @param {number} target
* @return {number[]}
*/
var twoSum = function(nums, target) {
   // 构建一个hash表，元素值为hash值，因为元素不会重复出现，所以不会出现索引覆盖的情况
   let dict = {}
   nums.forEach((e, idx) => {
       dict[e] = idx;
   })
   for (let idx=0; idx < nums.length; idx++) {
       // target - e 就是另一个元素，如果此元素存在hash表，就是答案所求。
       let theOth = dict[target - nums[idx]];
       if (theOth !== idx && theOth > -1) {
           return [idx, theOth];
       }
   }
};