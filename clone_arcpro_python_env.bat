::batch file made to clone the default ArcGIS Pro python environment and install aws libraries

::set new env location
SET new_env="C:\...\arcgispro-py3-clone"

::activate existing env
C:
cd "C:\Program Files\ArcGIS\Pro\bin\Python\Scripts"
CALL activate.bat 

::clone env
conda create --clone arcgispro-py3  -p %new_env%

::activate new environment
CALL activate.bat %new_env%

::install boto3
conda install boto3

::install aws cli
conda install -c conda-forge awscli

pause