# Practica 3 - Tienda Online

**Autor:** Mauro Jacobo

## Descripción
Aplicación de consola desarrollada en Python que simula una tienda online usando programación orientada a objetos. Permite registrar clientes y administradores, gestionar un catálogo de productos (normales, electrónicos y ropa), realizar pedidos con control de stock y consultar el histórico de pedidos de cada usuario.

## Estructura del proyecto
```
dockerfile
.dockerignore
requirements.txt
src/
  main.py
  models/
  Services/
```

## Ejecución sin Docker
```bash
cd src
python main.py
```

## Docker

### Construir la imagen
```bash
docker build -f dockerfile -t tienda-online:1.0 .
```

### Ejecutar el contenedor
```bash
docker run --rm tienda-online:1.0
```

### Descargar la imagen publicada en Docker Hub
```bash
docker pull jrm231/tienda-online:1.0
docker run --rm jrm231/tienda-online:1.0
```

Imagen: https://hub.docker.com/r/jrm231/tienda-online

### Variables de entorno
No aplica: la aplicación no utiliza variables de entorno. El dockerfile define PYTHONDONTWRITEBYTECODE y PYTHONUNBUFFERED solo para el funcionamiento de Python dentro del contenedor.

### Salida esperada
Al ejecutar el contenedor se imprime, por este orden:

1. PRODUCTOS: el inventario inicial (5 productos).
2. PEDIDOS: tres pedidos, de Rodrigo (115.0 €), Marcos (136.5 €) y Nicolas (55.4 €).
3. HISTÓRICO DE RODRIGO: su pedido de 115.0 €.
4. STOCK ACTUALIZADO: el inventario tras los pedidos (por ejemplo, FC 26 pasa de 15 a 14 unidades).

Los identificadores (ID) cambian en cada ejecución porque se generan con uuid.

## Flujo de trabajo
Se trabaja con ramas feature/ y Pull Requests hacia main.
