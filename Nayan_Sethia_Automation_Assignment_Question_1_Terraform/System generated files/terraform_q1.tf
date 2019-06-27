#declarartion of provider
provider "aws" {
region="${var.instance_region}"
}

#declaration about instance

resource "aws_instance" "nayan_terraform_q1"{
count="${var.instance_count}"
instance_type="t2.micro"
ami="ami-0e005fd51ba71dbe8"
security_groups=["${aws_security_group.allow_22_80.name}"]

tags={
Name="${var.instance_name}-${count.index+1}"
}
}
#declaration about security groups allowing tcp and ssh traffic to come in

resource "aws_security_group" "allow_22_80"{
name="nayan_terraform_sg"
description="to allow tcp & ssh"

ingress{
from_port=80
to_port=80
protocol="tcp"
}

ingress{
from_port=22
to_port=22
protocol="ssh"
}
tags={
name="nayan_terraform_sg"
}
}

