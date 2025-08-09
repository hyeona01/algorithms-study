function solution(nums) {
    var answer = 0;
    const s = new Set();
    
    for(let x of nums) {
        s.add(x);
    }
    
    const selectCnt = Math.floor(nums.length / 2);
    return s.size > selectCnt ? selectCnt : s.size;
}