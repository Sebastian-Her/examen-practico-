from StackHanoi import Stack

print("\n¡Vamos a jugar a las torres de Hanoi!")

#Crear las pilas
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


#Configurar el juego
num_disks = int(input("¿Con cuántos discos quieres jugar? "))
while num_disks < 3:
    num_disks = int(input("Ingresa un número mayor o igual a 3\n"))
for i in range(num_disks, 0, -1):
    left_stack.push(i)
num_optimal_moves = (2 ** num_disks) - 1
print(f"\nLo más veloz que puedes resolver este juego es en {num_optimal_moves} movimientos")


#Obtener entrada del usuario
def get_input():
    choices = ['L', 'M', 'R']
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Escribe {letter} para {name}")
        user_input = input("Selecciona una pila: ").strip().upper()
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

        
#Jugando el juego
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n\n...Pilas actuales...")
    for stack in stacks:
        stack.print_items()
    while True:
        print("\n¿Desde qué pila quieres mover un disco?\n")
        from_stack = get_input()
        print("\n¿A qué pila quieres mover el disco?\n")
        to_stack = get_input()
        if from_stack.get_size() == 0:
            print("\n\nMovimiento no válido. Inténtalo de nuevo")
        elif (to_stack.get_size() == 0 or
            from_stack.peek() < to_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nMovimiento no válido. Inténtalo de nuevo")

print(f"\n\nCompletaste el juego en {num_user_moves} movimientos y el número óptimo de movimientos es {num_optimal_moves}.")