# Portfolio Website

A streamlit based webapp deployed at [here](https://portfolio-website-2h1e.onrender.com/)

#### To build your own website like, go through the below information and follow the steps!!

## Contents

- LinkedIn Badge : [how to create one for your profile?](https://www.linkedin.com/pulse/how-create-linkedin-badge-your-website-amy-wallin/). Integrated using streamlit component
- Career Snapshot: Built using [streamlit_timeline](https://pypi.org/project/streamlit-timeline/)
- Skills & Tools: Used streamlit buttons & columns features
- Education : Plotly(library for visualization) table

## Files description
* images/ : images used for research paper section
* pdfs/ : pdfs available for downloading on portfolio
* constant.py : File with all static data used. 
* requirements.txt : requirements file generated using [pipreqs](https://pypi.org/project/pipreqs/)
* timeline.json : Json file used by streamlit_timeline for career snapshot
* send_mail.py : pythno file to support mail sending mails from the website by the users
* data.csv : CSV file containing info on all the projects
* streamlit_app.py : main python file consisiting of web app code

## How to deploy using Streamlit?
* Once confirm your app runds fine on localhost. Check using 
```
streamlit run streamlit_app.py 
```
* Create requirements.txt. 
* Push repo to github.
* Sign in to Streamlit and create a new app. 
* Fill in the info for the app and connect to your github repo where the application files are stored. 
* Cross-verify the info and deploy.

### If your app is error free, it should get deployed !!
If it doesn't then you can check the streamlit deployment logs and rectify the issue.
