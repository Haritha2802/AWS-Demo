# AWS
# AWS CLI, IAM, S3, and AWS Glue

## AWS CLI
AWS Command Line Interface (CLI) is a tool that enables users to interact with AWS services using command-line commands. It provides an efficient and automated way to manage AWS resources without using the AWS Management Console. The AWS CLI supports multiple operating systems and can be integrated into scripts and automation workflows.

### Features of AWS CLI:
- Simplifies interaction with AWS services.
- Supports automation through scripts.
- Cross-platform compatibility (Windows, macOS, Linux).
- Configurable with multiple profiles and credentials.

### Importance of AWS CLI:
- Reduces the time required for managing AWS services.
- Enhances automation and scalability of cloud-based operations.
- Helps in bulk operations and batch processing of AWS resources.

### Basic AWS CLI Commands:
- aws configure – Configures the AWS CLI with access key, secret key, region, and output format.
- aws s3 ls – Lists S3 buckets.
- aws ec2 describe-instances – Retrieves details of EC2 instances.
- aws iam list-users – Lists IAM users in the AWS account.

![alt text](Assests/terminal.png)




## AWS IAM (Identity and Access Management)
AWS IAM is a security service that enables organizations to manage user access to AWS resources securely. It helps define **who** can access **what** AWS resources and under **what conditions**.

### Key Concepts of IAM:
- **IAM Users:** Represent individuals who have access to AWS resources.
- **IAM Groups:** Collections of IAM users with similar access permissions.
- **IAM Roles:** Temporary permissions that can be assigned to users or AWS services.
- **IAM Policies:** JSON-based permissions that define access rules.
- **MFA (Multi-Factor Authentication):** Enhances security by requiring additional authentication steps.

### Benefits of IAM:
- Improves security and access control.
- Helps enforce least privilege principles.
- Enables centralized user management and monitoring.

![alt text](Assests/Picture1.png)
![alt text](Assests/Picture2.png)
![alt text](Assests/Picture3.png)
![alt text](Assests/Picture4.png)
![alt text](Assests/Picture9.png)
![alt text](Assests/Picture10.png)
![alt text](Assests/Picture11.png)
![alt text](Assests/Picture12.png)
![alt text](Assests/Picture13.png)
![alt text](Assests/Picture14.png)
![alt text](Assests/terminal2.png)




## Amazon S3 (Simple Storage Service)
Amazon S3 is an object storage service that provides highly scalable, secure, and durable cloud storage for a wide range of applications.


### Key Features of S3:
- **Scalability:** Handles unlimited data storage.
- **Durability:** Offers 99.999999999% (11 9’s) durability.
- **Security:** Supports encryption, IAM policies, and bucket policies.
- **Lifecycle Management:** Automatically transitions objects to different storage classes.
- **Versioning:** Keeps multiple versions of an object to protect against accidental deletions.

### Use Cases of Amazon S3:
- Backup and disaster recovery.
- Hosting static websites and media content.
- Data archiving and long-term storage.
- Big data analytics and machine learning.

![alt text](Assests/Picture6.png)
![alt text](Assests/Picture7.png)
![alt text](Assests/Picture8.png)
![alt text](Assests/Picture15.png)
![alt text](Assests/Picture16.png)
![alt text](Assests/Picture17.png)
![alt text](Assests/Picture18.png)
![alt text](Assests/Picture19.png)
![alt text](Assests/Picture20.png)
![alt text](Assests/Picture21.png)
![alt text](Assests/Picture22.png)
![alt text](Assests/Picture23.png)
![alt text](Assests/Picture24.png)
![alt text](Assests/Picture25.png)
![alt text](Assests/Picture26.png)
![alt text](Assests/Picture27.png)
![alt text](Assests/terminal3.png)



## AWS Glue
AWS Glue is a serverless data integration service that simplifies the process of discovering, preparing, and transforming data for analytics and machine learning applications.It is commonly used for ETL (Extract, Transform, Load) workflows.


### Components of AWS Glue:
- **Glue Data Catalog:** A centralized repository that stores metadata about datasets.
- **Glue Crawlers:** Automatically scans data sources to create metadata.
- **Glue ETL Jobs:** Processes data using Python or Apache Spark-based transformations.
- **Glue Triggers:** Automates job execution based on schedules or events.

### Benefits of AWS Glue:
- Automates data preparation and transformation.
- Reduces operational overhead with a fully managed service.
- Integrates seamlessly with AWS analytics and data lakes.
- Supports multiple data formats and storage options.

### Common Use Cases:
- Extracting, transforming, and loading (ETL) data for analytics.
- Creating and managing data catalogs for data lakes.
- Integrating with Amazon Redshift, S3, and other AWS services for data processing.

### Glue Database:
- In AWS Glue, a database is a logical container used to organize and store metadata about your data. It does not store the actual data but keeps track of where data is stored (e.g., in Amazon S3), its schema, and other relevant information.

## Key Features of an AWS Glue Database:
- Metadata Storage: Stores table definitions, schemas, and data locations in the AWS Glue Data Catalog.
- Logical Organization: Helps categorize tables based on use cases, projects, or departments.
- Integration with Other AWS Services: Works with Athena, Redshift Spectrum, and EMR for querying and processing data.
- Supports Multiple Data Sources: Can store metadata for data stored in Amazon S3, RDS, Redshift, DynamoDB, and external sources.

- Create an AWS Glue database named "project_db".
- Within this database, define tables such as "customers", "orders", and "products".
- Query these tables using AWS Athena or process them using AWS Glue ETL jobs.

![alt text](Assests/Picture28.png)
![alt text](Assests/Picture29.png)
![alt text](Assests/Picture30.png)


### AWS Glue Tables
- Key Components of an AWS Glue Table
- Table Name – A unique name identifying the table within an AWS Glue database.
- Database – Every table belongs to a specific Glue database, which acts as a logical grouping.
- Schema (Column Definitions) – Defines column names, data types (e.g., string, integer, timestamp), and partition keys.
- Data Format – Specifies the format of the stored data, such as Parquet, ORC, Avro, JSON, CSV, etc..
- Location – The S3 path or data source location where the actual data resides.
- Partitioning (Optional) – Helps improve query performance by organizing data into partitions (e.g., by year, month, or region).
- Input/Output Format – Defines how data should be read and written (e.g., using Apache Hive SerDe for CSV or Parquet).

![alt text](Assests/Picture31.png)
![alt text](Assests/Picture32.png)
![alt text](Assests/Picture33.png)
![alt text](Assests/Picture34.png)
![alt text](Assests/Picture35.png)
![alt text](Assests/Picture36.png)
![alt text](Assests/Picture37.png)


