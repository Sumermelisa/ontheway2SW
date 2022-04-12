print(("*" * 30) + "\nSOULMATE CALCULATOR\n" + ("*" * 30))





ad1 = input("isminiz:")
ad2 = input("crush'ınızın ismi:")

love = len(ad1) + len(ad2)

if len(ad1) > len(ad2):
    love -= 5
else:
    love += 3

love *=42
love = love / (100 + len(ad2))

love =10 if love > 10 else round(love,0)

print("{} ve {} soulmate yüzdesi {}"
.format(ad1,ad2,love))