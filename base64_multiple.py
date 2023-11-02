import base64

result = []
user_in = input("Enter the encoded text  :  ")
x = int (input("number of decode iterations  : "))
result.append(user_in)
for i in range(1,x+1,1) :
        user_dec = base64.b64decode(result[i-1])
        result.append(user_dec)
        user_dec=user_dec.strip()
        print("result of -", i, user_dec)