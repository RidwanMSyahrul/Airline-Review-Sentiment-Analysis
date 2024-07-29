# Airline Review Sentiment Analysis

# Introduction
A business quality is dependant on their customer feedbacks. Customer feedbacks are really important for company to see what they can improve on and change for the better. For example, an airline company. Customers has so many airline to choose from and the way they choose one that fit their needs (beside their destination) is to see the airline's review. Customer can see from other customer's past experience with the respective airline if they are worth to travel with. So, with that scenario in mind, the airline company can take adventage of the review they got to improve their airline quality. However, since there are countless of review, it won't be easy to read them one by one and check if it's a good review or a bad one. This sentiment analysis was made to help the airline to classify which review are Promoter (Good) review, Passive (Neutral) review, or Detractor (Bad) review, so that it will be easier to see what went wrong with the airline by only reading the Detractor review. This will help the company tremendously to improve their airline's quality and customer satisfaction.

## Objective
The objective of this project is to create an accurate sentiment analysis for airline review and classify them to three different class, which are Promoter, Passive, and Detractor review by using Natural Language Preprocessing (NLP).

Deployment: [Click Here!]([https://huggingface.co/spaces/RidwanMS/Airline_Review_Sentiment_Analysis])

## File info
### Main Folder:
- Dataset Airline Passenger Reviews.zip: This is the dataset used in this project, consist of 64,017 customers review. This dataset was acquired from [Kaggle]([https://www.kaggle.com/datasets/malharkhatu/airline-passenger-reviews/data])
- P2G7_Ridwan-Syahrul.ipynb: This script consist of processing the dataset, which are data loading, exploratory data analysis, data preprocessing, data modeling, model saving.
- P2G7_Ridwan-Syahrul_inference.ipynb: This script consist of code for testing the model saved using inference data.
- model_imp_SimpleRNN.zip: This file is the model used in the P2G7_Ridwan-Syahrul.ipynb script for the sentiment analysis machine learning.
- preprocess.pkl: This script is used for text preprocessing the dataset in P2G7_Ridwan-Syahrul_inference.ipynb script.
  
### Deployment Folder:
- app.py: This script will launch the application by calling other script, which is prediction.py.
- prediction.py: This script will load the model to be used in the sentiment analysis.
- requirements.txt: This is the library list for huggingface to use for the app to work.
