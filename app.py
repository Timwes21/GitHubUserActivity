import requests

account = input("Who's activity would you like to follow: ")
github = f"https://api.github.com/users/{account}/events"

page = requests.get(github).json()
    
def sparse(type, name, num):
    if type == "CreateEvent":
        print(f"- {num} Create Event(s) in {name}")
    elif type == "PushEvent":
        print(f"- Pushed {num} Commit(s) in {name}")
    elif type == "WatchEvent":
        print(f"- Starred {name}")
    elif type == "PullRequestEvent":
        print(f"- {num} Pull Request(s) in {name}")
    elif type == "MemberEvent":
        print(f"- Updated a Collaboration in {name}")
    elif type == "PublicEvent":
        print(f"- {name} was made public")
    else:
        print(type)


n = 0
list_of_data = []
    
    
    
def sparser(data, n):
    if n > 0:
        if data['type'] == list_of_data[0]['type'] and data['repo']['name'] == list_of_data[0]['repo']['name']:
            list_of_data.append(data)
            n += 1
        else:
            sparse(list_of_data[0]['type'], list_of_data[0]['repo']['name'], len(list_of_data))
            list_of_data.clear()
            list_of_data.append(data)
            n = 0
    else:
        list_of_data.append(data)
        n += 1
        
    return n
        
    
        
    
for i in page:
    n = sparser(i, n)
    








