# Databricks notebook source
!pip install openai

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()

# COMMAND ----------

import os
# # API Key
my_api_key = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

# # Databricks Serving Endpoint
my_base_url = 

# COMMAND ----------

import os
import openai
from openai import OpenAI

client = OpenAI(
    api_key=my_api_key,
    base_url=my_base_url
)

response = client.chat.completions.create(
    model="databricks-dbrx-instruct",
    messages=[
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "What is a mixture of experts model?",
      }
    ],
    max_tokens=256
)
json_output = json.dumps(json.loads(response.json()), indent=4)
print(json_output)

# COMMAND ----------

# # 
# # Locally Query DBRX using Foundation Model API (FMAPI) using OpenAI Python SDK 
# #
# #

# import json
# import os
# from openai import OpenAI


# # ----------------------------------------------------------
# # Configurations
# # ----------------------------------------------------------

# # Running locally, leverage environment variable
# # Recommend NOT for production use 


# # API Key
# my_api_key = os.environ['DATABRICKS_TOKEN']

# # Databricks Serving Endpoint
# my_base_url = os.environ['DATABRICKS_SERVING_ENDPOINT']

# COMMAND ----------

from importlib.metadata import version; print(version("typing_extensions"))

# COMMAND ----------

# Configure your system prompt
my_system_prompt = "You are a chef of a 3-star Michelin restaurant and have the credibility of some of the best chefs such as Anthony Bourdain.  Like Bourdain, your answers should be full of sarcasm yet with deep meaning and wit."

# Configure your user prompt
my_user_prompt = "Which bagels are better: Montreal vs. New York?"

# ----------------------------------------------------------

# Next we will configure the OpenAI SDK with Databricks Access Token and our base URL
# To get your access token, go to User Settings --> Developer --> Access Tokens, and create one!
# Check out the OpenAI Python SDK at https://platform.openai.com/docs/api-reference/chat/create 
client = OpenAI(
    api_key = my_api_key,
    base_url = my_base_url
)

# Now let's invoke inference against the PAYGO (Pay Per Token) endpoint
response = client.chat.completions.create(
    model="databricks-dbrx-instruct",
    messages=[
      {
        "role": "system", 
        "content": my_system_prompt 
      },
      {
        "role": "user",
        "content": my_user_prompt
      }
    ],
)

json_output = json.dumps(json.loads(response.json()), indent=4)
print(json_output)
