# file based from the following youtube video: https://www.youtube.com/watch?v=br09SwR8axo

from langchain.utilities import DuckDuckGoSearchAPIWrapper
import os
from langchain.prompts import ChatPromptTemplate

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxx"

examples = [
    {
        "input": "Can members of the police legally make arrests?",
        "output": "What can members of the police do?"
    },
    {
        "input": "In what country was Jan Schinde born?",
        "output": "What is Jan Schindel's background?"
    },
]

example_prompt = ChatPromptTemplate.from_messages([
    [
        ('human', '{input}?'),
        ('ai', '{output}')
    ]
])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    # input_variables=["input", "output"]
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert at world knowledge. Your task is to step back and paraphrase a question to a more generic step-back question, which is easier to answer."),
    few_shot_prompt,
    ("user", "{question}")
])