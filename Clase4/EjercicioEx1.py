notas = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
# Si Si Do Re Re Do Si La Sol Sol La Si Si La La
notas.insert(0,'Si')
notas.insert(1,'Si')
notas.insert(3,'Re')
notas.insert(5,'Do')
notas.pop(6)
notas.pop(6)
notas.insert(6,'Si')
notas.insert(7,'La')
notas.insert(9,'Sol')
notas.insert(13,'La')
notas.insert(14,'La')
print(notas)