# Deploy to Google App Engine

## Prerequisites

- `gcloud` CLI installed and on PATH
- Access to the `omega-monolith-826` GCP project
- Active GCP authentication (see Step 1)

## Steps

1. **Authenticate with GCP**

   ```zsh
   gcloud auth login
   ```

   Opens a browser for OAuth. Only required once per session or when credentials expire.

2. **Confirm the active project**

   ```zsh
   gcloud config get-value project
   ```

   Expected output: `omega-monolith-826`. If not set:

   ```zsh
   gcloud config set project omega-monolith-826
   ```

3. **Deploy the default service**

   ```zsh
   gcloud app deploy app.yaml
   ```

   Packages and uploads the Flask/gunicorn app on Python 3.12. Static files under `www/`
   are served by GAE handlers; all other routes fall through to Flask (`main.py`).

4. **Deploy dispatch rules** *(only when `dispatch.yaml` changes)*

   ```zsh
   gcloud app deploy dispatch.yaml
   ```

   Routes `dashboard.marksusol.com/*` to the `dashboard` service. The `dashboard` service
   must exist before this takes effect.

## Expected output

```
Services to deploy:

descriptor:             [.../omega-monolith-826/app.yaml]
source:                 [.../omega-monolith-826]
target project:         [omega-monolith-826]
target service:         [default]
target url:             [https://omega-monolith-826.appspot.com]
target service account: [omega-monolith-826@appspot.gserviceaccount.com]
```

## Verify

```zsh
gcloud app browse
```

Stream logs:

```zsh
gcloud app logs tail -s default
```

## Troubleshooting

- **`dispatch.yaml` deploy fails** — the `dashboard` service does not exist yet. Deploy
  it first before applying dispatch rules.
- **Static files not updating** — GAE caches static handlers; a new version deploy
  (`gcloud app deploy`) is required to bust the cache.
- **Auth errors** — re-run `gcloud auth login`; `application-default login` is for ADC
  (SDK/library use) and is not needed for `gcloud app deploy`.
