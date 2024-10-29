#!/usr/bin/env python3
import os
import shutil
import subprocess


def clear_bin_directory(bin_dir):
    for file in os.listdir(bin_dir):
        file_path = os.path.join(bin_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Clean: {file_path}")


def copy_scripts_to_bin(scripts_dir, bin_dir):
    for root, dirs, files in os.walk(scripts_dir):
        for file in files:
            if file.endswith(".sh") or file.endswith(".py"):
                script_name = os.path.splitext(file)[0]
                new_script_name = f"cps-{script_name}"
                original_script_path = os.path.join(root, file)
                new_script_path = os.path.join(bin_dir, new_script_name)

                if os.path.exists(new_script_path):
                    print(f"Advertencia: {new_script_path} ya existe, se renombrará.")
                    new_script_path = os.path.join(bin_dir, f"cps-{file}")

                shutil.copy(original_script_path, new_script_path)
                subprocess.run(["chmod", "+x", new_script_path])

                print(f"Build: {original_script_path} a {new_script_path}")


if __name__ == "__main__":
    scripts_directory = "./scripts"
    bin_directory = "./bin"

    os.makedirs(bin_directory, exist_ok=True)

    clear_bin_directory(bin_directory)

    copy_scripts_to_bin(scripts_directory, bin_directory)
