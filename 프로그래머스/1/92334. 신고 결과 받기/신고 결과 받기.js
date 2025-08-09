function solution(id_list, report, k) {
    const caution_list = {};
    const adj_list = {};
    
    for(let x of id_list){
        caution_list[x] = 0;
        adj_list[x] = new Set();  // 중복 제거
    }
    
    for(let i=0; i < report.length; i++){
        const info = report[i].split(" ");
        const user = info[0];
        const author = info[1];
        
        adj_list[user].add(author);
    }
    
    // 신고당한 횟수 계산
    for(let user of id_list){
        for(let reported of adj_list[user]){
            caution_list[reported] += 1;
        }
    }
    
    const result = [];
    for(let x of id_list){
        let cnt = 0;
        for(let reported of adj_list[x]){
            if(caution_list[reported] >= k){
                cnt += 1;
            }
        }
        result.push(cnt);
    }
    return result;
}