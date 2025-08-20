endereço_ip = input()
novo_ip = ""
for i in endereço_ip:
    if i == ".":
        novo_ip += "[.]"
    else:
        novo_ip += i
print(novo_ip)