#!/bin/bash
# go over each past commit and copy version of stats.json at that commit in directory history

mkdir -p history

# Iterate over each commit with its date
git rev-list --all --format="%at %H" | while read -r date commit; do
    # Skip the "commit" lines from the git output
    [[ $date == commit ]] && continue
    
    # Convert Unix timestamp to YYYY-MM-DD format
    formatted_date=$(date -d "@$date" +"%Y-%m-%d")
    
    # Check out the commit
    git checkout "$commit" -- stats.json 2>/dev/null
    
    if [ -f stats.json ]; then
        # Copy the stats.json to the history directory with date
        cp stats.json "history/stats_${formatted_date}.json"
    fi
done

# Checkout back to the main branch
git checkout -
