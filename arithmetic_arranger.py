##########Helpers ###############
def check_char(string):
    i = 0
    for char in string:
        i += 1
        if char not in [str(i) for i in range(10)]:
            return "A"
    if i > 4:
        return "B"

def format_prob(prob_list):

    if prob_list[1] == "+":
        total = int(prob_list[0]) + int(prob_list[2])
        total = str(total)

    if prob_list[1] == "-":
        total = int(prob_list[0]) - int(prob_list[2])
        total = str(total)
    
    if len(prob_list[0]) > len(prob_list[2]):
        space_no = len(prob_list[0]) - len(prob_list[2]) + 1
        numer_value = (2*" ") + prob_list[0] + 4 * " "
        denom_values = prob_list[1] + (space_no* " ") + prob_list[2] + 4 * " "
        dash = (len(numer_value) -4) * "-" + 4 * " "

        space_no_total = len(prob_list[0])  - len(total) + 2
        total = space_no_total * " " + total + 4 *" "

        return (numer_value, denom_values, dash, total)

    if len(prob_list[0]) <= len(prob_list[2]):
        space_no = len(prob_list[2]) - len(prob_list[0]) + 2
        numer_value = (space_no * " ") + prob_list[0] + 4 * " "
        denom_values = prob_list[1] + " " + prob_list[2] + 4 * " "
        dash = (len(numer_value) -4) * "-" + 4 * " "
        
        space_no_total = len(prob_list[2])  - len(total) + 2
        total = space_no_total * " " + total + 4 *" "
        return (numer_value, denom_values, dash, total)


######Main function##########
def arithmetic_arranger(problems, total = False):

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        problem = problem.split()
        if problem[1] != "+" and problem[1] != "-":
            return "Error: Operator must be '+' or '-'."
        if check_char(problem[0]) == "A" or check_char(problem[2]) == "A":
            return "Error: Numbers must only contain digits."
        if check_char(problem[0]) == "B" or check_char(problem[2]) == "B":
            return "Error: Numbers cannot be more than four digits."

    format_list = []
    for problem in problems:
        problem = problem.split()
        format_tuple = format_prob(problem)
        format_list.append(format_tuple)
    

    format_list = list(zip(*format_list))
    if total == True:
        arranged_problems = (''.join(list(format_list[0]))).rstrip() + '\n' + (''.join(list(format_list[1]))).rstrip() + '\n' + (''.join(list(format_list[2]))).rstrip() + '\n' + (''.join(list(format_list[3]))).rstrip()
    
    if total == False:
        arranged_problems = (''.join(list(format_list[0]))).rstrip() + '\n' + (''.join(list(format_list[1]))).rstrip() + '\n' + (''.join(list(format_list[2]))).rstrip()

    return arranged_problems