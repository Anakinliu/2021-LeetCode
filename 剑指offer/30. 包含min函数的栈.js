/**
 * 跳过此题
 * initialize your data structure here.
 */
 var MinStack = function() {
    this.dataStack = [];
    this.minStack = [Infinity];
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    this.dataStack.push(x);
    this.minStack.push(Math.min(x, this.minStack[this.minStack.length - 1]));
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.dataStack.pop();
    this.minStack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.dataStack[this.dataStack.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.min = function() {
    return this.minStack[this.minStack.length - 1];
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.min()
 */