import re

archivo = open('image1.xml','r')
texto = archivo.read()

patronCaja = re.compile('bndbox')
resultados = patronCaja.finditer(texto)
resultados = [_ for _ in resultados]

contenedores = []

while(resultados):
    inicio = resultados.pop(0).span()[0]
    fin = resultados.pop(0).span()[1]
    contenedores.append((inicio, fin))


rectangulos = []
for contenedor in contenedores:
    (inicio, fin) = contenedor
    lugarDeBusqueda = texto[inicio:fin]
    patronxmin = re.search(r'<xmin>\d{1,}<\/xmin>',lugarDeBusqueda)
    patronxminNumero = re.search(r'\d{1,}', patronxmin.group())
    xmin = patronxminNumero.group()
    patronymin = re.search(r'<ymin>\d{1,}<\/ymin>',lugarDeBusqueda)
    patronyminNumero = re.search(r'\d{1,}', patronymin.group())
    ymin = patronyminNumero.group()
    patronxmax = re.search(r'<xmax>\d{1,}<\/xmax>',lugarDeBusqueda)
    patronxmaxNumero = re.search(r'\d{1,}', patronxmax.group())
    xmax = patronxmaxNumero.group()
    patronymax = re.search(r'<ymax>\d{1,}<\/ymax>',lugarDeBusqueda)
    patronymaxNumero = re.search(r'\d{1,}', patronymax.group())
    ymax = patronymaxNumero.group()
    rectangulos.append( (xmin, ymin, xmax, ymax) )

print(rectangulos)