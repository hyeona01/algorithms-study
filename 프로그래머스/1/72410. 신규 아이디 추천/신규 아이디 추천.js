function solution(new_id) {
    // 1단계: 대문자 → 소문자
    let id = new_id.toLowerCase();

    // 2단계: 허용된 문자만 남기기
    id = id.replace(/[^a-z0-9-_.]/g, '');

    // 3단계: 마침표 2번 이상 → 1번
    id = id.replace(/\.{2,}/g, '.');

    // 4단계: 처음과 끝의 마침표 제거
    id = id.replace(/^\.|\.$/g, '');
    
    // 5단계
    if(id == "") id = "a";
    
    // 6단계
    if(id.length >= 16){
        id = id.slice(0, 15);
        id = id.replace(/\.$/g, '');
    }
    
    // 7단계
    if(id.length <= 2){
        const lastChar = id[id.length - 1];
        id = id + lastChar.repeat(3 - id.length);
    }
    return id;
}