# Simple-StableLM-Chat


#https://github.com/Stability-AI/StableLM/blob/main/README.md


This is a very simple python app that you can use to get up and talking with Stability AI's recently released Stable LM models locally.



Chatbot Chatbot Documentation
---------------

StableLM is a chatbot framework that allows you to build natural language interfaces. Here's some information about StableLM:

* The StableLM API is built on top of the popular Natural Language Toolkit (NLTK) library.
* StableLM supports various NLP tasks, such as tokenization, part-of-speech
* It is an open-source project, with a Python version included.
* It is written by a team of volunteers, who are always available to support its development.
* It has a large and active community


![Working](https://github.com/astrobleem/Simple-StableLM-Chat/blob/c48523ebf1e942e33cce2ca434c368a57a8f798f/stablepoem.png)

You'll need a working cuda torch environment.



Here are some notes from the setup.


Open PowerShell
PS D:\downloads> nvidia-smi
Wed Apr 19 20:12:01 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 473.81       Driver Version: 473.81       CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name            TCC/WDDM | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla M40 24GB     WDDM  | 00000000:01:00.0 Off |                    0 |
| N/A   27C    P8    17W / 250W |     46MiB / 23040MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+

take note CUDA Version: 11.4 


Invoke-WebRequest -Uri https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe -OutFile Anaconda3-2021.05-Windows-x86_64.exe

.\Anaconda3-2021.05-Windows-x86_64.exe /S

wait a long time... anaconda is stupid to install
close PowerShell

launch Anaconda Prompt powershell 

git clone https://github.com/astrobleem/Simple-StableLM-Chat.git
cd Simple-StableLM-Chat
conda create --name stablelm

conda activate stablelm

conda config --add channels pytorch

conda config --add channels conda-forge

#change cudatoolkit to match your installed version

conda install pytorch torchvision torchaudio cudatoolkit=11.4 -c pytorch -c nvidia
conda install transformers

pip install --upgrade urllib3
conda install --file requirements.txt
python -c "import torch; print(torch.cuda.is_available())"
python -c "import torch; print(torch.__version__)"

python .\chat.py


