'''
   A 'hello world' script to explore LangChain. It should
   be noted that in the Local LLM community, it is not advised
   to use LangChain in production at this time.
   Date: 09/09/2023

   Sample Command Line:
   python joke.py --adjective funny --conent dogs
'''

# Import Deps
from langchain.llms import LlamaCpp
from langchain import PromptTemplate
import argparse
import sys

# Add arguments
parser = argparse.ArgumentParser(description='Provide a (1) style of joke and a (2) joke topic')
parser.add_argument("--adjective", type=str, help="Style of joke, i.e. mean, funny, sad")
parser.add_argument("--content", type=str, help="Joke subject, i.e. babies, social-media, sports")
args = parser.parse_args()

# Check for command line arguments
if not sys.argv[1:]:
    print("\nPlease specify two arguments to run this script - style of joke and subject of joke - in the following manner: " + "\n\n" +
          
          "$ python joke.py --adjective \033[1mfunny\033[0m --content \033[1mbabies\033[0m" + "\n")
    sys.exit()

# Import LLM
llm = LlamaCpp(
#    model_path="~/AI/LLMs/oobabooga/text-generation-webui/models/codallama_models/codellama-34b-instruct.Q3_K_S.gguf",
    model_path="./models/llama-7b.ggmlv3.q4_0.bin",
    n_gpu_layers=4,
    n_ctx=512,
    temperature=.8
    )

# Define a template
print("\n")
template= """Q: Tell me a {adjective} joke about {content}.
A: """

# Create prompt from template
prompt = PromptTemplate.from_template(template)

# Check prompt variable
# print(prompt)

# Check input variables
# print(prompt.input_variables)

# Check prompt template
# print(prompt.template)

# Format the prompt and print it
# formatted_prompt = prompt.format(adjective="mean", content="babies")
formatted_prompt = prompt.format(adjective=str(args.adjective), content=str(args.content))
print(formatted_prompt)

# Prompt the LLM
result = llm(prompt = formatted_prompt, llm = llm, stop=["Q:", "\n"])
print(result)