# MoreThanMean
# หาจำนวนข้อมูลที่มีค่ามากกว่าค่าเฉลี่ย

# รับจำนวนข้อมูล
N = int(input())

# รับข้อมูล N จำนวน
numbers = []

for i in range(N):
    number = float(input())
    numbers.append(number)

# คำนวณค่าเฉลี่ย
mean = sum(numbers) / N

# นับจำนวนที่มากกว่าค่าเฉลี่ย
count = 0

for number in numbers:
    if number > mean:
        count += 1

# แสดงผล
print(count)
