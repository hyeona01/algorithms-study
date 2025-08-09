function solution(n)
{
    var answer = 0;
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log('Hello Javascript')
    
    const arr = String(n).split('').map(Number);
    const sumArr = arr.reduce((a, b) => a + b);

    return sumArr;
}