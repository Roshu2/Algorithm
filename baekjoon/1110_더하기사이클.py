n = int(input())
num = n
count = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    count += 1
    
    if num == n:
        break

print(count)




# def get_cycle(n):
#     count = 0
#     if n < 10:
#         m = n * 10
#         return get_cycle(m)
#     else:
#         sum_result = (n // 10) + (n % 10)
#         new_num = (n % 10) * 10 + sum_result
#         count += 1
#         if new_num == n:
#             print(count)
#         else:
#            return get_cycle(new_num)

# get_cycle(n)