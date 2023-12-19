# LangChain Experimentation
LangChain Experimentation is a repo to store LLM experiments conducted with LangChain.

**AI_Executive_Order_LangChain.ipynb**: \
A notebook which chunks and vectorizes the **October 2023
United States _Aritificial Intelligence Executive Order_**, stores that locally in a Weaviate vector
db, and uses an OpenAI API Key / GPT 3.5 Turbo to answer questions about the EO.

--------

**joke.py**: \
A CLI python script which leverages an Open Source local LLM - therefore no OpenAI API Key is necessary, and thus no cost - to produce custom humor.
A 7B parameter LLM is recommended for this type of exercise.

--------

Requirements include:
* dotenv
* langchain
* argparse
* weaviate
* sys

To run the notebook, you will need to populate **default.env** with your OpenAI API key and rename it to **.env**
