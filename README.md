# Real-Estate-House-price-Prediction
![Screenshot](https://user-images.githubusercontent.com/2795092/211560402-4dd6fc96-c22c-4f63-aa2e-7214ebf9cf81.JPG)
**dataset:** https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

This data science project walks through step by step process of how to build a real estate price prediction website. 
* **first**: we will build a model using SKLearn framework. We try algorithms: **Linear Regression, Lasso Regression, Decision Trees** using banglore home prices dataset from kaggle.com.
* **Second** step would be to write a python flask server that uses the saved model to serve http requests.
* **Third** component is the website built in html, css and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price.
* During model building we have gone through all steps of a data science project such as data load and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation etc. Technology and tools wise this project covers:

* Python
* Numpy and Pandas for data cleaning
* Matplotlib for data visualization
* Sklearn for model building
* Jupyter notebook, visual studio code and pycharm as IDE
* Python flask for backend
* HTML/CSS/Javascript for frontend UI
* Deploy the app to Amazon cloud (EC2)

# Installation steps
Git clone the repo
```
git clone https://github.com/Anirbanbhk88/Real-Estate-House-price-Prediction.git
```

Create a python Virtual environment and install dependencies from requirements.txt
```
pip install -r requirements.txt
```

Set the Flask environment variable and Run the Flask server
```
cd BHP/server
export FLASK_APP=server.py
flask run
```
