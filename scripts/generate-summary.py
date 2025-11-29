#!/usr/bin/env python3
"""Generate GitHub Actions summary from scan results"""

import json
import sys

try:
    with open('scan-results.json') as f:
        data = json.load(f)
    
    summary = data.get('summary', {})
    print(f"**Total Zombie Resources:** {summary.get('total_zombies', 0)}")
    print(f"**Potential Monthly Savings:** ${summary.get('cost_summary', {}).get('total_monthly_savings', 0):.2f}")
    print(f"**Potential Annual Savings:** ${summary.get('cost_summary', {}).get('total_annual_savings', 0):.2f}")
    print("")
    
    # By type
    stats = summary.get('stats', {})
    by_type = stats.get('by_type', {})
    if by_type:
        print("### By Resource Type")
        for resource_type, count in by_type.items():
            print(f"- **{resource_type}:** {count}")
            
except Exception as e:
    print(f"Error parsing results: {e}")
    sys.exit(0)