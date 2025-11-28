# 🧟 Zombie Resource Hunter

Automatically detect and eliminate unused AWS resources that are costing you money.

## Features

- 🔍 **EC2 Scanner**: Finds stopped instances and underutilized running instances
- 💾 **EBS Scanner**: Detects unattached volumes wasting storage costs
- 🗄️ **RDS Scanner**: Identifies idle database instances
- ⚖️ **ELB Scanner**: Locates unused load balancers
- 💰 **Cost Calculator**: Estimates monthly savings from cleanup
- 📊 **Detailed Reports**: Export findings in multiple formats

## Prerequisites

- Python 3.8+
- AWS credentials configured (`~/.aws/credentials` or environment variables)
- IAM permissions for read access to EC2, RDS, ELB, CloudWatch

## Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/zombie-resource-hunter.git
cd zombie-resource-hunter

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Edit `config.yaml` to customize:
- AWS regions to scan
- Thresholds for what counts as "zombie"
- Cleanup settings (dry-run vs actual deletion)

## Usage

### Scan for zombie resources (dry-run):
```bash
python src/main.py
```

### Scan specific resource types:
```bash
python src/main.py --resources ec2,ebs
```

### Generate detailed report:
```bash
python src/main.py --format json --output reports/scan-results.json
```

### Enable cleanup (DANGEROUS - use with caution):
```bash
# Edit config.yaml first, set cleanup.enabled = true
python src/main.py --cleanup
```

## IAM Permissions Required

Minimum IAM policy needed:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes",
        "ec2:DescribeLoadBalancers",
        "rds:DescribeDBInstances",
        "cloudwatch:GetMetricStatistics",
        "pricing:GetProducts"
      ],
      "Resource": "*"
    }
  ]
}
```

## Project Structure
```
zombie-resource-hunter/
├── src/
│   ├── main.py              # Entry point
│   ├── scanners/            # Resource scanners
│   │   ├── ec2_scanner.py
│   │   ├── ebs_scanner.py
│   │   ├── rds_scanner.py
│   │   └── elb_scanner.py
│   ├── cost_calculator.py   # Cost estimation
│   └── reporter.py          # Report generation
├── config.yaml              # Configuration
└── requirements.txt
```

## Roadmap

- [ ] Support for additional AWS services (Lambda, S3, etc.)
- [ ] Email/Slack notifications
- [ ] Scheduled scans via GitHub Actions
- [ ] Web dashboard
- [ ] Multi-account support

## License

MIT