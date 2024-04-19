import os
import subprocess

def process(program):
    fpc_path = "/usr/bin/fpc"
    pascal_file = "/home/panton8/A.pas"

    with open(pascal_file, 'w') as file:
        a = file.read()
        print(a)

    with open(pascal_file, 'w') as file:
        file.write(program)

    compile_command = [fpc_path, pascal_file]

    # Выполнение компиляции
    process_compile = subprocess.Popen(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output_compile, error_compile = process_compile.communicate()

    # Вывод результатов компиляции
    if process_compile.returncode == 0:
        compiled_program = pascal_file.replace(".pas", "")
        compiled_program_exe = compiled_program + ".out"  # добавляем расширение исполняемого файла

        # Выполнение скомпилированной программы
        if os.path.exists(compiled_program_exe):
            process_execute = subprocess.Popen([compiled_program_exe], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output_execute, error_execute = process_execute.communicate()

            # Вывод результата выполнения программы
            print("Результат выполнения программы:")
            print(output_execute.decode("utf-8"))
        else:
            print("Ошибка выполнения: исполняемый файл не найден.")
    else:
        print("Ошибка компиляции:")
        print(error_compile.decode("utf-8"))
