# Simple-StableLM-Chat

![Built to use Stability AI's Stable LM](https://github.com/Stability-AI/StableLM/blob/main/README.md)


This is a very simple python app that you can use to get up and talking with Stability AI's recently released Stable LM models locally.

Requirements
---------------
This works on my computer to load the 7B parameter models.

Windows 10 
16GB System RAM
Nvida Tesla M40 with 24GB VRAM


Chatbot Documentation
---------------

StableLM is a chatbot framework that allows you to build natural language interfaces. Here's some information about StableLM:

* The StableLM API is built on top of the popular Natural Language Toolkit (NLTK) library.
* StableLM supports various NLP tasks, such as tokenization, part-of-speech
* It is an open-source project, with a Python version included.


Example Output
---------------
![Working](https://github.com/astrobleem/Simple-StableLM-Chat/blob/c48523ebf1e942e33cce2ca434c368a57a8f798f/stablepoem.png)




Setting Up
---------------

You'll need a working conda and cuda torch environment.








Here are some notes on how to get this setup:

#Open PowerShell

Invoke-WebRequest -Uri https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe -OutFile Anaconda3-2021.05-Windows-x86_64.exe

.\Anaconda3-2021.05-Windows-x86_64.exe /S

#wait a long time... this launches silent install of anaconda

#close PowerShell

#launch Anaconda Prompt powershell 

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


Execute the Program
---------------------

python .\chat.py


