import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, SentimentOptions

authenticator = IAMAuthenticator('pjuol5xlhT0U0GF7vs3vzbI5JPzugntN_ftK9Bk8pwJz')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/06e8025a-5b56-4249-b65d-efa8b53ee13e')

response = natural_language_understanding.analyze(
    text=review_text,
    features=Features(sentiment=SentimentOptions())).get_result()

print(json.dumps(response, indent=2))
