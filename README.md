# Customer transcation Prediction
This repository is about solving [Customer Transaction Prediction](https://www.kaggle.com/competitions/santander-customer-transaction-prediction/overview) using LightGBM and its deployment in Flask and Streamlit app.


This repository contains the end to end ML training , deployment and containerizing ML pipeline using docker.

The dataset for the problem is available in [Kaggle](https://www.kaggle.com/competitions/santander-customer-transaction-prediction/data)

I have used LightGBM for this purpose. 
LightGBM model is highly efficient and fast because the gradient boosting tree is created leaf wise. XGBoost is slower as compared to LightGBM due 
to its level wise gradient boosting tree development. 


![Screenshot-from-2019-03-27-23-09-47-1](https://user-images.githubusercontent.com/65164450/210341753-4ff347f3-875e-4731-831c-65e68086a7ad.jpg)
Hence LightGBM is widely used in market data and transaction prediction data because it gives higher accuracy and it is lesser prone to overfit.
Steps:
## Installation 
Clone this repository:

```
git clone https://github.com/A0158/Try-on.git
cd ./Try-on/
```
Install dependencies:

```
pip install requirements.txt
```
## Training the model and loading model
1) Steps to preprocess data and run the model and inference in given in [Jupyter Notebook](https://github.com/A0158/Market-Prediction/blob/main/marketprediction.ipynb)

2) The model is loaded in [classifier.pkl](https://github.com/A0158/Market-Prediction/blob/main/classifier.pkl)

## Run the model in app using this command:

```
python run flaskapp.py
```
## Steps to dockerize the container
```
docker build -t name:tag .
```

## Run the docker
```
docker run -p 127.0.0.1:80:8080/tcp ubuntu bash
```
If you want to understand about dockers  check [Docker manual](https://docs.docker.com/desktop/)

## Install the streamlit app
```
pip install streamlit
```

## Run streamlit app
```
streamlit run streamapp.py
```


