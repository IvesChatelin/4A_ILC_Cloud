# API FLASK

lancer la base de données de test : `python db_test.py`

- Tweet 
   - Description: l'api qui permet de faire un tweet
   - url : `http://127.0.0.1:5000/api/v1/tweet`
   - Methode : `POST`
   - Data : 
      - `author` : username
      - `tweet` : message
      - `subject` : subject of tweet

- AllTweet
   - Description: l'api qui permet d'afficher tous les tweets
   - url : `http://127.0.0.1:5000/api/v1/alltweet`
   - Methode : `GET`
   - Params : `author`

- allsubject
   - Description: l'api qui permet d'afficher tous les sujets
   - url : `http://127.0.0.1:5000/api/v1/allsubject`
   - Methode : `GET`

- login
   - Description: l'api qui permet de se connecter
   - url : `http://127.0.0.1:5000/api/v1/login`
   - Methode : `POST`
   - Data : 
      - `email` : email
      - `username` : username

- register
   - Description: l'api qui permet de s'inscrire
   - url : `http://127.0.0.1:5000/api/v1/register`
   - Methode : `POST`
   - Data : 
      - `email` : email
      - `username` : username
      - `password` : password

- tweetofsubject
   - Description: l'api qui permet d'afficher tous les tweets d'un sujet
   - url : `http://127.0.0.1:5000/api/v1/tweetofsubject`
   - Methode : `GET`
   - Params : 
      - `author`
      - `subject`

- like
   - Description: l'api qui permet d'enregistrer les likes
   - url : `http://127.0.0.1:5000/api/v1/like`
   - Methode : `GET`
   - Params : 
      - `author`
      - `timestamp`

- dislike
   - Description: l'api qui permet de supprimer les likes
   - url : `http://127.0.0.1:5000/api/v1/dislike`
   - Methode : `GET`
   - Params : 
      - `author`
      - `timestamp`

- retweet
   - Description: l'api qui permet de reposter un tweet
   - url : `http://127.0.0.1:5000/api/v1/retweet`
   - Methode : `GET`
   - Params : 
      - `author`
      - `timestamp`

- retweet
   - Description: l'api qui permet de supprimer le reposte d'un tweet
   - url : `http://127.0.0.1:5000/api/v1/disretweet`
   - Methode : `GET`
   - Params : 
      - `author`
      - `timestamp`

- search
   - Description: l'api qui permet de la recherche d'un tweet ou sujet
   - url : `http://127.0.0.1:5000/api/v1/search`
   - Methode : `GET`
   - Params : 
      - `author`
      - `value`

- mytweet
   - Description: l'api qui permet d'afficher tous les tweets d'un utilisateur
   - url : `http://127.0.0.1:5000/api/v1/mytweet`
   - Methode : `GET`
   - Params : 
      - `author`
      - `value`

