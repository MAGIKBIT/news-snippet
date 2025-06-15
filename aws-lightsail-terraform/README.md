# AWS Lightsail Terraform Deployment

This project provides a Terraform configuration for deploying resources on AWS Lightsail. It includes the necessary files to set up instances, networking, and other services using Terraform.

## Project Structure

- `main.tf`: Contains the main configuration for the Terraform deployment, defining the resources to be created on AWS Lightsail.
- `variables.tf`: Defines the input variables for the Terraform configuration, specifying types and default values.
- `outputs.tf`: Specifies the output values that Terraform will display after deployment, such as instance IP addresses.
- `provider.tf`: Configures the AWS provider, including credentials and region settings.

## Prerequisites

- Terraform installed on your local machine.
- An AWS account with permissions to create Lightsail resources.
- AWS credentials configured in your environment.

## Setup Instructions

1. Clone this repository to your local machine.
2. Navigate to the project directory:
   ```
   cd aws-lightsail-terraform
   ```
3. Update the `variables.tf` file with your desired configuration values.
4. Initialize Terraform:
   ```
   terraform init
   ```
5. Plan the deployment:
   ```
   terraform plan
   ```
6. Apply the configuration to create the resources:
   ```
   terraform apply
   ```

## Outputs

After the deployment is complete, Terraform will display the output values defined in `outputs.tf`, which may include instance IP addresses and other relevant information.

## Cleanup

To remove the resources created by Terraform, run:
```
terraform destroy
```

This will delete all resources defined in the configuration.