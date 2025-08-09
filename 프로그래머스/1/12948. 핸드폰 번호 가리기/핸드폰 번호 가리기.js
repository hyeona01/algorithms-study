function solution(phone_number) {
    var answer = '';
    answer = "*".repeat(phone_number.length - 4);
    console.log(answer);
    answer += phone_number.slice(phone_number.length - 4, phone_number.length)
    return answer;
}