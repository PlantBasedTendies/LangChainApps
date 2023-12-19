# LangChainApps
LangChainApps is a repo to store LLM experiments conducted with LangChain.

--------
### :robot: **AI_Executive_Order_LangChain.ipynb**: 
A Retrieval Augmented Generation exercise notebook which outlines the process of:
- Chunking and vectorizing the October 2023 [**United States _Artificial Intelligence Executive Order_**](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/)
- Storing the vector embeddings locally in a Weaviate vector
db
- Using an OpenAI API Key / GPT 3.5 Turbo to answer questions about the EO

--------

### :rofl: **joke.py**: 
A CLI python script which:
- Leverages an Open Source local LLM*, therefore no OpenAI API Key is necessary, and thus no cost
- Produces custom jokes on the fly \
  \
  *7B parameter LLM is recommended for this type of exercise.

--------

:wrench: Requirements include:
* dotenv
* langchain
* argparse
* weaviate
* sys

\
:gear: To run the notebook, you will need to populate **default.env** with your OpenAI API key and rename it to **.env**
