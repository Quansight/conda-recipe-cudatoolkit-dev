from __future__ import print_function
import os
import shutil
from pathlib import Path
import stat


def set_chmod(file_name):
    # Do a simple chmod +x for a file within python
    st = os.stat(file_name)
    os.chmod(file_name, st.st_mode | stat.S_IXOTH)


def create_dir(new_dir):
    try:
        os.makedirs(new_dir)
    except FileExistsError:
        pass


def copy_files(src, dst):
    try:
        if (os.path.isfile(src)):
            set_chmod(src)
            shutil.copy(src, dst)
    except FileExistsError:
        pass


def _main():

    prefix_dir_path = Path(os.environ['PREFIX'])
    prefix_bin_dir_path = prefix_dir_path / 'bin'
    conda_prefix_path = Path(os.environ['CONDA_PREFIX'])
    print('---------------', prefix_dir_path)
    print('---------------', conda_prefix_path)
    # Create activated.d and deactivate.d directories
    activate_dir_path = conda_prefix_path / 'etc' / 'conda' / 'activate.d'
    deactivate_dir_path = conda_prefix_path / 'etc' / 'conda' / 'deactivate.d'
    create_dir(prefix_bin_dir_path)
    create_dir(activate_dir_path)
    create_dir(deactivate_dir_path)
    # Copy cudatoolkit-dev-activate and cudatoolkit-dev-deactivate
    # to activate.d and deactivate.d directories

    recipe_dir_path = Path(os.environ['RECIPE_DIR'])
    scripts_dir_path = recipe_dir_path / 'scripts'
    activate_scripts_path = scripts_dir_path / 'activate'
    deactivate_scripts_path = scripts_dir_path / 'deactivate'

    for file_name in os.listdir(activate_scripts_path):
        full_file_name = os.path.join(activate_scripts_path, file_name)
        copy_files(full_file_name, activate_dir_path)
    for file_name in os.listdir(deactivate_scripts_path):
        full_file_name = os.path.join(deactivate_scripts_path, file_name)
        copy_files(full_file_name, deactivate_dir_path)
    # Copy cudatoolkit-dev-post-install.py to $PREFIX/bin
    src = recipe_dir_path / 'cudatoolkit-dev-post-install.py'
    dst = prefix_bin_dir_path
    copy_files(src, dst)

    print("<<<<<<<<<<<<<<<<<<<<<<<<<Listing Different Files>>>>>>>>>>>>>>>>>>>>")
    print(os.listdir(activate_dir_path))
    print(os.listdir(deactivate_dir_path))
    print(os.listdir(prefix_bin_dir_path))


if __name__ == "__main__":
    _main()
