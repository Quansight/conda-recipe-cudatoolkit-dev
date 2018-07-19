#! /usr/bin/env python
import subprocess
class Bash2Py(object):
  __slots__ = ["val"]
  def __init__(self, value=''):
    self.val = value

def GetVariable(name, local=locals()):
  if name in local:
    return local[name]
  if name in globals():
    return globals()[name]
  return None

def Make(name, local=locals()):
  ret = GetVariable(name, local)
  if ret is None:
    ret = Bash2Py(0)
    globals()[name] = ret
  return ret

def Array(value):
  if isinstance(value, list):
    return value
  if isinstance(value, basestring):
    return value.strip().split(' ')
  return [ value ]

for Make("f").val in Array(CONDA_PREFIX.val)+Array("/pkgs/cudatoolkit-dev/bin"):
    subprocess.call(["unlink",str(CONDA_PREFIX.val)+"/bin/"+str(f.val)],shell=True)
del CUDA_HOME
for Make("f").val in Array(CONDA_PREFIX.val)+Array("/pkgs/cudatoolkit-dev-9.2-0/lib64"):
    subprocess.call(["unlink",str(CONDA_PREFIX.val)+"/lib/"+str(f.val)],shell=True)

"""
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
"""
