# Almentor-Data-Analysis

this analysis is next step of gathering data with Facebook API [in this repo](https://github.com/HossamAbdelraof/Facebook)

this project based in 2 steps  *Text  analysis in the result* to check the people interactions in comments  and 
 
here worked with 3 phases 

1- text analysis <br /><br />
2- data Analysis for Almentor.net facebook page post comments<br /><br />
3- data Analysis for Hessas masr facebook page post comments<br /><br />

#
## 1- text analysis:
the data we got from Facebook is comments, so we need to find peoples interactions iin our products based on ther comments<br>
from the analysis we can extract names and mentions, rating comments, complaints

the text analysis based on series steps:

***Setup text withfinctions***
|No. | Function | Function job |
|--- | --- | --- |
|1- |*Translate*: |translate the comments with Azure translation REST API|
|2- |*NER*: | apply Nane Entity Recognition to the translated text to findout if it is a name or mention|
|3- |*Text Rating*: | rate the text \[positive, negative, neutral\]|

***SaveResult to DF and Text***
the final results saved in DF and Text file 
#
## 2- data Analysis for Almentor.net
after setting up the data will start the analysis
the analysis for this page in (Almentor)[https://github.com/HossamAbdelraof/Almentor-Data-Analysis/tree/main/Almentor] directory


#
## 3- data Analysis for Hessas masr
Now the analysis for Hessas Masr page have extra work 
all the work in (Hessas Mesr)[https://github.com/HossamAbdelraof/Almentor-Data-Analysis/tree/main/Hessas%20Mesr] direcory


