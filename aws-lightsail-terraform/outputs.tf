output "news_snippet_instance_ip" {
  value = aws_lightsail_instance.my_instance.public_ip_address
}

output "news_snippet_instance_name" {
  value = aws_lightsail_instance.my_instance.name
}