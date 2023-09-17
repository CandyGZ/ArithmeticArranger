def arithmetic_arranger(problems, show_results=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = []
    # results_line = None

    if not show_results:
        results_line = list(" ") * len(problems)

        for problem, result in zip(problems, results_line):
            components = problem.split()
            operand1, operator, operand2 = components

            if operator not in ("+", "-"):
                return "Error: Operator must be '+' or '-'"

            if not operand1.isdigit() or not operand2.isdigit():
                return "Error: Numbers must only contain digits"

            if len(operand1) > 4 or len(operand2) > 4:
                return "Error: Numbers cannot be more than four digits"

            max_length = max(len(operand1), len(operand2), len(result))

            line1 = operand1.rjust(max_length + 2)
            line2 = operator + operand2.rjust(max_length + 1)
            dashes = "-" * (max_length + 2)
            # result_str = result.rjust(max_length + 2)

            arranged_problems.append((line1, line2, dashes))

        lines = list(map(list, zip(*arranged_problems)))
        arranged = "\n".join(["    ".join(line) for line in lines])
        arranged = arranged.replace("    ", " " * 4)

        output = ""
        for line in lines:
            output_line = "    ".join(line).rstrip() + "\n"
            output += output_line

        return output

    if show_results:
        results_line = list(
            map(lambda problem: str(eval(problem.replace(" ", ""))), problems)
        )

        for problem, result in zip(problems, results_line):
            components = problem.split()
            operand1, operator, operand2 = components

            if operator not in ("+", "-"):
                return "Error: Operator must be '+' or '-'"

            if not operand1.isdigit() or not operand2.isdigit():
                return "Error: Numbers must only contain digits"

            if len(operand1) > 4 or len(operand2) > 4:
                return "Error: Numbers cannot be more than four digits"

            max_length = max(len(operand1), len(operand2), len(result))

            line1 = operand1.rjust(max_length + 2)
            line2 = operator + operand2.rjust(max_length + 1)
            dashes = "-" * (max_length + 2)
            result_str = result.rjust(max_length + 2)

            arranged_problems.append((line1, line2, dashes, result_str))

        lines = list(map(list, zip(*arranged_problems)))
        arranged = "\n".join(["    ".join(line) for line in lines])
        arranged = arranged.replace("    ", " " * 4)

        output = ""
        for line in lines:
            output_line = "    ".join(line).rstrip() + "\n"
            output += output_line

        return output


# Ejemplos de uso
problems1 = ["32 - 698", "1500 - 3801", "45 + 43", "123 + 49", "988 + 40"]
print(arithmetic_arranger(problems1, True))
