## California House Pricing Prediction

### Software and Tools Requirement

1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [Git CLI](https://git-scm.com/downloads)

### Steps

1. Create a new environment
```
virtualenv -p python==3.9 venv
```
2. Analyse the data and create a ML Model

3. Create the Pickle files for scaling and linear regression model

    - Scaling pickle file will be used to scale the new data.
    - Linear regression model pickle file is used to predict the price based on scaled data.

4. Develop the web app using Flask

5. Create the Dockerfile and Github actions to deploy on Heroku 

