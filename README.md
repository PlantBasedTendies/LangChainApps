# LangChain Experimentation
LangChain Experimentation is a repo to store LLM experiments conducted with LangChain.

**AI_Executive_Order_LangChain.ipynb** is a notebook which chunks and vectorizes the **October 2023
United States _Aritificial Intelligence Executive Order_**, stores that locally in a Weaviate vector
db, and uses an OpenAI API Key and GPT 3.5 Turbo to answer questions about the EO.

**joke.py** leverages a local LLM - and thus no OpenAI API Key (or cost) necessary - to produce custom humor.


Requirements include:
* dotenv
* langchain
* argparse
* weaviate
* sys
