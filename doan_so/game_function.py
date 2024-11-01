import random

def generate_secret_number(min, max):
    secret = random.randint(min, max) #randint trả về số nguyên ngẫu nhiên trong khoảng đó
    return secret

def get_point(attemp):
    point = 0
    if attemp == 1:
        point = 100
    elif attemp == 2:
        point = 50
    elif attemp == 3:
        point = 30
    return point

def get_point_2(attemp):
    if attemp == 1:
        return 100
    elif attemp == 2:
        return 50
    elif attemp == 3:
        return 30
    
def get_point_3(attemp):
    if attemp == 1:
        return 100
    if attemp == 2:
        return 50
    if attemp == 3:
        return 30
    
def game_play(attemp_max, secret):
    for i in range(1, attemp_max):
        a = int(input(f"Mời bạn nhập 1 số bạn thích từ 1 - 100 lần {i}: "))
        if a == secret:
            point = get_point(i)
            print("Chúc mừng bạn đã chiến thắng với số điểm là:",point)
            break
        else:
            if i == 3:
                print(f"Game Over. số bí mật đó là {secret}")
            elif a > secret:
                print("Aaaa sai rồi, số bạn lớn quá. Hãy nhập lại!")
            else:
                print("Aaaa sai rồi, số bạn nhỏ quá. Hãy nhập lại!")    


def main():
    print('''
        Chào mừng bạn đến với game ĐOÁN SỐ ^^
        - Tôi đã ra một con số bí mật từ 1 - 100
        - Bây giờ bạn có 3 lượt chơi hãy đoán con số đó nào.''')
    
    secret = generate_secret_number(3, 6)
    game_play(3, secret)
    print(secret)



main()