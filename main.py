from sympy import factorint

def asal_carpanlar(n):
    factors = factorint(n) #Verilen n sayısını asal çarpanlarına ayırır ve bir sözlük olarak döndürür. Bu sözlükte anahtarlar asal sayılar, değerler ise bu asal sayıların üsleridir.
    factors_str = '*'.join([f'{p}^{e}' for p, e in factors.items()]) #Her bir asal çarpanı ve üssünü p^e formatında birleştirir ve bunları * ile ayırır.
    return f'{n} = {factors_str}' #Sonucu belirtilen formatta döndürür.

sayi = int(input("Pozitif bir tam sayı giriniz: "))
print(asal_carpanlar(sayi))
