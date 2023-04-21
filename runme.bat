@echo off

rem Set the version of Miniconda to download
set VERSION=latest

rem Set the URL to download the latest Miniconda installer
set URL=https://repo.anaconda.com/miniconda/Miniconda3-%VERSION%-Windows-x86_64.exe

rem Set the name of the installer file
set FILENAME=Miniconda3-%VERSION%-Windows-x86_64.exe

rem Set the installation path
set INSTALL_PATH=%USERPROFILE%\Miniconda3
set CONDA_EXE=%INSTALL_PATH%\Scripts\conda.exe
set CONDA_BAT=%INSTALL_PATH%\condabin\conda.bat
set CONDA_ACT=%INSTALL_PATH%\Scripts\activate.bat
set CONDA_ENV_NAME=stablelm



if exist "%UserProfile%\Miniconda3" (
    echo Miniconda is already installed.
) else (
rem Download the latest Miniconda installer using curl
echo Downloading Miniconda installer...
curl -o %FILENAME% %URL%

rem Install Miniconda silently
echo Installing Miniconda...
start /wait "" "%FILENAME%" /S /D="%INSTALL_PATH%"
echo Init Conda shell...
call "%CONDA_EXE%" init cmd.exe

echo Adding Conda channels...
call "%CONDA_BAT%" config --add channels conda-forge
call "%CONDA_BAT%" config --add channels pytorch

echo Installing dependencies..
call "%CONDA_BAT%" env create --file environment.yml


rem call "%CONDA_BAT%" install --yes pytorch
rem call "%CONDA_BAT%" install --yes torchvision
rem call "%CONDA_BAT%" install --yes torchaudio
rem call "%CONDA_BAT%" install --yes torchaudio
rem call "%CONDA_BAT%" install --yes cudatoolkit=11.4 
rem call "%CONDA_BAT%" install --yes transformers


rem Cleanup
echo Cleaning up...
del "%FILENAME%"

rem Print message when installation is complete
echo Miniconda is now installed at %INSTALL_PATH%.
)


echo Installing dependencies..
call "%CONDA_BAT%" install --yes pytorch transformers torchvision torchaudio cudatoolkit=11.4



cmd "/k activate stablelm && python chat.py"
