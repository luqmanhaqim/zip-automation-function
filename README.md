# zip-automation-function
 
# AWS Lambda S3 Object Compression

## Overview
This repository contains the code and infrastructure as code (IAC) to automate the compression of newly added objects in an Amazon S3 bucket using an AWS Lambda function triggered by AWS SAM (Serverless Application Model). The compressed objects are then uploaded back to the same S3 bucket, and the original objects are deleted.

### Objective
The objective of this repository is to achieve the following tasks:

1. **Task 1: AWS Lambda Function**
   - Create an AWS Lambda function using AWS SAM to compress newly added objects in an S3 bucket.
   - The Lambda function is written in Python and triggered every time a new object is added to the S3 bucket.
   - After compression, the Lambda function uploads the compressed object back to the same S3 bucket and deletes the original object.

2. **Task 2: CloudFormation Template**
   - Create an S3 bucket and connect it to the Lambda function using CloudFormation.
   - The CloudFormation template (`template.yaml`) defines the stack including the S3 bucket and Lambda function, ensuring they are deployed together.
     
3. **Task 3: Documentation and Version Control**
   - Commit changes using best practices from the beginning to the end.
   - Push changes to a public repository and add documentation to the project by adding a README file.

## Components

1. **Code (Python)**
   - Contains the Python code for the AWS Lambda function responsible for compressing S3 objects.

2. **Infrastructure as Code (IAC) - CloudFormation**
   - The `template.yaml` file defines the CloudFormation stack including the S3 bucket and Lambda function configurations.

3. **Framework - AWS SAM**
   - Utilizes AWS SAM to define and deploy serverless applications on AWS, simplifying the process of creating and managing Lambda functions and related resources.

4. **CI/CD - GitHub Actions**
   - GitHub Actions are used for continuous integration and deployment, automating the build, test, and deployment process of the Lambda function and CloudFormation stack.
   
## Environment Setup

Follow these steps to set up your development environment:

### 1. Python 3.10

Make sure you have Python 3.10 installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### 2. Create Virtual Environment

Create a virtual environment using `venv` (built-in with Python 3) or `virtualenv`:

```bash
# Using venv
python3 -m venv venv

# Activate virtualenv

# On Windows
.\env\Scripts\activate

# On macOS/Linux
source env/bin/activate
```

## How to Use

1. **Clone Repository :** 
   `https://github.com/luqmanhaqim/zip-automation-function.git`
   
2. **Add GitHub Secrets**
- Add necessary secrets to the GitHub repository's environment secrets. Refer to the table below for the required secrets/ environment variables:

| Environment Variable                  | Description                                      |
|---------------------------------------|--------------------------------------------------|
| PIPELINE_USER_ACCESS_KEY_ID           | AWS Access Key ID for pipeline user              |
| PIPELINE_USER_SECRET_ACCESS_KEY       | AWS Secret Access Key for pipeline user          |
| SAM_TEMPLATE                          | Name of the SAM template file                    |
| TESTING_STACK_NAME                    | Name of the testing CloudFormation stack         |
| TESTING_PIPELINE_EXECUTION_ROLE       | Role for executing the testing pipeline          |
| TESTING_CLOUDFORMATION_EXECUTION_ROLE | Role for executing CloudFormation in testing     |
| TESTING_ARTIFACTS_BUCKET              | Bucket name for storing artifacts in testing     |
| TESTING_REGION                        | AWS region for testing environment               |
| PROD_STACK_NAME                       | Name of the production CloudFormation stack      |
| PROD_PIPELINE_EXECUTION_ROLE          | Role for executing the production pipeline       |
| PROD_CLOUDFORMATION_EXECUTION_ROLE    | Role for executing CloudFormation in production  |
| PROD_ARTIFACTS_BUCKET                 | Bucket name for storing artifacts in production  |
| PROD_REGION                           | AWS region for production environment            |


3. **Push Changes to Trigger Pipeline**
- Push changes to the main branch to trigger the GitHub Actions pipeline, which will build and deploy the Lambda function and CloudFormation stack automatically.

## How to Contribute

1. **Clone Repository:**
   `https://github.com/luqmanhaqim/zip-automation-function.git`


2. **Create Feature Branch**
- Create a new branch from the `main` branch for your feature or bug fix.
  Example command: 
  ```
  git checkout -b feature/new-feature main
  ```

3. **Make Changes**
- Make your changes, commit them, and push to your feature branch.

4. **Create Pull Request**
- Create a pull request from your feature branch to the main branch.
- The pull request will be approved upon code review completion.




