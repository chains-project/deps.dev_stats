"""
Create a line charts for number of dependencies over time

ls history/ | tail
stats_2025-01-21.json
stats_2025-01-22.json
stats_2025-01-23.json
stats_2025-01-24.json
stats_2025-01-25.json
stats_2025-01-26.json
stats_2025-01-27.json
stats_2025-01-28.json
stats_2025-01-29.json

cat history/stats_2025-01-21.json
[
   {
      "packageCount" : 168806,
      "system" : "CARGO"
   },
   {
      "packageCount" : 1295764,
      "system" : "GO"
   },
   {
      "packageCount" : 670019,
      "system" : "MAVEN"
   },
   {
      "packageCount" : 3377620,
      "system" : "NPM"
   },
   {
      "packageCount" : 430711,
      "system" : "NUGET"
   },
   {
      "packageCount" : 575669,
      "system" : "PYPI"
   }
]


"""

import json
import glob
import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def load_stats(filename):
    """Load stats from a JSON file"""
    with open(filename) as f:
        return json.load(f)

def extract_date(filename):
    """Extract date from filename like stats_2025-01-21.json"""
    return datetime.strptime(filename.split('stats_')[1].split('.json')[0], '%Y-%m-%d')

def create_time_series():
    # Get all stats files
    files = sorted(glob.glob('history/stats_*.json'))
    
    # Initialize data structure
    data = {
        'dates': [],
        'CARGO': [], 'GO': [], 'MAVEN': [], 
        'NPM': [], 'NUGET': [], 'PYPI': []
    }
    
    # Collect data
    for f in files:
        try:
            date = extract_date(f)
            stats = load_stats(f)
            
            data['dates'].append(date)
            for entry in stats:
                data[entry['system']].append(entry['packageCount'])
        except Exception as e:
            pass
    
    # Create absolute numbers plot
    plt.figure(figsize=(12, 6))
    for system in ['CARGO', 'GO', 'MAVEN', 'NPM', 'NUGET', 'PYPI']:
        plt.plot(data['dates'], data[system], label=system, marker='o', markersize=3)
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()
    plt.title('Package Count Over Time by System')
    plt.xlabel('Date')
    plt.ylabel('Number of Packages')
    plt.legend()
    plt.grid(True)
    plt.savefig('package_trends_absolute.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Create relative growth plot
    plt.figure(figsize=(12, 6))
    for system in ['CARGO', 'GO', 'MAVEN', 'NPM', 'NUGET', 'PYPI']:
        initial_value = data[system][0]
        relative_growth = [(x / initial_value - 1) * 100 for x in data[system]]
        plt.plot(data['dates'], relative_growth, label=system, marker='o', markersize=3)
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()
    plt.title('Relative Package Growth Since First Measurement')
    plt.xlabel('Date')
    plt.ylabel('Growth (%)')
    plt.legend()
    plt.grid(True)
    plt.savefig('package_trends_relative.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_time_series()