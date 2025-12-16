import convert_notebooks 
import shutil
import os
import pathlib


def create_notebook_dir() -> str:
    root = pathlib.Path(__file__).parent.parent.resolve()
    notebook_dir = os.path.join(root, "notebooks")
    os.makedirs(notebook_dir, exist_ok=True)
    return notebook_dir

if __name__ == "__main__":
    notebooks_converted = convert_notebooks.main()
    notebook_dir = create_notebook_dir()
    for notebook in notebooks_converted:
        shutil.move(notebook, os.path.join(notebook_dir,os.path.basename(notebook.name)))
        