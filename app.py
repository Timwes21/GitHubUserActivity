import requests

account = input("GitHub-Activity ")
github = f"https://api.github.com/users/{account}/events"

page = requests.get(github)

while page.status_code != 200:
    print("status code not 200")  # since it is a command line, I wanted an appropriate response

page = page.json() # turns the page into json format
    
def sparse(type, name, num): # funcction to measure the size, type and name, the evaluate the response needed
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
list_of_data = [] # Initialize a list to store duplicates
    
    
    
def sparser(data, n):
    if n > 0: # intead of using the length of duplicates found, use n to stay in the if statement when the list is cleared
        # if there is a duplicate store it in the list
        if data['type'] == list_of_data[0]['type'] and data['repo']['name'] == list_of_data[0]['repo']['name']:
            list_of_data.append(data)
            n += 1
        else:
            # if the next one is not a duplicate print the list of duplicates
            sparse(list_of_data[0]['type'], list_of_data[0]['repo']['name'], len(list_of_data))
            list_of_data.clear() # after the duplicates are displayed clear the list
            list_of_data.append(data) # append data to list to check for more duplicates
            n = 0
    else:
        list_of_data.append(data)
        n += 1
        
    return n
        
    
        
# for loop to check the data in the page
for i in page:
    n = sparser(i, n)
    








