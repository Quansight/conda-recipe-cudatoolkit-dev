import os
from pathlib import Path

conda_prefix = os.environ['CONDA_PREFIX']
conda_prefix_bin = os.path.join(conda_prefix, 'bin')
cudatoolkit_home = Path(conda_prefix) / 'pkgs' / 'cudatoolkit-dev-9.2-0'
os.environ['CUDA_HOME'] = str(cudatoolkit_home)
cudatoolkit_bin = cudatoolkit_home / 'bin'

for file_name in os.listdir(cudatoolkit_bin):
    full_file_path = os.path.join(cudatoolkit_bin, file_name)
    if not os.path.islink(full_file_path):
        os.symlink(full_file_path, conda_prefix_bin)
    else:
        pass


ld_library_path = os.path.join(conda_prefix, 'lib')
cudatoolkit_libraries = cudatoolkit_home / 'lib64'

for file_name in os.listdir(cudatoolkit_libraries):
    full_file_path = os.path.join(cudatoolkit_libraries, file_name)
    if not os.path.islink(full_file_path):
        os.symlink(full_file_path, ld_library_path)
    else:
        pass
