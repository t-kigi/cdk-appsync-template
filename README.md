# cdk-appsync-template

This is a basic project to create AWS AppSync API by CDK Python.


# Setup

## AWS Profile

You need to get IAM programic access and setup them as your profile. 

```
$ aws configure --profile <your profile>
... (setup your configurations)
```


## Install CDK CLI

Run following and install cdk command if needed.

```
$ npm install -g aws-cdk
```

## Python Virtual Environment

- Precondition: you can use `pipenv` .
- Recommendation: you can use `pyenv` .

At first, it needs to create python virtual environment by pipenv.

```
$ git clone git@github.com:t-kigi/cdk-appsync-template.git
$ cd cdk-appsync-template
$ pipenv install
```

If this is first time to use `aws cdk` on your AWS account / region, you run following at once.

```
$ pipenv run cdk bootstrap --profile <your profile>
```

# How to use

```
# deploy (and update)
$ pipenv run cdk deploy --profile <your profile>

# destory
$ pipenv run cdk destory --profile <your profile>
```

# LICENSE

Apache License Version 2.0
