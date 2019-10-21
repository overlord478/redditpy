import praw
import requests
client = 'your client id'
client_Secret = "your client secret"
url = []
url_title = []
url_parsed = []
s = [".jpg",".jpeg",".png",".gif"]
path = "path to store the pics!!"
reddit = praw.Reddit(client_id = client ,client_secret = client_Secret,username = "your username",password = "your password",user_agent = "praw_check")
print(reddit.user.me())	
for submission in reddit.subreddit('subreddit name eg:"memes"').hot(limit = 100):
	url.append(submission.url)
	url_title.append(submission.title)
for title in url_title:
	url_parsed.append(''.join(s for s in title if s.isalnum()))
for index in range(len(url)):
	ext = url[index][-4:] if url[index][-4:] in s else ".jpg"
	with open(path+url_parsed[index]+str(index)+ext,'wb') as handle:
		response = requests.get(url[index],stream=True)
		if not response.ok:
			print(response)
		for block in response.iter_content(1024):
			if not block:
				break
			handle.write(block)
	
print("Success !")
