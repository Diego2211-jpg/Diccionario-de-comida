comiditas = {
            "PIZZA": "Algo redondo hecho de pan que se le embarra salsa de tomate y se le coloca queso y algun ingrediente encima",
            "PASTA": "Un platillo con espaguettis y que los tienes que cocer para después sasonarlos como quieras",
            "SUSHI": "Un rollo de arroz envuelto con algas y relleno con pepino y normalmente camarón",
            "SANDWICH": "Dos panes uno encima del otro y que en medio suelen llevar jamón y queso" ,
            "TACOS": "Una tortilla ya sea de maiz o harina doblada con carne adentro",
            }
word = input("Escribe una comida que no conozcas bien (¡con mayúsculas!): ")

if word in comiditas.keys():
    print(comiditas[word])
else:
    print("Esta palababra no esta disponible")
