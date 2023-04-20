@echo off

set CONDA_EXE=%UserProfile%\Miniconda3\Scripts\conda.exe
set CONDA_ENV_NAME=stablelm
set CONDA_CHANNELS=pytorch conda-forge

echo Checking for Miniconda installation...
if exist "%UserProfile%\Miniconda3" (
    echo Miniconda is already installed.
) else (
    set DOWNLOAD_URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

    echo Downloading Miniconda installer...
    curl -o miniconda.exe %DOWNLOAD_URL%

    echo Installing Miniconda...
    start /wait "" miniconda.exe /S /D="%UserProfile%\Miniconda3"

    echo Cleaning up...
    del /f miniconda.exe
)

echo Activating Conda environment...
call "%CONDA_EXE%" activate %CONDA_ENV_NAME%

echo Adding Conda channels...
call "%CONDA_EXE%" config --env --add channels %CONDA_CHANNELS%

echo Installing packages with Conda...
call "%CONDA_EXE%" install -y cpuid transformers pytorch torchvision torchaudio cudatoolkit=11.4 -c pytorch -c nvidia

echo Upgrading urllib3 with Pip...
pip install --upgrade urllib3

echo Running chat.py...
python .\chat.py

echo Done.
