import logging
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

# Configure logging to capture all levels of log messages
#logging.basicConfig(level=logging.DEBUG)

# Initialize the OllamaLLM model with the specified version
model = OllamaLLM(model="nemotron-mini:latest")

# Create a chat prompt template with a system message and a human message template
chat_template = ChatPromptTemplate.from_messages(
    [
        # System message to set the context for the assistant
        SystemMessage(
            content=(
                "You are a helpful assistant that re-writes the user's text to "
                "sound more upbeat."
            )
        ),
        # Human message template to capture user input
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

# Chain the chat template, model, and output parser together
chain = chat_template | model | StrOutputParser()

# Invoke the chain with a sample input text
result = chain.invoke({"text": "I don't like eating tasty things"})

# Print the result of the chain invocation
print(result)