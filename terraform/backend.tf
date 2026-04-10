terraform {
  backend "s3" {
    bucket = "particle41-test-bucket-backend"
    key    = "backend"
    use_lockfile = true
    region = "us-east-1"
  }
}
