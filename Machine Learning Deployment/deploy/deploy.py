import boto3

sagemaker = boto3.client('sagemaker')

# Define model settings
model_name = 'mnist-model'
model_data = 's3://your-bucket/model/model.h5'
role = 'arn:aws:iam::your-account-id:role/your-sagemaker-role'

# Create model
response = sagemaker.create_model(
    ModelName=model_name,
    PrimaryContainer={
        'Image': '763104351884.dkr.ecr.us-west-2.amazonaws.com/tensorflow-inference:2.4.1-cpu',
        'ModelDataUrl': model_data
    },
    ExecutionRoleArn=role
)

print(response)
