import random
print('''
    Chào mừng bạn đến với game ĐOÁN SỐ ^^
- Tôi đã ra một con số bí mật từ 1 - 100
- Bây giờ bạn có 3 lượt chơi hãy đoán con số đó nào.''')
secret = random.randint(1,100) #randint trả về số nguyên ngẫu nhiên trong khoảng đó
point = 0 #Điềm số
print(secret)
for i in range(1,4):
    a = int(input(f"Mời bạn nhập 1 số bạn thích từ 1 - 100 lần {i}: "))
    if a == secret:
        if i == 1:
            point = 100
        elif i == 2:
            point = 50
        elif i == 3:
            point = 30
        print("Chúc mừng bạn đã chiến thắng với số điểm là:",point)
        break
    else:
        if i == 3:
            print(f"Game Over
                  số bí mật đó là {secret}")
            #break
        elif a > secret:
            print("Aaaa sai rồi, số bạn lớn quá. Hãy nhập lại!")
        else:
            print("Aaaa sai rồi, số bạn nhỏ quá. Hãy nhập lại!")       

# refactor
