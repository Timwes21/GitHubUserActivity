import requests
import json
github = "https://api.github.com/users/Erik-Cupsa/events"
json_file = "events.json"

page = requests.get(github).json()


print(page)   



print("recent activity:")
def commits():
    pass
    
    
def sparse(data):
    if data['type'] == "CreateEvent":
        print(f"Create Event in {data['repo']['name']}")
    elif data['type'] == "PushEvent":
        print(f"Pushed Commit in {data['repo']['name']}")
    elif data['type'] == "WatchEvent":
        print(f"Starred {data['repo']['name']}")
    elif data['type'] == "PullRequestEvent":
        print(f"Pull Request in {data['repo']['name']}")
    elif data['type'] == "MemberEvent":
        print(f"Updated a Collaboration in {data['repo']['name']}")
    elif data['type'] == "PublicEvent":
        print(f"{data['repo']['name']} was made public")
    else:
        print(data["type"])
        
for i in page:
    sparse(i)
    
    







