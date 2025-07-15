#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video],...}

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock]..}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def menu():
    print('***MENÚ PRINCIPAL***')
    print('1. Stock marca.')
    print('2. Busqueda por precio.')
    print('3. Listado de productos.')
    print('4. Salir.')

def stock_marca():
    modelo = ''
    cant = {}
    marca = input('Ingrese marca a consultar: ').title() #no pude sumar ni ingresar HP
    for clave, valor in productos.items():
        if marca == valor[0]:
            modelo = clave
            for clave, valor in stock.items():
                if modelo == clave:
                    cant[clave] = stock[clave]
                    total = 0 + valor[1]
                    print(f'El stock es: {total}')

def busqueda_precio():
    while True:
        try:
            p_min = int(input('Ingrese el precio mínimo: '))
            p_max = int(input('Ingrese el precio máximo: '))    
            if p_min < 249990:
                print('No hay notebooks en ese rango de precio')
            elif p_max > 749990:
                print('No hay notebooks en ese rango de precio')  
            print(f'Los de noteboos entre los precios consultas son: ')            
        except ValueError:
            print('Debe ingresar valores enteros!!')

#marca - modelo - ram - GB de DD
def ordenar_productos():
    print('------Listado de Notebooks Ordenados------')
    for clave, valor in productos.items():        
        print(f'{valor[0]} - {clave} - {valor[2]} - {valor[4]}')
    print('------------------------------------------')        

while True:
    menu()
    try:
        opc = int(input('Ingrese una opción: '))
        if opc == 1:            
            stock_marca()   
        elif opc == 2:
            busqueda_precio()
        elif opc == 3:
            ordenar_productos()
        elif opc == 4:
            print('Porgrama finalizado.')
            break
        else:
            print('Debe seleccionar una opción válida!!')
    except ValueError:
        print('Debe seleccionar una opción válida!!')