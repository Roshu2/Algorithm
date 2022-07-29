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