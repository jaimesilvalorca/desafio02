from pizza import Pizza


print("Atributos de clase:")
print("Ingredientes cárnicos:", Pizza.ingredientes_carnicos)
print("Ingredientes vegetales:", Pizza.ingredientes_vegetales)
print("Tipos de masa:", Pizza.tipos_de_masa)
print()


print("¿'salsa de tomate' está presente en la lista ['salsa de tomate', 'salsa bbq']?")
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))
print()


pizza_pedido = Pizza()
pizza_pedido.hacer_pedido()


print("Ingredientes y tipo de masa de la pizza:")
print("Ingrediente de carne:", pizza_pedido.ingrediente_proteico)
print("Primer ingrediente vegetal:", pizza_pedido.ingrediente_vegetal_1)
print("Segundo ingrediente vegetal:", pizza_pedido.ingrediente_vegetal_2)
print("Tipo de masa:", pizza_pedido.tipo_de_masa)
print("¿Es una pizza válida?", pizza_pedido.es_valida)
print()


print("¿Es la clase Pizza una pizza válida?")
print(Pizza.es_valida)
