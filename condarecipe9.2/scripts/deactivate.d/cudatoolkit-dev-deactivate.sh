#!/usr/bin/env bash

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/bin;
do  
    unlink $CONDA_PREFIX/bin/${f}

done


for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/lib64;
do 
    unlink $CONDA_PREFIX/lib/${f}
    
done

unset CUDA_HOME