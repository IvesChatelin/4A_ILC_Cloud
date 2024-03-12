import redis

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# users jerome
userByName = r.hset(
	"jerome",
	mapping={
		"email": "jerome@gmail.com",
		"password": "jerome"
	}
)
userByEmail = r.hset(
	"jerome@gmail.com",
	mapping={
		"username": "jerome",
		"password": "jerome"
	}
)

#user esirem
userByName = r.hset(
	"esirem",
	mapping={
		"email": "esirem@gmail.com",
		"password": "esirem"
	}
)
userByEmail = r.hset(
	"esirem@gmail.com",
	mapping={
		"username": "esirem",
		"password": "esirem"
	}
)

# tweet 
tweet1 = r.hset(
	"10/03/2024 14:54",
	mapping={
	    "author": "esirem",
		"subject": "#cours de cloud compiting",
		"message": "examen le 26 mars 2024"
	}
)
tweet2 = r.hset(
	"08/03/2024 14:54",
	mapping={
	    "author": "jerome",
		"subject": "#cours de cloud compiting",
		"message": "rendu le 13 Mars"
	}
)
tweet3 = r.hset(
	"07/03/2024 14:54",
	mapping={
	    "author": "jerome",
		"subject": "#compte rendu",
		"message": "compte rendu du projet via github"
	}
)

# list of tweet
tweet_list = r.lpush("tweets", *["10/03/2024 14:54","08/03/2024 14:54","07/03/2024 14:54"])
			
# list of tweet for one author
userWhoHasTweet1 = r.lpush("tweets:esirem", "10/03/2024 14:54")
userWhoHasTweet2 = r.lpush("tweets:jerome", "08/03/2024 14:54")
userWhoHasTweet2 = r.lpush("tweets:jerome", "07/03/2024 14:54")
			
# list of tweet for one subject
subjectTweeted1 = r.lpush("tweets:#cours de cloud compiting", "10/03/2024 14:54")
subjectTweeted2 = r.lpush("tweets:#cours de cloud compiting", "08/03/2024 14:54")
subjectTweeted2 = r.lpush("tweets:#compte rendu", "07/03/2024 14:54")

print("succès")
