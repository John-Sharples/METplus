#! /bin/sh

################################################################################
# Environment: diff.v5
# Last Updated: 2022-07-08 (mccabe@ucar.edu)
# Notes: Adds packages needed to run differences tests to compare output to
#   truth data.
# Python Packages:
#   pillow==9.2.0
#   pdf2image==1.16.0
#
# Other Content:
#   poppler-utils
################################################################################

# Conda environment to create
ENV_NAME=diff.v5

# Conda environment to use as base for new environment
BASE_ENV=netcdf4.v5

conda create -y --clone ${BASE_ENV} --name ${ENV_NAME}
conda install -y --name ${ENV_NAME} -c conda-forge pillow==9.2.0

yum -y install poppler-utils

conda install -y --name ${ENV_NAME} -c conda-forge pdf2image==1.16.0
