def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    parsedProblem = [
        dict(zip(["operand1", "operator", "operand2"], x.split()))
        for x in problems
    ]

    #Error Checking
    for problem in parsedProblem:
        if problem["operator"] not in "-+":
            return "Error: Operator must be '+' or '-'."

        if not problem["operand1"].isdecimal(
        ) or not problem["operand2"].isdecimal():
            return "Error: Numbers must only contain digits."

        problem["max_length"] = max(
            [len(problem["operand1"]),
             len(problem["operand2"])])

        if problem["max_length"] > 4:
            return "Error: Numbers cannot be more than four digits."

        if solve == True:
            problem["result"] = calc(problem)

    arranged_problems = ""
    arranged_problems += "    ".join([
        f"{int(x['operand1']):{x['max_length'] + 2}d}" for x in parsedProblem
    ]) + "\n"

    arranged_problems += "    ".join([
        f"{x['operator']} {int(x['operand2']):{x['max_length']}d}"
        for x in parsedProblem
    ]) + '\n'

    arranged_problems += "    ".join(
        [str('-' * (x["max_length"] + 2)) for x in parsedProblem])

    if solve == True:
        arranged_problems += '\n' + "    ".join(
            [f"{x['result']:{x['max_length'] + 2}d}" for x in parsedProblem])

    return arranged_problems


def calc(problem):
    if problem["operator"] == "+":
        return int(problem["operand1"]) + int(problem["operand2"])
    else:
        return int(problem["operand1"]) - int(problem["operand2"])
