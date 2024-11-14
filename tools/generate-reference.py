#!/usr/bin/env python3

import argparse
import os


def extract_comments_and_code(file_path):
    comments = []
    code = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
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
            main_scripts = []
            additional_files = []

            for file in files:
                file_path = os.path.join(root, file)

                if (
                    file.endswith(".sh")
                    or file.endswith(".py")
                    or file.endswith(".vim")
                    or file.endswith("rc")
                ):
                    main_scripts.append(file_path)
                elif file == "executable" or file.endswith(
                    (".png", ".jpg", ".jpeg", ".gif", ".bin", ".exe")
                ):
                    continue
                else:
                    additional_files.append(file_path)

            for script in main_scripts:
                comments, code = extract_comments_and_code(script)
                script_name = os.path.basename(script)

                ref_file.write(f"## {script_name}\n\n")

                if comments:
                    if use_gh_flag:
                        ref_file.write("> **COMENTARIOS**\n")
                    elif use_cli_flag:
                        ref_file.write("> [!NOTE]\n")

                    for comment in comments:
                        ref_file.write(">\n")
                        ref_file.write(f"{comment}\n")
                    ref_file.write("\n")

                extension = script_name.split(".")[-1]
                if extension == "py":
                    extension = "python"

                ref_file.write(f"```{extension}\n")
                ref_file.writelines(code)
                ref_file.write("```\n")

            if additional_files:
                ref_file.write(
                    f"> **Recursos adicionales en dir: {os.path.basename(root)}**\n\n"
                )
                for additional_file in additional_files:
                    additional_file_name = os.path.basename(additional_file)
                    extension = additional_file_name.split(".")[-1]
                    ref_file.write(f"*{additional_file_name}*\n\n")
                    ref_file.write(f"```{extension}\n")
                    with open(
                        additional_file, "r", encoding="utf-8", errors="ignore"
                    ) as f:
                        content = f.readlines()
                    ref_file.writelines(content)
                    ref_file.write("\n```\n\n")


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
    try:
        make_reference(scripts_directory, args.gh, args.cli)
        print("\n✔ Referencia generadas")
        print("1. Puedes exportarlas a PDF con tu parser favorito.")
        print("2. O hacer push y verlas en GitHub :).\n")
    except Exception as e:
        print(f"Ocurrió un error durante la generación de referencias: {e}")
