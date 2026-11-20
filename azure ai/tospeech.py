
"""
For more samples please visit https://github.com/Azure-Samples/cognitive-services-speech-sdk
"""

import azure.cognitiveservices.speech as speechsdk
from urllib.parse import urlparse

# Using the functional credentials from the previous step
endpoint_url = "https://25695a3213-7074-resource.cognitiveservices.azure.com/"
speech_key = "1IXGlGyFuQDkf8VKgLbvr8Y23CpsnZoXuY2UzpriSNK0nMKvwpijJQQJ99CKACF24PCXJ3w3AAAAACOGAU2X"

parsed = urlparse(endpoint_url)
base_endpoint = f"{parsed.scheme}://{parsed.netloc}"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, endpoint=base_endpoint)
speech_config.speech_synthesis_voice_name = "en-US-EmmaMultilingualNeural"

# Use the default speaker as audio output
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

text = "Hello, welcome to Azure AI Foundry!"

result = speech_synthesizer.speak_text_async(text).get()

# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))