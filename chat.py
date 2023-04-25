"""
This module implements a chatbot using StableLM, an AI language model trained by StabilityAI.
The chatbot provides responses to user questions using StableLM's natural language processing capabilities.

The chatbot uses StableLM's pre-trained model, and generates responses based on user inputs using the 
model's predictive abilities. The chatbot is designed to respond to a variety of questions related to 
general knowledge topics.

Usage:
    Run this module directly to start a conversation with the chatbot. You can ask the chatbot any 
    question and it will generate a response based on its trained knowledge. 

    You can also import this module and use the `oracle_response` function to generate responses to 
    user questions programmatically.

Author:
    Chad Doebelin
"""
MODEL_NAME = "stabilityai/stablelm-tuned-alpha-7b"
MAX_LENGTH = 256
TEMPERATURE = 0.65

import torch
import time
from transformers import AutoModelForCausalLM, AutoTokenizer, StoppingCriteria, StoppingCriteriaList, pipeline


# Check for CUDA availability
# device = torch.device("cuda" if not(torch.cuda.is_available()) else "cpu")
# print(f"The device type is {device.type}")
def bytes_to_gb(bytes_value):
    gb_value = bytes_value / (1024 ** 3)
    return gb_value

def get_device():
    if torch.cuda.is_available():
        # Get current GPU's VRAM (in bytes)
        vram_bytes = torch.cuda.get_device_properties(0).total_memory
        print(f"Cuda Found! You have {((round(bytes_to_gb(vram_bytes))))} GB VRAM\n")

        # Convert 24 GB to bytes
        min_vram_required_bytes = 24 * (1024 ** 3)

        if vram_bytes >= min_vram_required_bytes:
            return torch.device("cuda")
        if ((round(bytes_to_gb(vram_bytes))) >= 16):
            return torch.device("cuda")
    print("You didn't have at least 16GB of VRAM. Switching to CPU.")
    return torch.device("cpu")

device = get_device()


# If using CPU support and use appropriate data type
if device.type == "cpu":
        print("You're using a CPU, we're going to use the smaller 3B set")
        MODEL_NAME = "stabilityai/stablelm-tuned-alpha-3b"
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
        model.float().to(device)
        torch.backends.cudnn.enabled = False
else:
    print("loading tokenizer RAM")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    print("loading model to RAM")
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    print("sending to GPU")
    model.half().to(device)
    

class StopOnTokens(StoppingCriteria):
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        stop_ids = [50278, 50279, 50277, 1, 0]
        for stop_id in stop_ids:
            if input_ids[0][-1] == stop_id:
                return True
        return False
		
class StopOnLength(StoppingCriteria):
    def __init__(self, max_length: int):
        self.max_length = max_length

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        if len(input_ids[0]) >= self.max_length:
            return True
        return False
        
class StopOnQuality(StoppingCriteria):
    def __init__(self, max_perplexity: float):
        self.max_perplexity = max_perplexity
        self.language_model = pipeline("text-generation", model="gpt2")

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        generated_text = self.language_model.tokenizer.decode(input_ids[0])
        perplexity = self.language_model(generated_text)[0]["perplexity"]
        if perplexity >= self.max_perplexity:
            return True
        return False
        
        
# open the file for reading
with open("preprompt.txt", "r") as f:
    # read the contents of the file into a variable
    preprompt = f.read()

# print the contents of the file
print("Preprompt text:")
print(preprompt)

# define a function for the oracle's response
def oracle_response(question):
    # add your logic here to generate a response based on the user's question
    prompt = f"{session}\n<|USER|>{question}\n<|ASSISTANT|>\n"
    
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    print("Generating response...")
     # Record the start time
    start_time = time.time()
    
    tokens = model.generate(**inputs, max_new_tokens=MAX_LENGTH,temperature=TEMPERATURE,do_sample=True, stopping_criteria=StoppingCriteriaList([StopOnTokens()]))
    response = (tokenizer.decode(tokens[0], skip_special_tokens=True))
    # Record the end time and calculate the elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Response generated! Time elapsed: {elapsed_time:.2f} seconds")  # Print the elapsed time
    print(f"Response generated! Time elapsed: {elapsed_time/60:.2f} minutes")

    return response

# initialize an empty session
session = ""

# loop until the user says "goodbye"
while True:
    # ask the user for a question
    question = input("Ask the oracle a question: ")
    
    # add the question to the session
    session += "<|USER|>" + question + "\n"
    
    # check if the user said "goodbye"
    if question.lower() == "goodbye":
        break
        
    #The temperature is a hyperparameter used in language generation models 
    #It controls the degree of randomness in the generated responses.
    #A higher temperature leads to more diverse and unpredictable responses, 
    #while a lower temperature leads to more conservative and predictable responses.
    if question.lower() == "increasetemp":
        #This can result in more creative and varied responses, but they may also be less coherent or relevant to the context.
        howmuch = float(input("increase how much?"))
        TEMPERATURE = round(TEMPERATURE + howmuch)
        print(TEMPERATURE)
        question = input("Ask the oracle a question: ")
    if question.lower() == "decreasetemp":
        #On the other hand, if the temperature is set to a low value, 
        #the language model is more likely to select the most probable word or token for the next output, 
        #resulting in more predictable and conservative responses.
        howmuch = float(input("decrease how much?"))
        TEMPERATURE = round(TEMPERATURE - howmuch)
        print(TEMPERATURE)
        question = input("Ask the oracle a question: ")
        
        
        
    if question.lower() == "increaselength":    
        howmuch = int(input("increase how much?"))
        MAX_LENGTH = MAX_LENGTH + howmuch
        print(MAX_LENGTH)
        question = input("Ask the oracle a question: ")
    if question.lower() == "decreaselength":
        howmuch = int(input("decrease how much?"))
        MAX_LENGTH = MAX_LENGTH - howmuch
        print(MAX_LENGTH)
        question = input("Ask the oracle a question: ")        
    # check if user said "clear"
    if question.lower() == "clear":
        session = ""
        question = input("Ask the oracle a question: ")
    # get the oracle's response from the function
    response = oracle_response(question)
    response = response.replace(question,"")
    # respond with the oracle's response
    print("Oracle: " + response)
    
    # add the oracle's response to the session
    session = "<|ASSISTANT|>" + response + "\n"
    
# print the entire session
#print("Conversation history:\n" + session)


# save the session to a file
#with open("session.txt", "w") as f:
#    f.write(session)

# print a message indicating that the session has been saved
#print("Session saved to session.txt.")

