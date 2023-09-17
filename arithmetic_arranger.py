def arithmetic_arranger(problems, result=False):
    # Comprueba si hay más de 5 problemas. Si es así, devuelve un error.
    if len(problems) > 5:
        return "Error: Too many problems."

    # Crea un diccionario de operadores y sus funciones correspondientes.
    ops = {
        "+": lambda pair: str(pair[0] + pair[1]),
        "-": lambda pair: str(pair[0] - pair[1]),
    }

    # Inicializa las listas que contendrán los problemas ordenados, las líneas superior e inferior, las líneas de separación y los resultados.
    arranged_problems = []
    top = []
    bottom = []
    lines = []
    results = []

    # Itera sobre los problemas y ordena cada uno.
    for problem in problems:
        chunks = problem.split()
        max_len = len(max(chunks, key=len))

        # Comprueba si todos los números son dígitos.
        if not all([i.isnumeric() for i in chunks[::2]]):
            return "Error: Numbers must only contain digits."

        # Comprueba si el operador es '+' o '-'.
        elif chunks[1] not in ops.keys():
            return "Error: Operator must be '+' or '-'."

        # Comprueba si los números tienen más de 4 dígitos.
        elif max_len > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calcula la longitud de la línea.
        line_len = max_len + 2

        # Crea la línea de separación.
        line = "-" * line_len

        # Alinea los números a la derecha.
        first_num = chunks[0].rjust(line_len, " ")
        second_num = f"{chunks[1]}{' ' * (line_len - len(chunks[2]) - 1)}{chunks[2]}"

        # Agrega los números y la línea de separación a las listas correspondientes.
        top.append(first_num)
        bottom.append(second_num)
        lines.append(line)

        # Si se solicita el resultado, calcula el resultado de la operación y lo agrega a la lista de resultados.
        if result:
            res = ops[chunks[1]]([int(i) for i in chunks[::2]])
            results.append(f"{res.rjust(line_len, ' ')}")

    # Crea una cadena con los problemas ordenados, separados por líneas en blanco.
    arranged_problems = "\n".join(["    ".join(i) for i in (top, bottom, lines)])

    # Si se solicita el resultado, agrega una línea en blanco y los resultados al final de la cadena.
    if results:
        arranged_problems += "\n" + "    ".join(results)

    # Devuelve la cadena con los problemas ordenados.
    return arranged_problems


print(
    arithmetic_arranger(["32 + 698", "3801 - 2", "23 + 54", "80 - 45", "44 - 12"], True)
)
