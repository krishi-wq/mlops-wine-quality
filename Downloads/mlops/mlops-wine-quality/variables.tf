variable "public_key_path" {
  description = "Path to your SSH public key"
  default     = "~/.ssh/id_rsa.pub"
}

variable "github_username" {
  description = "GitHub username"
  type        = string
}

variable "repo_name" {
  description = "GitHub repository name"
  type        = string
}
