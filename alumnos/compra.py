   
class carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito
    
    def calcular_total(self):
        total = 0
        for key, value in self.carrito.items():
            total += value['cantidad'] * value['precio']
        return total

    def agregar(self, producto):
        if producto.codigo not in self.carrito.keys():
            self.carrito[producto.codigo] = {
                'codigo': producto.codigo,
                'precio': producto.precio,
                'cantidad': 1,
                'total': producto.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key == producto.codigo:
                    value['cantidad'] = value['cantidad'] + 1
                    value['precio'] = producto.precio
                    value['total'] = value['cantidad'] * producto.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True  

    def eliminar(self, producto):
        id= producto.codigo
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        for key, value in self.carrito.items():
                if key == producto.codigo:
                    value['cantidad'] = value['cantidad'] - 1
                    value['precio'] = producto.precio  # Cambio realizado aquí
                    value['total'] = value['total'] + producto.precio
                    break
        self.guardar_carrito()

    def limpiar(self):
        self.session['carrito']={}
        self.session.modified= True