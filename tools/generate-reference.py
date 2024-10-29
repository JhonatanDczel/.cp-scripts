#!/usr/bin/env python3
import os


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


def make_reference(scripts_dir):
    with open("REFERENCE.md", "w") as ref_file:
        ref_file.write("# Scripts Reference\n\n")
        for root, dirs, files in os.walk(scripts_dir):
            for file in files:
                if file.endswith(".sh") or file.endswith(".py"):
                    file_path = os.path.join(root, file)

                    comments, code = extract_comments_and_code(file_path)

                    ref_file.write(f"## {file}\n\n")

                    if comments:
                        ref_file.write("> [!NOTE]\n")
                        for comment in comments:
                            ref_file.write(f">\n")
                            ref_file.write(f"{comment}\n")
                        ref_file.write("\n")

                    extension = file.split(".")[-1]

                    if extension == "py":
                        extension = "python"

                    ref_file.write(f"```{extension}\n")
                    ref_file.writelines(code)
                    ref_file.write("```\n\n")


if __name__ == "__main__":
    scripts_directory = "./scripts"
    make_reference(scripts_directory)
