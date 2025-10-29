provider "aws" {
  region = "us-east-1"
}

resource "aws_key_pair" "deployer" {
  key_name   = "mlops-key"
  public_key = file(var.public_key_path)
}

resource "aws_security_group" "allow_http" {
  name        = "allow_http"
  description = "Allow HTTP and SSH inbound traffic"

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "mlops_vm" {
  ami           = "ami-0c55b159cbfafe1f0" # Update with correct AMI for your region
  instance_type = "t2.micro"
  key_name      = aws_key_pair.deployer.key_name
  security_groups = [aws_security_group.allow_http.name]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y python3 git
              git clone https://github.com/${var.github_username}/${var.repo_name}.git /home/ec2-user/mlops-app
              cd /home/ec2-user/mlops-app
              python3 -m pip install --upgrade pip
