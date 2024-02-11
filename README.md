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


# Task 4: Cost Analysis

## Overview
This section provides a cost analysis for the Lambda function based on the provided specifications and pricing information.

## Assumption
- Allocated Memory for Lambda Function: 3072 MB
- Average Execution Time: 3.5 seconds
- Number of Invocations per hour: 1000,000
- 30 days in a month
- Price per GB-second for 3072 MB RAM: $0.00005
- Request Cost: $0.20 per 1M requests

## Cost Calculation
1.**Lambda Pricing Formula:**
  Total Cost = [Total Invocation per month * (Execution Duration Price * Price per GB-second)] + Total Request Cost


2. **Duration Cost per Invocation:**
   - Calculate the execution duration price:
     ```
     Execution Duration Price = Memory Allocated * Time to Run Job
                         = 3.072 GB * 3.5 seconds
                         = 10.752 GB-seconds
     ```
   - Calculate the duration cost per invocation:
     ```
     Duration Cost per Invocation = Execution Duration Price * Price per GB-second
                                   = 10.752 GB-seconds * $0.00005
                                   = $0.0005376
     ```

3. **Request Cost:**
   - Number of Invocations per day : 1000,000
    ```
     Number of Invocation per month = (Number of Invocations per day * 24) * 30
                        = (1,000,000 * 24) * 30
                        = 720,000,000
     ```


   - Cost per 1M requests: $0.20
   - Total Request Cost:
     ```
     Total Request Cost = (Number of Invocations per Month / 1,000,000) * Request Cost
                        = (720,000,000 / 1,000,000) * $0.20
                        = $144.00
     ```

4. **Total Monthly Cost:**
   - Calculate the total monthly cost by summing the duration cost per invocation and the request cost:
     ```
     Total Monthly Cost = (Duration Cost per Invocation * Number of Runs) + Total Request Cost
                        = ($0.0005376 * 720,000,000) + $144.00
                        = $387,072 + $144.00
                        = $387,216
     ```

## Summary 
Based on the provided specifications and pricing information, the expected monthly cost for the Lambda function is approximately $387,216 USD.

## Suggestion

### Optimize Memory Allocation

Evaluate the memory requirements of the Lambda function and adjust the allocated memory accordingly. This can be achieved by continuously analyzing historical usage patterns and performance metrics. Determine if the current memory allocation is optimal. In some cases, reducing memory allocation can lead to significant cost savings without impacting performance. AWS CloudWatch is a valuable tool for monitoring Lambda performance, and when coupled with CloudWatch Insights monitoring, it can result in significant cost optimization 



