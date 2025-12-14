import pathlib
import os
import sys
import subprocess


def find_notebooks(target_dir: str) -> list[str]:
    root = pathlib.Path(__file__).parent.parent.resolve()
    target_dir = os.path.join(root, target_dir)
    print(f"Target directory: {target_dir}")

    notebooks_to_convert = [
        os.path.join(root, file)
        for root, _, files in os.walk(target_dir)
        for file in files
        if file.startswith("notebook") and file.endswith(".py")
    ]
    return notebooks_to_convert


def create_notebooks(target_dir: str) -> list[str]:
    notebooks_to_convert = find_notebooks(target_dir)
    notebooks_converted = []
    for file in notebooks_to_convert:
        subprocess.run(["jupytext", "--to", "ipynb", "--execute", file])
        ipynb_file = pathlib.Path(file).with_suffix(".ipynb")
        notebooks_converted.append(ipynb_file)
    return notebooks_converted


if __name__ == "__main__":
    print(
        "This script should collect all .py files that should be converted to notebooks"
    )
    print(
        "Please provide the relative directory path from the project root as an command line argument, default will be src."
    )
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "src"
    notebooks_converted = create_notebooks(target_dir)
