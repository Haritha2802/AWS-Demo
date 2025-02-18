import boto3

s3 = boto3.client('s3')

import boto3
s3_resource = boto3.resource("s3")



import boto3

# Create an S3 client specifying the region explicitly
s3_client = boto3.client("s3", region_name="us-east-1")

bucket_name = "my-unique-bucket-12344566"

# Remove the LocationConstraint for us-east-1
s3_client.create_bucket(Bucket=bucket_name)

print(f"Bucket {bucket_name} created successfully.")

response = s3_client.list_buckets()
for bucket in response["Buckets"]:
    print(bucket["Name"])
