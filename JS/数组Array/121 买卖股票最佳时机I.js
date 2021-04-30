//  只需迭代一次
var maxProfit = function(prices) {
    let min_price = Number.MAX_VALUE;
    let max_pro = 0;
    console.log(min_price);
    for (let i=0; i < prices.length; i++) {
        console.log(prices[i]);
        if (prices[i] < min_price) {
            min_price = prices[i];
            
        } else if (prices[i] - min_price > max_pro) {
            max_pro = prices[i] - min_price;
        }
    }
    return max_pro;
};

console.log(maxProfit([7,1,5,3,6,4]));















