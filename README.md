[![Build Status](https://travis-ci.org/Quansight/conda-recipe-cudatoolkit-dev.svg?branch=master)](https://travis-ci.org/Quansight/conda-recipe-cudatoolkit-dev)

# conda-recipe-cudatoolkit-dev
conda recipe for a "full" cudatoolkit package


## Build and Install the package 

    conda create -n cudatest python=3.6 conda-build numba conda-verify -y

    source activate cudatest 

    conda build condarecipe9.2/

    conda install --use-local $CONDA_PREFIX/conda-bld/linux-64/cudatoolkit-dev-9.2-0.tar.bz2 -v


## Testing the package

To confirm that the compiler was properly installed, run:

    which nvcc

This returns the installation path

    /home/ubuntu/miniconda3/envs/cudatest/bin/nvcc  

To find the compiler's version, run:

    nvcc --version

You get:

    vcc: NVIDIA (R) Cuda compiler driver
    Copyright (c) 2005-2018 NVIDIA Corporation
    Built on Tue_Jun_12_23:07:04_CDT_2018
    Cuda compilation tools, release 9.2, V9.2.148

This repo contains both python (numba) tests and cuda tests.

To run python (numba) tests, run:
 

    cd tests
    python run_test.py

If everything is configured properly, you get:

```
Finding cublas
	located at /home/ubuntu/miniconda3/envs/cudatest/lib/libcublas.so.9.2.148
	trying to open library...	ok
Finding cusparse
	located at /home/ubuntu/miniconda3/envs/cudatest/lib/libcusparse.so.9.2.148
	trying to open library...	ok
Finding cufft
	located at /home/ubuntu/miniconda3/envs/cudatest/lib/libcufft.so.9.2.148
	trying to open library...	ok
Finding curand
	located at /home/ubuntu/miniconda3/envs/cudatest/lib/libcurand.so.9.2.148
	trying to open library...	ok
Finding nvvm
	located at /home/ubuntu/miniconda3/envs/cudatest/lib/libnvvm.so.3.2.0
	trying to open library...	ok
	finding libdevice for compute_20...	ok
	finding libdevice for compute_30...	ok
	finding libdevice for compute_35...	ok
	finding libdevice for compute_50...	ok
NVVM version (1, 5)
```

To run CUDA (Thrust) tests, run:

    nvcc -o version thrust_version.cu
    ./version

You get:

    Thrust v1.9
