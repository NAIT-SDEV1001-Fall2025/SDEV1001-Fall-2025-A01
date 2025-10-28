fav_fruit_voters = {
    "daniel": "apple",
    "jessica": "apple",
    "michael": "banana",
    "john": "banana",
    "jessie": "apple",
    "jim": "orange",
    "jenny": "apple",
    "jason": "orange",
    "joseph": "banana",
    "james": "orange",
    "mary": "apple",
    "melody": "banana",
}

voting_results = {
    "banana": 0,
    "apple": 0,
    "orange": 0
}

# list the voters
print("Voters:")
for voter in fav_fruit_voters.keys():
    print(F"- {voter}")

# tally up code here.
for vote in fav_fruit_voters.values():
    voting_results[vote] += 1

# print the results
print("Voting Results:")
for fruit, votes in sorted(voting_results.items()):
    print(F"- The fruit: {fruit} has {votes} votes")
