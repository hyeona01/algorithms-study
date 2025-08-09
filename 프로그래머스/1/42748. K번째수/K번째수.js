function solution(array, commands) {
    var answer = [];
    for(let [start, end, idx] of commands){
        const new_list = array.slice(start-1, end).sort((a,b)=>a-b);
        console.log(new_list);
        answer.push(new_list[idx-1]);
        console.log(new_list[idx-1]);
    }
    return answer;
}