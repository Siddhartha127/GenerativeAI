from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4',temperature=1.5, max_completion_tokens=10                                                                     )
# temperature is a parameter that controls the randomness of a models output. It determines the creative or determinism of the response . 
# lower values(0-0.3)= more deterministi and predictablr
# higher values(0.7-1.5)= more creative and diverse
# max_completion_tokens is the maximum number of tokens that the model can generate in a single response.
result = model.invoke("What is the capital of India?")

print(result)
print(result.content) # only answer 