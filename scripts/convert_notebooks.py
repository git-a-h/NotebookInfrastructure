import pathlib
import os 
import sys
import subprocess


if __name__ == '__main__':
    print('This script should collect all .py files that should be converted to notebooks')
    print('Please provide the relative directory path from the project root as an command line argument, default will be src.')

    root = pathlib.Path(__file__).parent.parent.resolve()
    target_dir = os.path.join(root, sys.argv[1]) if len(sys.argv) > 1 else os.path.join(root, 'src')
    print(f'Target directory: {target_dir}')

    notebooks_to_convert = [os.path.join(root,file) for root, _, files in os.walk(target_dir) for file in files if file.startswith('notebook') and file.endswith('.py')]
    for notebook in notebooks_to_convert:
        subprocess.run(['jupytext', '--to', 'ipynb', '--execute', notebook])
