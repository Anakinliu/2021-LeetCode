var groupAnagrams = function (strs) {
    const sortStr = str => Array.from(str).sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join("");
    let sortedStrs = strs.map(e => sortStr(e))
    console.log(sortedStrs);
    let mapSameStr = {};
    sortedStrs.forEach((element, idx) => {
        if (element in mapSameStr) {
            mapSameStr[element].push(idx);
        } else {
            mapSameStr[element] = [idx];
        }
    });
    // console.log(mapSameStr);
    let res = []
    for (let key in mapSameStr) {
        let temp = [];
        for (let idx of mapSameStr[key]) {
            temp.push(strs[idx]);
        }
        res.push(temp);
    }
    console.log(res);
    return res;
};
groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
