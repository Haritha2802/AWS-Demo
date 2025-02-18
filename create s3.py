import boto3

# Initialize session with credentials (if not using aws configure)
session = boto3.Session(
    aws_access_key_id="AKIAUPMYNM4IHDIE7ZNI",
    aws_secret_access_key="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",
    region_name="us-east-1"
)

# Create S3 client
s3_client = boto3.client("s3")

# Create an S3 bucket
bucket_name = "my-unique-bucket-12344566"
region = "us-east-1"

s3_client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={"LocationConstraint": region}
)


print(f"Bucket {bucket_name} created successfully.")

# List all S3 buckets
response = s3_client.list_buckets()
print("Existing Buckets:")
for bucket in response["Buckets"]:
    print(bucket["Name"])
