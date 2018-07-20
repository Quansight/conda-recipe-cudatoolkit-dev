#!/usr/bin/env bash

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/bin/*;
do  
    to_unlink=$(basename ${f});
    unlink $CONDA_PREFIX/bin/${to_unlink};

done


for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/lib64/*;
do  
    to_unlink=$(basename ${f});
    unlink $CONDA_PREFIX/lib/${to_unlink};
    
done

unset CUDA_HOME