#!/usr/bin/env python3
import os
import argparse


def extract_comments_and_code(file_path):
    comments = []
    code = []

    with open(file_path, "r") as f:
        for line in f:
            if line.strip().startswith("# >") and not line.strip().startswith("#!"):
                comments.append(line.strip()[2:])
            else:
                code.append(line)

    return comments, code


def make_reference(scripts_dir, use_gh_flag, use_cli_flag):
    with open("REFERENCE.md", "w") as ref_file:
        ref_file.write("# Scripts Reference\n\n")
        for root, dirs, files in os.walk(scripts_dir):
            for file in files:
                if file.endswith(".sh") or file.endswith(".py"):
                    file_path = os.path.join(root, file)

                    comments, code = extract_comments_and_code(file_path)

                    ref_file.write(f"## {file}\n\n")

                    if comments:
                        if use_gh_flag:
                            ref_file.write("> **COMENTARIOS**\n\n")
                        elif use_cli_flag:
                            ref_file.write("> [!NOTE]\n")

                        for comment in comments:
                            ref_file.write(">\n")
                            ref_file.write(f" {comment}\n")
                        ref_file.write("\n")

                    extension = file.split(".")[-1]

                    if extension == "py":
                        extension = "python"

                    ref_file.write(f"```{extension}\n")
                    ref_file.writelines(code)
                    ref_file.write("```\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ejecutar desde el directorio principal, USA SIEMPRE --cli",
        epilog="\nEjemplo: ./generate-reference.py --cli.",
    )
    parser.add_argument(
        "--gh", action="store_true", help="Generar referencias para Github Actions"
    )
    parser.add_argument(
        "--cli", action="store_true", help="Generar referencias para verlas localmente"
    )

    args = parser.parse_args()

    if not (args.gh or args.cli):
        parser.print_help()
        exit(1)

    scripts_directory = "./scripts"
    make_reference(scripts_directory, args.gh, args.cli)
    print(
        "Referencia generadas, puedes exportarlas a pdf con tu parser favorito\nO hacer push y verlos en github :)."
    )
