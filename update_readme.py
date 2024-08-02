import json

# Load LeetCode stats from the JSON file
with open('leetcode.json', 'r') as file:
    data = json.load(file)

# Extract relevant data
total_problems_solved = data['totalSolved']
acceptance_rate = data['acceptanceRate']
easy_solved = data['easySolved']
medium_solved = data['mediumSolved']
hard_solved = data['hardSolved']

# Update README.md
with open('README.md', 'r') as file:
    lines = file.readlines()

with open('README.md', 'w') as file:
    for line in lines:
        if line.startswith('![LeetCode Stats]'):
            file.write(f'![LeetCode Stats](https://leetcode-badge-api.herokuapp.com/Jahnavi BS.png)\n')
        else:
            file.write(line)
