import os
from pathlib import Path

conda_prefix = os.environ['CONDA_PREFIX']
conda_prefix_bin = os.path.join(conda_prefix, 'bin')
cudatoolkit_home = Path(conda_prefix) / 'pkgs' / 'cudatoolkit-dev-9.2-0'
del os.environ['CUDA_HOME']
cudatoolkit_bin = cudatoolkit_home / 'bin'

for file_name in os.listdir(cudatoolkit_bin):
    full_file_path = os.path.join(conda_prefix_bin, file_name)
    if os.path.islink(full_file_path):
        os.unlink(full_file_path)

    else:
        pass

ld_library_path = os.path.join(conda_prefix, 'lib')
cudatoolkit_libraries = cudatoolkit_home / 'lib64'

for file_name in os.listdir(cudatoolkit_libraries):
    full_file_path = os.path.join(ld_library_path, file_name)
    if os.path.islink(full_file_path):
        os.unlink(full_file_path)
    else:
        pass
