# LangChain Experimentation
LangChain Experimentation is a repo to store LLM experiments conducted with LangChain.

**AI_Executive_Order_LangChain.ipynb** is a notebook which chunks and vectorizes the October 2023
* *United States Aritificial Intelligence Executive Order* *, stores that locally in a Weaviate vector
db, and uses an OpenAI API Key and GPT 3.5 Turbo to answer questions about the EO.

**joke.py** leverages a local LLM to produce custom humor.

More projects will be uploaded as they get refined.

Requirements include:
* dotenv
* langchain
* argparse
* weaviate
* sys
