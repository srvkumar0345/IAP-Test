provider "aws" {
  region = "us-west-2"
}

resource "aws_eks_cluster" "this" {
  name     = "my-k8s-cluster"
  role_arn = aws_iam_role.eks.arn

  vpc_config {
    subnet_ids = ["subnet-abc123", "subnet-def456"]
  }
}

resource "aws_eks_node_group" "node" {
  cluster_name    = aws_eks_cluster.this.name
  node_group_name = "example"

  scaling_config {
    desired_size = 2
    max_size     = 3
    min_size     = 1
  }

  instance_types = ["t2.medium"]
}
