from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain`
from langchain.chains import SequentialChain
from secret_key import openapi_key
import os
os.environ['OPENAI_API_KEY']=openapi_key
llm=OpenAI(temperature=0.6)
def generate_restraunt_name_and_items(cuisine):
    #chain1: restaurant name
    prompt_template_name=PromptTemplate(
        input_variables=['cuisine'],
        template="i want to open a restaurant for {cuisine} food .suggest a fancy name for this."
    )
    name_chain=LLMChain(llm=llm,prompt=prompt_template_name,output_key='restaurant_name')

    # chain2:Menu items
    prompt_template_items=PromptTemplate(
        input_variables=['restaurant_name'],
        template="suggest some menu items for {restaurant_name}.return it as comma separated value"
    )
    food_items_chain=LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )
    response=chain({'cuisine':cuisine})
    return response
if __name__=='__main__':
    print(generate_restraunt_name_and_item('Italian'))