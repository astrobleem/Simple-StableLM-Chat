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
call "%CONDA_BAT%" config --add channels pytorch
call "%CONDA_BAT%" config --add channels conda-forge


echo Installing dependencies..
call "%CONDA_BAT%" install --yes pytorch torchvision torchaudio cudatoolkit=11.4 -c pytorch -c nvidia 
call "%CONDA_BAT%" install --yes transformers


rem Cleanup
echo Cleaning up...
del "%FILENAME%"

rem Print message when installation is complete
echo Miniconda is now installed at %INSTALL_PATH%.
)


echo Installing dependencies..
call "%CONDA_BAT%" install --yes pytorch transformers torchvision torchaudio cudatoolkit=11.4 -c pytorch -c nvidia 



cmd "/k activate base && python chat.py"
