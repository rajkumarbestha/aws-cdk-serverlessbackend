
# AWS CDK for Serverless Backend in Python
![python 3.5 3.6 3.7](https://img.shields.io/badge/python-%3E3.6-blue) ![AWS CDK](https://img.shields.io/badge/aws--cdk.core-1.62.0-brightgreen)

This project uses the [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) (Cloud Development Kit), an Amazon Toolkit to define IaC (Infrastructure as Code) using Python. AWS CDK converts the implemented code to CloudFormation (which uses an AWS syntax to describe and provision all the infrastructure resources in AWS).

## Features

In this project we have implemented an AWS CDK app to deploy a simple AWS serverless infrastructure. It deploys the following AWS services:
* Lambda - a sample lambda
* Cloudwatch Rule Trigger - which triggers the lambda based on cron or rule defined
* RDS Mysql Instance - Basic free tier Mysql RDS
* API Gateway (with cors support) - which calls the lambda
* S3

The goal is to define a simple infrastructure that we can use in all the projects as well as introduce specific aspects (which might not necessarily be needed in this project but might be useful in other more complex projects or with a specific purpose). 

The Resources can be easily adapted to a non-serverless architecture also.

## Usage
To manually create a virtualenv on MacOS, Linux or Windows:

```
$ python -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```
Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```
After running the above command, you can find the CloudFormation Template in the cdk.out directory, validate and deploy using

```
$ cdk deploy
```
 
## Understand the Structure

* `app.py`: Entry point to the CDK App.
* `cdk.json`: A configuration file that defines how to execute the application.
* `cdk.out/*`: When cdk synth is executed, CloudFormation templates are placed under this directory. These files are used for deploying the insfrastrure with cdk deploy
* `serverlessbackend/libs`: Library files, i.e. custom resources. The reason why we separated the resource classes from the ServerlessBackend Stack is that the custom resource classes can be enforced with organizational or the general best practices and the users can use them inside the stack as is. 
* `serverlessbackend/config.properties`: List of config values provided.
* `serverlessbackend/serverless_backend.py`: This is where the CloudFormation template gets created.

## Other Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Still, there is a lot of room for improvement. Hope this will be useful.

Happy Learning!
