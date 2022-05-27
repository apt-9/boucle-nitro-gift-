import random 

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:
    nitrocode = ''

    for i in range(16):
        nitrocode = f"{nitrocode}{random.choice(caracteres)}"

    print(f"https://discord.gift/{nitrocode}")

    with open("nitros.txt", "a+") as nitroFile:

        nitroFile.write(f"https://discord.gift/{nitrocode}\n")

        nitroFile.close() 
