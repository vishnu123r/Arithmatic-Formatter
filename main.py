# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger, format_prob, check_char
from unittest import main


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main(module='test_module', exit=False)