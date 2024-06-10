# Health assistant chat bot

Health assistant chat bot to help with health advice.

![architecture](images/architecture.png)

We use two data sets which are enriched with FBLLMs (DBRX model), and then piped into separate vector searches for better separation.

The llm pipeline can be found in: [etl/health_chat_bot.ipynb](etl/health_chat_bot.ipynb)

The source datasets are from:

* ICD data from [https://www.cms.gov/medicare/coding-billing/icd-10-codes/2023-icd-10-cm](https://www.cms.gov/medicare/coding-billing/icd-10-codes/2023-icd-10-cm)
* 
