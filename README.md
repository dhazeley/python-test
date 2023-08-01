# pqaas-model

## Requirements

- Python 3
- Pipenv

## Project Setup

- Install all dependencies
  `pipenv install --dev`

- Copy the `.env.example` file into your own `.env` file. ENV variable updates should be made in `.env` and is never comitted to git.

- Run development server
  `pipenv run dev`

- Send an example[/examples.http] request to the API at: `localhost:6000`

## Contribution

This project has a Dev, QA, and Production environment. In order to make contributions, create a PR into the `main` branch. A deployment will automatically be made targeting to the Dev environment.

If you want to redeploy your code to the Dev environment, run a new [DEV Cloud Run Deploy](https://github.com/colex-th/pqaas-firebase/actions/workflows/dev.yml) workflow.

Upon merge to the `main` branch, a new QA deployment will be made.
