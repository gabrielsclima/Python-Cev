from datetime import date
print("-- Analisador de ano bissexto (socorro estou morrendo de sono) --")

ano = int(input("Ano para analisar (0 para ano atual): "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto")

else:
    print(f"O ano {ano} não é bissexto")
