/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(numbers, target) {
    let low = 0;
    let high = numbers.length-1;
    let s = numbers[low] + numbers[high];
    console.log(s);
    while (s != target) {
        if (s > target) {
            high--;
        }
        if (s < target) {
            low++;
        }
        s = numbers[low] + numbers[high];
    }
    return [low+1, high+1];
     
};

console.log(twoSum([2,7,11,15], target = 9)); 