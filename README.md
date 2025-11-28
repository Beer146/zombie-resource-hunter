# 🧟 Zombie Resource Hunter

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![AWS](https://img.shields.io/badge/AWS-boto3-orange.svg)](https://aws.amazon.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Automatically detect and eliminate unused AWS resources that are costing you money. Find stopped EC2 instances, unattached EBS volumes, idle RDS databases, and unused load balancers across all your AWS regions.

## 🎯 Features

- 🔍 **EC2 Scanner**: Finds stopped instances and underutilized running instances
- 💾 **EBS Scanner**: Detects unattached volumes wasting storage costs
- 🗄️ **RDS Scanner**: Identifies idle database instances with no connections
- ⚖️ **ELB Scanner**: Locates unused Application, Network, and Classic load balancers
- 💰 **Cost Calculator**: Estimates monthly and annual savings from cleanup
- 📊 **Multi-Format Reports**: Console, JSON, CSV, and HTML output
- 🌍 **Multi-Region Support**: Scan across multiple AWS regions simultaneously
- ⚙️ **Configurable Thresholds**: Customize what qualifies as a "zombie" resource

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- AWS credentials configured (via `~/.aws/credentials` or environment variables)
- IAM permissions for read access to EC2, RDS, ELB, and CloudWatch

### Installation
```bash
# Clone the repository
git clone https://github.com/Beer146/zombie-resource-hunter.git
cd zombie-resource-hunter

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage
```bash
# Scan all resources in all configured regions
python src/main.py

# Scan specific resource types only
python src/main.py --resources ec2,ebs

# Output as JSON
python src/main.py --format json

# Output as CSV
python src/main.py --format csv
```

## 📸 Example Output
```
🧟 ZOMBIE RESOURCE HUNTER - SCAN RESULTS
================================================================================

📊 SUMMARY
   Total Zombie Resources: 1
   Potential Monthly Savings: $3.00
   Potential Annual Savings: $36.00

📦 BY RESOURCE TYPE
   EC2: 1 resources ($3.00/month)

🌍 BY REGION
   us-east-1: 1 resources

🔍 DETAILED FINDINGS

EC2 Resources (1):
+---------------------+------------+-----------+----------+---------------------------------------+
| Resource ID         | Name       | Region    | Status   | Reason                                |
+=====================+============+===========+==========+=======================================+
| i-0da5d7e56e21f3300 | Homelab-VM | us-east-1 | stopped  | Instance stopped for more than 7 days |
+---------------------+------------+-----------+----------+---------------------------------------+
```

## ⚙️ Configuration

Edit `config.yaml` to customize:

### AWS Regions
```yaml
aws:
  regions:
    - us-east-1
    - us-west-2
    - eu-west-1
```

### Detection Thresholds
```yaml
thresholds:
  ec2:
    stopped_days: 7        # Days stopped to be considered zombie
    cpu_threshold: 5       # CPU % below which it's underutilized
  
  ebs:
    unattached_days: 7     # Days unattached to be zombie
  
  rds:
    idle_days: 7
    connection_threshold: 1
  
  elb:
    no_traffic_days: 7
    request_threshold: 10
```

### Output Settings
```yaml
reporting:
  format: console          # console, json, csv, html
  save_to_file: true
  output_dir: ./reports
```

## 🔐 Required IAM Permissions

Attach this policy to your IAM user/role:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes",
        "elasticloadbalancing:DescribeLoadBalancers",
        "rds:DescribeDBInstances",
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": "*"
    }
  ]
}
```

## 📁 Project Structure
```
zombie-resource-hunter/
├── src/
│   ├── main.py                 # Entry point
│   ├── scanners/               # Resource scanners
│   │   ├── ec2_scanner.py      # EC2 instance scanner
│   │   ├── ebs_scanner.py      # EBS volume scanner
│   │   ├── rds_scanner.py      # RDS database scanner
│   │   └── elb_scanner.py      # Load balancer scanner
│   ├── cost_calculator.py      # Cost estimation logic
│   └── reporter.py             # Report generation
├── config.yaml                 # Configuration file
├── requirements.txt            # Python dependencies
└── README.md
```

## 🛣️ Roadmap

- [ ] **Resource Cleanup**: Automated deletion with approval workflow
- [ ] **Additional Services**: Lambda, S3, Elastic IPs, NAT Gateways
- [ ] **Notifications**: Email and Slack integration
- [ ] **Scheduling**: GitHub Actions for automated weekly scans
- [ ] **Web Dashboard**: Interactive UI for viewing results
- [ ] **Multi-Account**: AWS Organizations support
- [ ] **Cost History**: Track savings over time
- [ ] **Right-Sizing**: Recommend cheaper instance types

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - see LICENSE file for details

## 🔗 Part of DevOps Portfolio

This is part of my DevOps automation portfolio. Check out my other projects:
- 🧟 **Zombie Resource Hunter** (this project)
- 📊 Right-Sizing Recommendation Engine (coming soon)
- ✅ Compliance-as-Code Validator (coming soon)
- 📝 Postmortem Generator (coming soon)

---

**Built with ❤️ for cloud cost optimization**
