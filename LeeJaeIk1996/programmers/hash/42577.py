'''
- 프로그래머스 해시 42577번: 전화번호 목록
- 해당 풀이는 파이썬의 sort()를 활용한 풀이입니다.

풀이 과정
1. sort()를 활용하여 접두사가 같은 순으로 정렬한다.
    해당 문제의 경우, 접두사가 있는 요소들을 전부 찾아내는 것이 아니라,
    하나라도 존재한다면 False 값을 추출하는 것이기 때문에
    정렬한 뒤 접두사와 접두사가 있는 문자열만 찾아내면 된다. 그러므로
    접두사: prefix_num = phone_book[phone_num]
    접두사가 있는 문자열: compare_num = phone_book[phone_num + 1]
    를 준비한다.
2. prefix_num이 compare_num에 있는지 확인한 뒤(prefix_num in compare_num),
    반대로 compare_num에 접두사가 들어있는지 확인(compare_num.find(prefix_num) == 0)
'''
def solution1(phone_book):
    phone_book.sort()   
    for phone_num in range(len(phone_book)):
        if phone_num == len(phone_book) - 1:  
            break
        prefix_num = phone_book[phone_num]
        compare_num = phone_book[phone_num + 1]
        
        if prefix_num in compare_num and compare_num.find(prefix_num) == 0:
            return False
        
    return True

'''
- 프로그래머스 해시 42577번: 전화번호 목록
- 해당 풀이는 해시를 활용한 풀이입니다.
- 해당 문제를 해시를 활용하여 푸는 방법을 몰라 인터넷 서치를 하여 공부한 뒤, 재작성한 코드입니다.

풀이 과정
1. 하나의 hash table(dictionary)을 만든다.
2. hash table에 phone_book 배열의 요소들을 저장한다.
    key: phone_book의 요소 / value: 1 (value = 1 은 숫자 요소가 한 개 존재한다는 의미)
3. 찾아야 되는 접두사 prefix 변수를 선언. 초기엔 빈 상태의 문자열을 생성
4. phone_book 배열의 문자열에서 문자 하나 하나들을 순회하며 prefix에 저장
5. 저장된 prefix를 갖고 기존에 만든 hash_table에 prefix가 있는지 검사
'''
def solution2(phone_book):
    hash_table = {}   # hash table을 만든다.
    for phone_number in phone_book:
        hash_table[phone_number] = 1  # key = phone_number / value = 1

    for phone_number in phone_book:
        prefix = ""
        for number in phone_number: # phone_book배열의 요소 하나 하나를 다시 반복한다.
            prefix += number    # 요소 하나 하나를 prefix에 합함
            if prefix in hash_table and prefix != phone_number:   # 접두사 prefix가 hash table에 존재하는지 확인
                return False

    return True


