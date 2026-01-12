from dotenv import load_dotenv
load_dotenv()

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

endpoint = os.environ["AI_SERVICE_ENDPOINT"]
key = os.environ["AI_SERVICE_KEY"]

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

result = client.analyze_sentiment(
    documents=["Azure AI Services DNS is now working perfectly."]
)

print(result[0].sentiment)