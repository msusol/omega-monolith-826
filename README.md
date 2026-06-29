# omega-monolith-826

Working Website:

- [Google App Engine](http://omega-monolith-826.appspot.com/) a.k.a. [www.marksusol.com](http://www.marksusol.com)

## Deployment

```zsh
omega-monolith-826% gcloud auth login
omega-monolith-826% gcloud app deploy app.yaml

Services to deploy:

descriptor:                  [/Users/marksusol/LosusAI/Projects/Website/omega-monolith-826/app.yaml]
source:                      [/Users/marksusol/LosusAI/Projects/Website/omega-monolith-826]
target project:              [omega-monolith-826]
target service:              [default]
target version:              [20260221t203832]
target url:                  [https://omega-monolith-826.appspot.com]
target service account:      [omega-monolith-826@appspot.gserviceaccount.com]

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse
```