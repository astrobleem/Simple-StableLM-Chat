# Simple-StableLM-Chat
created from
#https://github.com/Stability-AI/StableLM/blob/main/README.md
This is a very simple python app that you can use to get up and talking with Stable Diffusions Stable LM models locally.


![Working](https://github.com/astrobleem/Simple-StableLM-Chat/blob/a9dd3d307d6dad140d7775f9badf635ba2861f12/working.bmp)
You'll need a working cuda torch environment.
Here are some notes.



nvidia-smi
#pay attention to cuda toolkitversion

conda create --name my_env
conda activate my_env




conda config --add channels pytorch
conda config --add channels conda-forge


#change cudatoolkit to match your installed version
conda install pytorch torchvision torchaudio cudatoolkit=11.4 -c pytorch -c nvidia

#huggingface download wouldnt work until i did this
pip install --upgrade urllib3

#checks to see if torch works with cuda

python -c "import torch; print(torch.cuda.is_available())"

