function selectionSort(arr) {
    let len = arr.length;
    let minIndex = 0;
    for (let i=0; i<len-1; i++) {
        minIndex = i;
        for (let j=i+1; j<len; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
    }
    return arr;
}

arr = [1,3,5,7,2,4,6,8];
console.log(selectionSort(arr));