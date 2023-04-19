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


![Working](https://github.com/astrobleem/Simple-StableLM-Chat/blob/a9dd3d307d6dad140d7775f9badf635ba2861f12/working.bmp)

You'll need a working cuda torch environment.



Here are some notes from the setup.


nvidia-smi
#pay attention to cuda toolkitversion

conda create --name stablelm

conda activate stablelm





conda config --add channels pytorch
conda config --add channels conda-forge


#change cudatoolkit to match your installed version

conda install pytorch torchvision torchaudio cudatoolkit=11.4 -c pytorch -c nvidia

#huggingface download of model wouldnt work until i did this

pip install --upgrade urllib3

#checks to see if torch works with cuda

python -c "import torch; print(torch.cuda.is_available())"

