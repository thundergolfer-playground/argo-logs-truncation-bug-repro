# argo-logs-truncation-bug-repro
Built for the purposes of reproducing https://github.com/argoproj/argo/issues/1717

## Running

### Local

```
pipenv shell
python demo/main.py
```

or `pipenv run python demo/main.py`

### Argo Workflows

```
argo -n argo submit --watch https://raw.githubusercontent.com/thundergolfer-playground/argo-logs-truncation-bug-repro/master/argo-logs-truncation-bug-workflow.yaml
```yaml

## Docker

`docker build .`

