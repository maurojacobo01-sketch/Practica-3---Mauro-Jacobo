from Services.Tienda_service import TiendaService


def main():
    tienda = TiendaService()

    # Registrar usuarios
    cliente1 = tienda.registrar_usuario("cliente", "Rodrigo", "rodrigo@uie.edu", "Calle Príncipe, Vigo")
    cliente2 = tienda.registrar_usuario("cliente", "Marcos", "marcos@uie.edu", "Calle Urzáiz, Vigo")
    cliente3 = tienda.registrar_usuario("cliente", "Nicolas", "nicolas@uie.edu", "Rúa do Areal, Vigo")
    tienda.registrar_usuario("administrador", "Mauro", "mauro@uie.edu")

    # Añadir productos
    producto1 = tienda.anadir_producto("electronico", "Videojuego - FC 26", 70.0, 15, garantia=2)
    producto2 = tienda.anadir_producto("electronico", "Videojuego - Zelda: Tears of the Kingdom", 60.0, 10, garantia=2)
    producto3 = tienda.anadir_producto("ropa", "Reloj deportivo Casio", 45.0, 20, talla="Ajustable", color="Negro")
    producto4 = tienda.anadir_producto("normal", "Cajetilla de tabaco Marlboro", 5.5, 50)
    producto5 = tienda.anadir_producto("normal", "Cajetilla de tabaco Camel", 5.2, 40)

    # Listar inventario
    print("PRODUCTOS:")
    tienda.listar_productos()

    # Realizar pedidos
    pedido1 = tienda.realizar_pedido(cliente1.id, [(producto1.id, 1), (producto3.id, 1)])
    pedido2 = tienda.realizar_pedido(cliente2.id, [(producto2.id, 2), (producto4.id, 3)])
    pedido3 = tienda.realizar_pedido(cliente3.id, [(producto5.id, 2), (producto3.id, 1)])

    # Mostrar pedidos
    print("\nPEDIDOS:")
    print(pedido1)
    print(pedido2)
    print(pedido3)

    # Histórico de pedidos de Rodrigo
    print("\nHISTÓRICO DE RODRIGO:")
    for pedido in tienda.listar_pedidos_usuario(cliente1.id):
        print(pedido)

    # Stock actualizado
    print("\nSTOCK ACTUALIZADO:")
    tienda.listar_productos()


if __name__ == "__main__":
    main()