# Text Analysis for Almentor.net Facebook data

before starting work create Azure text analysis/translation resource
```
https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics
https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesTextTranslation
```

install text analysis python libraries 

```
pip install azure-ai-textanalytics
```


this codeuse 2 text analysis services { sentment_analysis, NER } 
azure translation service

## 
the code read comments data from other code  ( Facebook comment collector repo )

the process steps

1- check if the comment is amention using NER

2- translate the comment to english if required and if not a mention

3- apply sentment analysis to the translated comment

4- save the colelcted data to .csv and .txt files
