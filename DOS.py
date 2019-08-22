entrada1="a"
salida1="f"

cambio=str.maketrans(entrada1,salida1)
str="Ana"
print(str.translate(cambio))