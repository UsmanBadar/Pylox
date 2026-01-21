import sys, os
from pathlib import Path

def generate_ast():

    if len(sys.argv) > 1:
        dir_name = sys.argv[1]
    else:
        print("Usage: generate_ast <output directory>")
        sys.exit(1)

    types = [
        "Binary   : Expr left, Token operator, Expr right",
        "Grouping : Expr expression",
        "Literal  : Object value",
        "Unary    : Token operator, Expr right"

    ]
   
    define_ast(dir_name, "Expr", types)



def define_ast(output_dir, base_name, types):
    dir_path = Path(output_dir)
    file_path = dir_path / "expr.py"

    os.makedirs(dir_path, exist_ok=True)

    header = (
    '"""Generated AST classes for Expr."""\n\n'
    'from __future__ import annotations\n'
    'from dataclasses import dataclass\n'
    'from typing import Any\n'
)
    


    try:
        with open(file_path, "w", encoding = "utf-8") as file:
            file.write(header)
            for t_item in types:
                t_item_splitted = t_item.split(":")
                classname = t_item_splitted[0].strip()
                fields_str = t_item_splitted[1].strip()
                fields_list = fields_str.split(",")
                field_names_list = [field_item.strip().split(" ")[1].strip() for field_item in fields_list]
                field_names_str = ", ".join(field_names_list)
                class_line = f"\n\nclass {classname}:\n"
                init_line = f"\tdef __init__(self, {field_names_str}):\n"
                body = ""
                for name in field_names_list:
                    body += f"\t\tself.{name} = {name}\n"
                class_code_str = class_line + init_line + body
                file.write(class_code_str)




    except Exception as e:
        print(f"File not found. error: {e}")
        sys.exit(1)





if __name__ == "__main__":
    generate_ast()


