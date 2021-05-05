import re


def arithmetic_arranger(problems, getanswer=False):
    # too many problems

    if len(problems) > 5:
        return "Error: Too many problems."

    firstNum = ""
    secondNum = ""
    lines = ""
    result = ""

    for item in problems:
        if re.search("[^\s0-9.+-]", item):
            if re.search("[*]", item) or re.search("[/]", item):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        leftOper = item.split(" ")[0]
        rightOper = item.split(" ")[2]
        operator = item.split(" ")[1]
        if len(leftOper) >= 5 or len(rightOper) >= 5:
            return "Error: Numbers cannot be more than four digits."

        answer = ""
        if operator == "+":
            answer = str(int(leftOper) + int(rightOper))

        elif operator == "-":
            answer = str(int(leftOper) - int(rightOper))

        lengthOf = max(len(leftOper), len(rightOper)) + 2
        top = str(leftOper).rjust(lengthOf)
        bottom = operator + str(rightOper).rjust(lengthOf-1)
        line = ""
        for s in range(lengthOf):
            line += "-"
        solution = str(answer).rjust(lengthOf)

        if item != item[-1]:
            firstNum += top + "    "
            secondNum += bottom + "    "
            lines += line + "    "
            result += solution + "    "
        else:
            firstNum = firstNum.rstrip()
            secondNum = secondNum.rstrip()
            lines = lines.rstrip()
            result = result.rstrip()

    if getanswer:
        answ = firstNum.rstrip() + "\n" + secondNum.rstrip() + "\n" + lines.rstrip() + "\n" + result.rstrip()
        # print(type(answ))
        return answ
    else:
        answ = firstNum.rstrip() + "\n" + secondNum.rstrip() + "\n" + lines.rstrip()
        return answ



# # TEST CASES
# # print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# # print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
# # print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# # print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
# # print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40","653 + 87"]))
# # print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
# # print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
# # print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
# # print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))
# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# # print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))

