words = input()

alpha_occ_arr = [0] * 26

for char in words:
    if not char.isalpha():
        continue
    arr_index = ord(char) - ord('a')
    alpha_occ_arr[arr_index] += 1
    
max_occ = 0
max_aplha_index = 0
for i in range(len(alpha_occ_arr)):
    alpha_occ = alpha_occ_arr[i]
    if alpha_occ > max_occ:
        max_occ = alpha_occ
        max_aplha_index = i
print(chr(max_aplha_index + ord('a')))


word = input().lower() # lower는 소문자로만 받는 함수
word_list = list(set(word))
cnt = []
for i in word_list:
    count = word.count(i) # word안에 count함수로 알파벳 몇개있는데 int로 반환
    cnt.append(count)
if cnt.count(max(cnt)) >= 2:
    print("?") # cnt 리스트안에 가장큰 숫자가 두개이상이면 ? 프린트
else:
    print(word_list[cnt.index(max(cnt))].upper()) # upper는 대문자만 출력