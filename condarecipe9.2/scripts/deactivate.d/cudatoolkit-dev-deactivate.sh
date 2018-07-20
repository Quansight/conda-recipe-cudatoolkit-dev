#!/usr/bin/env bash

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/bin/*;
do  
    to_unlink=$(basename ${f});
    
    if [ -L $CONDA_PREFIX/bin/${to_unlink} ]; then
        unlink $CONDA_PREFIX/bin/${to_unlink};
    fi 

done


for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/lib64/*;
do  
    to_unlink=$(basename ${f});

    if [ -L $CONDA_PREFIX/lib/${to_unlink} ]; then
       unlink $CONDA_PREFIX/lib/${to_unlink};
    fi 
    
done


for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/nvvm/bin/*;
do  
    to_unlink=$(basename ${f});

    if [ -L $CONDA_PREFIX/bin/${to_unlink} ]; then
       unlink $CONDA_PREFIX/bin/${to_unlink};
    fi 
    
done

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/nvvm/lib64/*;
do  
    to_unlink=$(basename ${f});

    if [ -L $CONDA_PREFIX/lib/${to_unlink} ]; then
       unlink $CONDA_PREFIX/lib/${to_unlink};
    fi 
    
done
