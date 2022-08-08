#2525 오븐시계

hour, min = map(int, input().split())
time_need = int(input())

if min + time_need >= 60:
    minute = (min + time_need)%60
    hour += (min + time_need)//60
    if hour >= 24:
        hour = 0 + hour - 24
else:
    minute = min + time_need

print(hour, minute)