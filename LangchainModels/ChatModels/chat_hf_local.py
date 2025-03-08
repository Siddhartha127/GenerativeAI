from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
os.environ['HF_HOME'] = 'W:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        do_sample=True,
        temperature=0.5,
        max_new_tokens = 100
    )
)
model = ChatHuggingFace(llm=llm)
x = input("Enter 'Start' to begin: ")
if x.strip().lower() == "start":
    while True:
        ques = input("Enter query (type 'STOP' to exit): ")
        if ques.strip().lower() == "stop":
            print("Chatbot session ended.")
            break

        result = model.invoke(ques)
        print("Bot:", result.content)