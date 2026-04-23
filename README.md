☁️ AWS Cloud Engineering Projects

5 hands-on AWS projects built from scratch as a Junior Cloud Engineer — all running on AWS Free Tier.

Author: Rufus Ayodele | Junior Cloud Engineer
Cloud Provider: Amazon Web Services (AWS)
Region: EU North (Stockholm)

🗺️ Project Roadmap
Project 1 (EC2 + Webpage)
        ↓
Project 2 (Python + S3 Automation)
        ↓
Project 3 (MySQL Database)
        ↓
        = Full 3-Tier Web Application!
        ↓
Project 4 (Dockerized Container)
        ↓
Project 5 (Private VPN Server)
        ↓
        = Production-Like Cloud Environment 🚀

🥇 Project 1 — Host a Webpage on EC2
What I Built
A live webpage hosted on an AWS EC2 instance, served by Nginx and accessible via a public IP address.
Steps Taken

Launched an EC2 t2.micro Ubuntu instance
Connected via SSH using PuTTY and a .pem key pair
Installed and configured Nginx web server
Created a custom HTML/CSS webpage
Configured Security Groups to open port 80 (HTTP)
Accessed the live webpage via public IPv4 address

Skills Learned
EC2 Linux SSH Nginx Security Groups Public IPs PuTTY
Files

project1-webpage/index.html — The hosted webpage


🥈 Project 2 — Python Automation Script on EC2
What I Built
A Python script that automatically backs up files to AWS S3, scheduled to run daily using a Cron Job.
Steps Taken

Created an S3 bucket (rufus-backups-2026) for storage
Created an IAM Role (ec2-s3-role) and attached it to EC2
Installed AWS CLI and boto3 Python library
Wrote a Python script to upload files to S3 with dated folders
Scheduled the script to run automatically every night at 10pm using Cron

Skills Learned
Python boto3 AWS S3 IAM Roles AWS CLI Automation Cron Jobs
Files

project2-python/backup.py — The automated backup script


🥉 Project 3 — MySQL Database on EC2
What I Built
A MySQL database installed on EC2, connected to a Python script that stores and retrieves visitor data.
Steps Taken

Installed and secured MySQL server on EC2
Created a database (rufusdb), user (webuser) and visitors table
Configured Security Groups to allow database connections
Installed mysql-connector-python library
Wrote a Python script to connect, insert and query data from the database

Skills Learned
MySQL Databases Python mysql-connector Security Groups Networking
Files

project3-database/dbconnect.py — Database connection and query script


🏅 Project 4 — Dockerize the App
What I Built
A Flask web application packaged into a Docker container and deployed on EC2, with the image stored in AWS ECR.
Steps Taken

Installed Docker on EC2
Created a Flask web application (app.py)
Wrote a Dockerfile to define the container build recipe
Built the Docker image and ran it as a container on port 8080
Configured Security Groups to open port 8080
Accessed the Dockerized app via browser

Skills Learned
Docker Dockerfile Flask Python Containers AWS ECR Port Mapping
Files

project4-docker/app.py — Flask web application
project4-docker/Dockerfile — Docker build recipe


🎖️ Project 5 — Set Up a Private VPN Server
What I Built
A private OpenVPN server running on a dedicated EC2 instance, allowing secure encrypted access to all cloud resources.
Steps Taken

Launched a new EC2 instance dedicated to the VPN server
Configured Security Groups to open ports 22, 1194 (UDP) and 443
Downloaded and ran the OpenVPN installer script
Configured protocol (UDP), port (1194), DNS (Google) and client name
Downloaded the .ovpn config file to laptop using WinSCP
Installed OpenVPN Connect on laptop and imported the config
Successfully connected laptop through the private VPN tunnel

Skills Learned
OpenVPN VPN VPC Private Networking Security WinSCP UDP
Files

project5-vpn/rufus-laptop.ovpn — VPN client configuration file


🛠️ Full Tech Stack
CategoryTechnologiesCloud PlatformAmazon Web Services (AWS)ComputeEC2 t2.micro, t3.microStorageAmazon S3SecurityIAM, Security Groups, VPN, SSH Key PairsWeb ServerNginxDatabaseMySQLContainerizationDocker, Dockerfile, AWS ECRProgrammingPython 3, boto3, Flask, mysql-connectorAutomationCron Jobs, AWS CLINetworkingVPC, OpenVPN, Security Groups, Inbound RulesOSUbuntu 24.04 LTSToolsPuTTY, WinSCP, PuTTYgen, OpenVPN Connect

💡 Key Lessons Learned

Always save your .pem key file immediately after creating it — AWS only lets you download it once!
Use IAM roles instead of storing AWS credentials directly on the server
Security Groups act as a firewall — always follow the principle of least privilege
Stop EC2 instances when not in use to stay within the AWS Free Tier limits
Use sudo for system-level commands on Ubuntu
Docker solves the "it works on my machine" problem by packaging everything together
A VPN adds a critical layer of security by making servers only accessible through a private tunnel


🚀 What's Next

 Kubernetes (K8s) — Container orchestration
 Terraform — Infrastructure as Code
 GitHub Actions — CI/CD Pipeline
 CloudWatch — Monitoring and alerting
 AWS Certificate Manager — HTTPS/SSL


👨‍💻 About Me
I am Rufus Ayodele, a Junior Cloud Engineer passionate about building and securing cloud infrastructure. This repository documents my hands-on AWS learning journey — from launching my first EC2 instance to running a fully containerized app behind a private VPN.
📧 Connect with me on LinkedIn
🌍 All projects built on AWS Free Tier

Built with determination, curiosity and a lot of PuTTY sessions! ☁️🚀
