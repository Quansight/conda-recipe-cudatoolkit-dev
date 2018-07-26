#!/usr/bin/env bash

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev/bin/*;
do  
    to_unlink=$(basename ${f});
    
    if [ -L "$CONDA_PREFIX/bin/${to_unlink}" ]; then
        unlink $CONDA_PREFIX/bin/${to_unlink};
    fi 

done


for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev/lib64/*;
do  
    to_unlink=$(basename ${f});

    if [ -L "$CONDA_PREFIX/lib/${to_unlink}" ]; then
       unlink $CONDA_PREFIX/lib/${to_unlink};
    fi 
    
done


for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev/include/*;
do 
    to_unlink=$(basename ${f});

    if [ -L "$CONDA_PREFIX/include/${to_unlink}" ]; then
       unlink $CONDA_PREFIX/include/${to_unlink};
    fi 
done    


if [ -L "$CONDA_PREFIX/nvvm" ]; then 
    unlink $CONDA_PREFIX/nvmm;
fi 


if [ -L "$CONDA_PREFIX/lib64" ]; then 
    unlink $CONDA_PREFIX/lib64;
fi 