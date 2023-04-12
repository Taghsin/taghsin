#!/bin/bash

# Set the path to the SAM template file
template_file="template.yaml"

# Display help message and exit
function show_help {
  echo "Usage: $0 [-h] [--region region_name] [--profile profile_name] [--stackName stack_name] [--bucketName bucket_name]"
  echo "Deploy an AWS SAM  Taghsin application using CloudFormation"
  echo ""
  echo "  -h                  Display this help message and exit"
  echo "  --region            The AWS region to use for deployment (default: us-east-1)"
  echo "  --profile           The AWS profile to use for deployment (optional)"
  echo "  --stackName         The name of the CloudFormation stack to create or update"
  echo "  --bucketName        Optional: the name of an S3 bucket to use for deployment artifacts"
  echo "                      If not specified, a new bucket will be created with a unique name"
  exit 0
}

# Set the default region and profile
region="us-east-1"
profile="default"

# Set the default stack and bucket names
stack_name=""
bucket_name=""

# Set the parameters based on user input
while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    -h)
      show_help
      ;;
    --region)
      region="$2"
      shift
      shift
      ;;
    --profile)
      profile="$2"
      shift
      shift
      ;;
    --stackName)
      stack_name="$2"
      shift
      shift
      ;;
    --bucketName)
      bucket_name="$2"
      shift
      shift
      ;;
    *)
      echo "Invalid option: $key"
      show_help
      ;;
  esac
done

if [[ -z "$stack_name" ]]; then
  echo "Error: stackName parameter is required."
  show_help
fi

if [[ -z "$bucket_name" ]]; then
  # Generate a unique bucket name based on the current date/time
  bucket_name="sam-deploy-$(date +%Y%m%d%H%M%S)"
fi

# Check if the bucket already exists, create it if it doesn't
if ! aws s3 ls "s3://$bucket_name" --region "$region" --profile "$profile" 2>&1 | grep -q 'NoSuchBucket'; then
  echo "Using existing S3 bucket: $bucket_name"
else
  echo "Creating S3 bucket: $bucket_name"
  aws s3 mb "s3://$bucket_name" --region "$region" --profile "$profile"
fi

# Package the application and upload to S3
echo "Packaging application..."
sam package \
  --template-file $template_file \
  --output-template-file packaged.yaml \
  --s3-bucket $bucket_name \
  --region "$region" \
  --profile "$profile"

# Deploy the application using CloudFormation
echo "Deploying application..."
sam deploy \
  --template-file packaged.yaml \
  --stack-name $stack_name \
  --capabilities CAPABILITY_IAM \
  --region "$region" \
  --profile "$profile"
