# programa que convierte de decimal a binario

dec = input("Digite numero-> ")
dec = int(dec)
bin = []
while dec >= 1:
    bin.append(dec % 2)
    dec = round(dec // 2)

bin.reverse()

for num in bin:
    print(num, end='')
print("")
