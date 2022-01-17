import ascNum
import time

currTime = time.localtime()

if currTime.tm_hour <= 9:
    h0 = int(0)
    h1 = int(str(currTime.tm_hour)[0])
else:
    h0 = int(str(currTime.tm_hour)[0])
    h1 = int(str(currTime.tm_hour)[1])

if currTime.tm_min <= 9:
    m0 = int(0)
    m1 = int(str(currTime.tm_min)[0])
else:
    m0 = int(str(currTime.tm_min)[0])
    m1 = int(str(currTime.tm_min)[1])

for x in range(0, 5):
    timeStr = f"{ascNum.numbers[h0][x]}  {ascNum.numbers[h1][x]} {ascNum.numbers[10][x]} {ascNum.numbers[m0][x]}  {ascNum.numbers[m1][x]}"
    print(timeStr)
