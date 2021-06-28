# Deep Learning Chatbot Project

## System Requirements
* Python 3.9.5 x64 bit (Tensorflow doesn’t run on 32-bit distributions)
* Tensorflow 2.5.0
* Keras 2.4.3
* nltk 3.6.2
* numpy 1.19.5

## Test Chatbot
### Create Model
```
python train.py
```

### Run Chatbot
```
python chat.py
```

### Medical Support Intent Dataset Messages
- hello there my chatbot friend
- help me
- lookup for hospital
- patient id

### COVID-19 Intent Dataset Messages 
- will I die?
- contact with infected
- had contact with infected
- what are the steps to protect employees
- what to do outside
- outside?
- covid symptoms
- how much people have been infected

Covid model doesnt have a 100% accuracy so it may return an empty answer

## Link to medium tutorial
https://a01701804.medium.com/build-a-python-chatbot-using-keras-nltk-db19eea77f74
