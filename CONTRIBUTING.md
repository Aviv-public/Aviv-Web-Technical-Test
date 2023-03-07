# CONTRIBUTION

## Requirements

### Pre-commit hook

[Pre-commit](https://pre-commit.com/#install) is used to trigger automatically pre-commit checks.
For now, the pre-commit config will check that we don't leak any secrets nor password when committing.

Using Pip
````shell
pip install pre-commit
````

Using HomeBrew
```shell
brew install pre-commit
```

Then, 
```shell
pre-commit install
```
