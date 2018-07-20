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

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/nvvm/bin/*;
do 
    link=$(basename "$f");
    ln -sf $f $CONDA_PREFIX/bin/${link};

done

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/nvvm/lib64/*;
do 
    link=$(basename "$f");
    ln -sf $f $CONDA_PREFIX/lib/${link};

done

for f in $CONDA_PREFIX/pkgs/cudatoolkit-dev-9.2-0/nvvm/libdevice/*;
do 
    link=$(basename "$f");
    ln -sf $f $CONDA_PREFIX/lib/${link};

done