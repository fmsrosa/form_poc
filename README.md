## Overview

This project consists in a Streamlit App running locally or in Streamlit Cloud.

It is a POC showcasing a form containing:
1. A numerical question
2. A checkbox question
3. A dropdown question
4. A map question
5. An upload to Google Drive Account
6. A Submit button

Other than the upload to Google Drive Account, that occurs after clicking Submit, the rest is not used in any further operation.

App is deployed at [https://formpoc-dakba4brtxrjoca3mi2z6f.streamlit.app/](https://formpoc-dakba4brtxrjoca3mi2z6f.streamlit.app/)

## Repository structure

```
├── .gitignore                <- Directories and files to be ignored by git
├── .poetry.lock              <- Current poetry settings.
├── .pre-commit-config.yaml   <- Settings for pre-commit
├── .python-version           <- Current Python version
├── .streamlit
│   ├── secrets.toml          <- Secrets to be used by streamlit.
│
├── app.py                    <- Streamlit App
│
├── data
│   ├── external              <- Data from third party sources.
│   ├── processed             <- Data that has been transformed.
│   ├── raw                   <- The original, immutable data dump.
│   └── user_output           <- User output data.
│
├── docs                      <- Markdowns with pertinent documentation.
│
├── notebooks                 <- Jupyter notebooks. Naming convention is a zero followed by a number,
│                                if the number has single digit, or just the number if it has more
│                                than one digit, followed by the creator's initials, and a short
│                                `-` delimited description, e.g.`10-jqp-initial-data-exploration`.
│
├── pyproject.toml            <- Project configuration file with package metadata.
│
├── README.md                 <- The top-level README for developers using this project.
│
├── requirements.txt          <- List of packages installed.
│
├── streamlit_rfm_app         <- Package folder
│   └── __init__.py           <- Init file representing package.
│
└── templates                   <- HTML templates.
```

## Using Google Drive Upload

### Create a Service Account

**You need a Google Account for this part.**

Create a service account following. Instructions at 
[https://developers.google.com/android/management/service-account](https://developers.google.com/android/management/service-account).

Do not forget to enable access to Google Drive API.

The service account will only have access to enabled APIs.

### Create a new key

In your service account, under "Keys", click on "Add Key" -> "Create new key".

This will download a json file.

### Convert .json to .toml

Since streamlit.secrets expects a .toml and we will want to deploy the app on Streamlit Cloud, you need to convert your .json file to a .toml.

You can do this manually.

For more information regarding on secret management on Streamlit check [https://docs.streamlit.io/develop/api-reference/connections/secrets.toml](https://docs.streamlit.io/develop/api-reference/connections/secrets.toml).

## Run locally

To run locally, install poetry env or the packages using requirements.txt and run `streamlit run app.py`.

If you are using Poetry, do not forget to activate the environment.

## Deploy on Streamlit Cloud

### Commit code to Github

You will need to commit your code to a Github repo and make it public first.

### Login in Streamlit Cloud

You can login at [https://share.streamlit.io/](https://share.streamlit.io/) using your Github account.

### Create your app

Click "Create App" and "Create App from Github repository" and select your repository.

### Add secrets

In your main page on Streamlit, click on the three dots menu of your app, and Settings.

Copy the content of your .streamlit/secrets.toml to "Secrets".

Redeploy your app.