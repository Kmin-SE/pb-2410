# Viết chương trình cho phép nhập vào nickname của một người. 
# Và hãy in ra lời chào với người ấy theo định dạng: “Hi, <nickname>!”.

nickname = input("Nhap nickname: ")

# print("Hi, ", nickname, "!", sep="") # sep: ký tự ngăn cách

# res = "Hi, " + nickname + "!" # Cộng chuỗi
# print(res)

print(f"Hi, {nickname}!") # format string 
