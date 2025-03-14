#!/bin/bash

# Export AWS credentials as environment variables (more secure)
export AWS_ACCESS_KEY_ID="*******"
export AWS_SECRET_ACCESS_KEY="******"
export AWS_DEFAULT_REGION="us-west-2"

# Create AWS credentials file with restricted permissions
mkdir -p ~/.aws
cat > ~/.aws/credentials << EOF
[default]
aws_access_key_id = ${AWS_ACCESS_KEY_ID}
aws_secret_access_key = ${AWS_SECRET_ACCESS_KEY}
region = ${AWS_DEFAULT_REGION}
EOF

chmod 600 ~/.aws/credentials

echo "AWS credentials configured securely." 