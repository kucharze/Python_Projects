# file based from the following youtube video: https://www.youtube.com/watch?v=br09SwR8axo

from langchain.utilities import DuckDuckGoSearchAPIWrapper
import os
from langchain.prompts import ChatPromptTemplate

examples = [
    {
        "input": "Can members of the police legally make arrests?",
        "output": "What can members of the police do?"
    }
]

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxx"