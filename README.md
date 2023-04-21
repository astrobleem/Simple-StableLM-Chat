# Simple-StableLM-Chat

![Built to use Stability AI's Stable LM](https://github.com/Stability-AI/StableLM/blob/main/README.md)

StableLM is a language model developed by Stability AI that has been trained on an incredibly vast dataset called Pile, which contains 1.5 trillion tokens. This makes StableLM one of the most advanced language models available, capable of generating highly nuanced and accurate responses to a wide variety of inputs.

The purpose of this project is to showcase the capabilities of StableLM by building a simple chatbot that can engage in conversations with users. With StableLM as its foundation, the chatbot is able to generate responses that are highly context-sensitive and demonstrate a remarkable level of understanding of natural language.

To try out the chatbot, simply follow the instructions provided in the repository. You'll be able to engage in conversations with the chatbot and witness firsthand the impressive capabilities of StableLM. We hope that this project serves as a starting point for others who are interested in exploring the power of StableLM and the potential of AI chatbots.
This is a very simple python app that you can use to get up and talking with Stability AI's recently released Stable LM models locally.

Requirements
---------------
This works on my computer to load the 7B parameter models.

-Windows 10 

-16GB System RAM

-Nvida Tesla M40 with 24GB VRAM

-40 GB FREE DISK SPACE

If you only have 16GB of RAM, and No GPU, this is going to be really bad. 
It will attempt to load the 3B parameter model, which does fit, but there
is no room left over for anything else so it starts swapping to disk. 


Chatbot Documentation
---------------



Example Output
---------------
![Working](https://github.com/astrobleem/Simple-StableLM-Chat/blob/c48523ebf1e942e33cce2ca434c368a57a8f798f/stablepoem.png)




Setting Up
---------------

I added a runme.bat file that should download and install miniconda and then then requirements, and then launch the app. 
After cloning the repository, 
Double click the runme.bat
This will take a long time. It's going to download a lot of stuff.



Contributing
-------------

Contributions to Simple-StableLM are welcome. If you find a bug or have a suggestion for a new feature, please open an issue on the GitHub repository. If you would like to contribute code, please fork the repository and create a pull request.

License
------------
Simple-StableLM is released under the Apache 2.0 License. See LICENSE for details.



