function divisor(n) {
    if (n == 0) return 1;
    let cnt = 0;
    
    for(let i=1; i<=Math.sqrt(n); i++) {
        if(n % i == 0) {
            cnt += (n / i == i) ? 1 : 2;
        }
    }
    
    return cnt;
}

function solution(number, limit, power) {
    var answer = 0;
    for (let i = 1; i < number + 1; i++) {
        const p = divisor(i);
        answer += (p > limit) ? power : p;
    }
    return answer;
}