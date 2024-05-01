## Integrate our code OpenAI API
import os
from tabnanny import verbose
from constants import openai_key
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

first_prompt = PromptTemplate(
        input_variables = ['name'],
        template ="Tell me about celebrity {name}"
)



# streamlit framework
llm = Ollama(model="mistral")
chain = LLMChain(llm=llm,prompt =first_prompt,verbose=True)

st.title('Celebrity search')
input_text=st.text_input("Search the topic u want")


if input_text:
    st.write(chain.run(input_text))