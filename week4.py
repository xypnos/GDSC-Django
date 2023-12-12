
def basic_operations(a, b):
    try:
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b
    except ZeroDivisionError:
        return {"error": "Division by zero"}
    except Exception as e:
        return {"error": str(e)}

    return {"addition": addition, "subtraction": subtraction, "multiplication": multiplication, "division": division}


def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent
        modulo = kwargs.get('modulo')
        if modulo is not None:
            result %= modulo
    except Exception as e:
        return {"error": str(e)}

    return {"result": result}
def apply_operations(operation_list):
    results = list(map(lambda x: x[0](*x[1]), operation_list))
    return results from math_operations import basic_operations, power_operation, apply_operations

result_basic = basic_operations(10, 5)
print("Basic Operations Result:", result_basic)

result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)

result_power_modulo = power_operation(2, 3, modulo=5)
print("Power Operation with Modulo Result:", result_power_modulo)

operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
]

result_apply = apply_operations(operations)
print("Apply Operations Result:", result_apply)
# script.py
from file_operations import list_files_in_directory, is_file_recently_updated, update_file, create_last_24hours_folder, move_files_to_last_24hours

current_directory = "."
files_to_update = [file for file in list_files_in_directory(current_directory) if is_file_recently_updated(file)]

create_last_24hours_folder()

for file in files_to_update:
    update_file(file, "Content updated!")

move_files_to_last_24hours(files_to_update)

