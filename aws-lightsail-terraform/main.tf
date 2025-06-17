# Create a Lightsail instance for the news-snippet application
resource "aws_lightsail_instance" "my_instance" {
  name              = "news-snippet"
  availability_zone = "us-east-1a"
  blueprint_id      = "ubuntu_20_04"
  bundle_id         = "micro_2_0"

  tags = {
    Name = "news-snippet Lightsail Instance"
  }
}
# ----------------------------------------------------------------------------------
# The following resources create and attach a static IP to the Lightsail instance
# ----------------------------------------------------------------------------------
resource "aws_lightsail_static_ip" "my_static_ip" {
  # Assign a static IP to the Lightsail instance
  name = "news-snippet"
}
# This resource creates an AWS S3 bucket with the specified configuration.
# 
# Arguments:
#   bucket        - (Required) The name of the bucket. Must be globally unique.
#   acl           - (Optional) The canned ACL to apply. Defaults to "private".
#   tags          - (Optional) A mapping of tags to assign to the bucket.
#
# Example:
#   resource "aws_s3_bucket" "example" {
#     bucket = "my-unique-bucket-name"
#     acl    = "private"
#     tags = {
#       Environment = "Dev"
#     }
#   }
#
# For more information, see the AWS provider documentation:
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket
resource "aws_lightsail_static_ip_attachment" "my_static_ip_attachment" {
  static_ip_name = aws_lightsail_static_ip.my_static_ip.name
  instance_name  = aws_lightsail_instance.my_instance.name
}