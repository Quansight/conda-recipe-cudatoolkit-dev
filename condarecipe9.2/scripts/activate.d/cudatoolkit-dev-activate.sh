#!/usr/bin/env bash

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/bin/*;
do 
    link=$(basename "$f");

    if ! [-L $CONDA_PREFIX/bin/${link}]; then
       ln -s $f $CONDA_PREFIX/bin/${link};
    fi 

done


for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/lib64/*;
do 
    link=$(basename "$f");
    
    if ! [-L $CONDA_PREFIX/lib/${link}]; then
       ln -s $f $CONDA_PREFIX/lib/${link};
    fi

done

set CUDA_HOME=$CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/