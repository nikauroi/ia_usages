"""
[env]
# Conda Environment
conda create --name fmm_fastapi_poc python=3.9.13
conda info --envs
source activate fmm_fastapi_poc
conda deactivate

# if needed to remove
conda env remove -n [NAME_OF_THE_CONDA_ENVIRONMENT]
conda env remove -n fmm_fastapi_poc


# update conda 
conda update -n base -c defaults conda

# to export requirements
pip freeze > requirements.txt

# to install
pip install -r requirements.txt

# manual install
To complete

# [path]
cd /Users/brunoflaven/Documents/03_git/ia_usages/ia_prompt_seo/

# launch the file
python usecase_referent_seo_1.py


"""

# for api key
import os
from dotenv import load_dotenv

# Import the OpenAI class from the openai module
from openai import OpenAI

### 1. GET API KEY ###
# Load environment variables from the .env file
load_dotenv()

# Access the API key using os.getenv
api_key = os.getenv("OPENAI_API_KEY")


### 2. GET STUFF FROM CHATGPOT ###
# Create an instance of the OpenAI class with the provided API key
client = OpenAI(api_key=api_key)

def openai_chat(user_prompt):

    # Create a chat completion using the OpenAI client
    response = client.chat.completions.create(
        # Set the model to "gpt-3.5-turbo-0125"
        model="gpt-3.5-turbo-0125", 
        messages=[{"role": "user", "content": user_prompt}]
    )

    # Response from the chat completion
    answer = response.choices[0].message.content

    # Calculate the price for input tokens
    # For gpt-3.5-turbo-0125
    # Input : 0,50 US$ / 1M tokens
    
    input_price = response.usage.prompt_tokens * (0.5 / 1e6)

    # Calculate the price for output tokens
    # For gpt-3.5-turbo-0125
    # Output : 1,50 US$ / 1M tokens

    output_price = response.usage.completion_tokens * (1.5 / 1e6)

    # calculate the total price
    total_price = input_price + output_price

    # Return the answer, input price, output price, total price
    return {
        "answer": answer,
        "input_price": f"$ {input_price}",
        "output_price": f"$ {output_price}",
        "total_price": f"$ {total_price}"
    }


prompt = """
Who is Friedrich Nietzsche?
"""


# Calling our function with the prompt
openai_chat(prompt)

####### OUTPUT #######
print(openai_chat(prompt))


