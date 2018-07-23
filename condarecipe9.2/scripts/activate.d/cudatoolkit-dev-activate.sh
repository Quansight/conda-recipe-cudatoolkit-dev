#!/usr/bin/env bash

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/bin/*;
do 
    link=$(basename "$f");
    ln -sf $f $CONDA_PREFIX/bin/${link};
done


for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/lib64/*;
do 
    link=$(basename "$f");
    ln -sf $f $CONDA_PREFIX/lib/${link};

done

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/include/*;
do 
    link=$(basename "$f");
    ln -sf $f $CONDA_PREFIX/include/${link};

done


ln -sf $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/nvvm $CONDA_PREFIX/
ln -sf $CONDA_PREFIX/lib $CONDA_PREFIX/lib64 
