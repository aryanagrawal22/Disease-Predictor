# Disease-Predictor

## A responsive & ergonomic website to predict the disease from given symptoms and health parameters using machine learning algorithms.

### Repo Info - There are *three branches*

#### 1) Main - Contains Readme File (Project Info)
#### 2) Server - Contains Web Hosted Project (Node)
#### 3) API - Contains ML Hosted Project (FastAPI)

### Overview :
The model predicting the disease is trained in using Machine Learning and then using a Framework called FastAPI (like flask) in python,  the model is loaded and hosted on a web hosting service. This then acts as an API that receives and sends predictions and graphs as a result to our main backend server. On the Frontend when the user input the data into the parameters, the data is sent to the backend, and then to the API  which is then predicting the outcome of the model. The result is then displayed on the frontend when received on the server.

### Hosted Link :

#### -- Website :
[![Link](https://api.iconify.design/bx/bx-link-external.svg?color=white&width=40&height=40)](https://disease-predict-website.herokuapp.com/)

#### -- ML API :
[![Link](https://api.iconify.design/bx/bx-link-external.svg?color=white&width=40&height=40)](https://disease-predict-api.herokuapp.com/docs)

### Features :

- Predicts disease by given symptoms and health parameters
- 3 types of disease prediction ( heart, stroke and hepatitis)
- Extensive comparsion of parameters is given through a graph
- High accuracy and easy to use interface

### Tech :

Disease Predictor uses a number of different technologies like: <br/> <br/>
![Python](https://api.iconify.design/akar-icons/python-fill.svg?color=white&width=50&height=50)
![FastAPI](https://api.iconify.design/simple-icons/fastapi.svg?color=white&width=50&height=50)
![ScikitLearn](https://api.iconify.design/simple-icons/scikitlearn.svg?color=white&width=50&height=50)
![Numpy](https://api.iconify.design/file-icons/numpy.svg?color=white&width=50&height=50)
![Pandas](https://api.iconify.design/simple-icons/pandas.svg?color=white&width=50&height=50)
![Node,js](https://api.iconify.design/akar-icons/node-fill.svg?color=white&width=50&height=50)
![EJS](https://api.iconify.design/file-icons/ejs.svg?color=white&width=50&height=50)
- [FastAPI] - Fast web framework for building APIs with Python
- [Scikit-learn] - Tools for predictive data analysis
- [Matplotlib] - Library for creating static, animated, and interactive visualizations
- [Numpy] -  Library used for working with array, algebra and matrices
- [Pandas] - Library used for data analysis
- [Node.js] - Evented I/O for the backend
- [Express] - Fast node.js network app framework 
- [EJS] - Embedded JavaScript templating engine
