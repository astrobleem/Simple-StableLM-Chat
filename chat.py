import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, StoppingCriteria, StoppingCriteriaList

tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-tuned-alpha-7b")
model = AutoModelForCausalLM.from_pretrained("stabilityai/stablelm-tuned-alpha-7b")

#tokenizer = AutoTokenizer.from_pretrained("StabilityAI/stablelm-base-alpha-7b")
#model = AutoModelForCausalLM.from_pretrained("StabilityAI/stablelm-base-alpha-7b")

model.half().cuda()

class StopOnTokens(StoppingCriteria):
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        stop_ids = [50278, 50279, 50277, 1, 0]
        for stop_id in stop_ids:
            if input_ids[0][-1] == stop_id:
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
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    tokens = model.generate(**inputs, max_new_tokens=128,temperature=0.7,do_sample=True, stopping_criteria=StoppingCriteriaList([StopOnTokens()]))
    response = (tokenizer.decode(tokens[0], skip_special_tokens=True))
    return response

# initialize an empty session
session = ""

# loop until the user says "goodbye"
while True:
    # ask the user for a question
    question = input("Ask the oracle a question: ")
    
    # add the question to the session
    session += "User: " + question + "\n"
    
    # check if the user said "goodbye"
    if question.lower() == "goodbye":
        break
    
    # check if user said "clear"
    if question.lower() == "clear":
        session = ""
    # get the oracle's response from the function
    response = oracle_response(question)
    
    # respond with the oracle's response
    print("Oracle: " + response)
    
    # add the oracle's response to the session
    session = "Oracle: " + response + "\n"
    
# print the entire session
print("Conversation history:\n" + session)


# save the session to a file
with open("session.txt", "w") as f:
    f.write(session)

# print a message indicating that the session has been saved
print("Session saved to session.txt.")

