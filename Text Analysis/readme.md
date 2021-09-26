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
the code read comments data from other code  [Facebook Comments Collector](https://github.com/HossamAbdelraof/Facebook-Comments-Colelctor)

the process steps

1- check if the comment is amention using NER

2- translate the comment to english if required and if not a mention

3- apply sentment analysis to the translated comment

4- save the colelcted data to .csv and .txt files
##

### NER function:

```python
def NER(text):
    global text_analysis_client
    
    ## add limit to the comment or it is a spam comment
    if len(text) > 750:
        return True
    
    try:
        
        # send request with the text
        NER_res = text_analysis_client.recognize_entities(documents = [text])[0]
        
        try:
        
            # check if the result is person return True
            # if no data returns then it's not human
            entity = NER_res.entities[0]
            
            if entity.category == 'Person':
                return True
                
            else:
              return False
              
        except IndexError:
            return False
        
    except Exception as err:
        print("Encountered exception. {}".format(err))
```

this function check if the comment is mantioned person or human name 
if return True if name found and False if any else

#
### Translate Function:

```python
def translate(text):
    
    global translate_key
    global translate_endpoint
    global is_human
    
    if is_human:
        return text
     
    # subscription key and endpoint
    subscription_key = translate_key
    endpoint = translate_endpoint   

    # select endpoint resource url url
    constructed_url = endpoint + '/translate'

    # set request parameters and headers
    params = {
        'api-version': '3.0',
        'to': 'en',
        'toScript': 'latn'}  

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': "eastus",
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())

    # set body {text or document to translate}.
    body = [{
        'text': text}]

    
    # send the request and get translated comment
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    
        # convert data to json
    response = request.json()

    # return translated text
    return response[0]['translations'][0]['text']
```

this function translate the comment to englist using azure Cognitive Translation request 
but if the comment is human name it return the name without translation

#
### Sentment Analysis Function:
```python
def sentiment_analysis(translated):
    
    global text_analysis_client
    

    if not(is_human):
        

        ## analyse translated text score
        response =  text_analysis_client.analyze_sentiment(documents=[translated])[0]
        ## P1 is the overall sentment 
        p1 = "Document Sentiment: {}\n".format(response.sentiment)
        ## P2 is every rate score 
        p2 = "\nOverall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            response.confidence_scores.positive,
            response.confidence_scores.neutral,
            response.confidence_scores.negative)
        
        result = p1 + p2
        
        return result
        
    
    # if the result is human name
    # will not ranslate and assume the text is neutral
    else:
        result = "Document Sentiment: neutral\n" + "Overall scores: positive=0.00; neutral=1.00; negative=0.00\n"
        return result
```
this function apply sentment analysis on the translated comment and get it' negative/positive/neutral rank and every statement propability

# 
### the data Table:
```python
data = {"text":[],
        "Translate":[],
        "is_human":[],
        "Sentiment":[]}
```
data table contain many columns 

> text: the orignal text to merge on (in the next code)<br />
Translated: the translated comment<br />
is_human: if the comment is human or not<br />
sentent: the sentment rank<br />


#
### Start Function:
the start  function call the main 3 function and write the result to .txt file andad it to the data table<br />
```python
def start(file, start= 0, end = -1):
    global data
    
    try: 
        if start == end:
            print("Data Limit Reached")
            return


        # load text from the data frame
        text = df.message[start]

        # checkif the comment is human mention
        is_human = NER(text)

        # translate the text to English
        translated = translate(text)
 

        # runsentment analysis on translated text
        result = sentiment_analysis(translated)


        ## add text to DF
        data["text"].append(text)

        ## Add humanity uesult
        file.write("\nis human: {}\n".format(is_human))
        data["is_human"].append(is_human)

        ## add Translated text 
        file.write("Translate: {}\n".format(translated))
        data["Translate"].append(translated)

        ## add analysis result
        data["Sentiment"].append(result)
        file.write(result)

        ## write Done and indexnumber 
        file.write("\n done {}\n".format(start))

        """
        Recall the Function Again until no Data or reach limit
        """
        start(file, start+1)
        
        
    except KeyError as e:
        print("No More Data\nprocessis done")
        return
```


