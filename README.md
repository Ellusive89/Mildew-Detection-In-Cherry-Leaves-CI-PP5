# Powdery Mildew Detection In Cherry Leaves
The Powdery Mildew Detector is an application capable of determining the health status of cherry leaves by identifying if they have powdery mildew. By analyzing an image of a cherry leaf, the app can discern whether the leaf is healthy or affected.

This application utilizes a supervised binary classification machine learning model, with the binary classifier being responsible for predicting the results.


## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.


## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* List here your project hypothesis(es) and how you envision validating it (them).


## The rationale to map the business requirements to the Data Visualisations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.


## ML Business Case
* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.


## Dashboard Design

### Wireframes:
![Project_Summary](assets/wireframes/Project%20Summary.png)
![Leaves_Visualizer](assets/wireframes/Leaves%20Visualizer.png)
![Mildew_Detection](assets/wireframes/Mildew%20Detection.png)
![Project_Hypothesis](assets/wireframes/Hypothesis%20and%20Validation.png)
![ML_Performance](assets/wireframes/ML%20Performance.png)


## Deployment

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries

### Languages

* Python

### Frameworks and associated technologies

* Git: Git served as the version control tool, with commits being made through the Gitpod terminal and subsequently pushed to GitHub,
* GitHub: This platform was employed to house the project's code after it was transferred from Git,
* Balsamiq: This tool was utilized for crafting wireframes,
* Heroku: This container-centric cloud service was used for deploying the project,

### Libraries for Data Analysis and Machine Learning
* Numpy: An open-source Python library designed for array operations. It boasts extensive mathematical functions, random number capabilities, and linear algebra routines,
* Matplotlib: A cross-platform Python library for visualizing data and creating graphical plots,
* Seaborn: A Python-based data visualization library built on Matplotlib, primarily used for visualizing random distributions,
* Pandas: An open-source Python package tailored for handling datasets. It provides tools for data analysis, cleaning, exploration, and manipulation,
* Plotly: An interactive, open-source graphing library for browsers, especially useful for creating visual presentations within Jupyter notebooks,
* Streamlit: A tool designed for creating web applications tailored to data science and machine learning tasks,
* Tensorflow: An open-source platform specializing in deep neural networks for machine learning,
* Shutil: A utility module for file copying and deletion,
* Joblib: Offers a collection of tools for creating lightweight pipelines in Python,
* PIL: Stands for Python Imaging Library, which is a free, open-source library enhancing Python's capabilities in opening, editing, and saving a variety of image file formats,


## Credits

* [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew#Tree_leaves) for informations about powdery mildew,
* [Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.ap) for emoji used in the app,
* [Cherry Powdery Mildew](https://ca.decisionaid.systems/articles/cherry_powdery_mildew) for more information about powdery mildew,
* [Streamlit](https://docs.streamlit.io/library/api-reference/status) for information about Streamlit,
* CI Slack for trubleshooting,


## Acknowledgements
* Thank the people that provided support throughout this project.
