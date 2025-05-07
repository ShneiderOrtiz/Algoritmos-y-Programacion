lista = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}
valores_unicos = []

for valor in lista.values():
    if valor not in valores_unicos:
        valores_unicos.append(valor)

print(valores_unicos)

