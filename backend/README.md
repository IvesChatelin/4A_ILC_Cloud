# API FLASK

- Tweet 
   - url : `http://127.0.0.1:5000/api/v1/tweet`
   - Methode : `POST`
   - Data : 
      - `author` : username
      - `tweet` : message
      - `subject` : subject of tweet

- AllTweet
   - url : `http://127.0.0.1:5000/api/v1/alltweet`
   - Methode : `GET`
   - Params : `author`

- allsubject
   - url : `http://127.0.0.1:5000/api/v1/allsubject`
   - Methode : `GET`

- login
   - url : `http://127.0.0.1:5000/api/v1/login`
   - Methode : `POST`
   - Data : 
      - `email` : email
      - `username` : username

- register
   - url : `http://127.0.0.1:5000/api/v1/register`
   - Methode : `POST`
   - Data : 
      - `email` : email
      - `username` : username
      - `password` : password

- tweetofsubject
   - url : `http://127.0.0.1:5000/api/v1/tweetofsubject`
   - Methode : `GET`
   - Params : 
      - `author`
      - `subject`

- like
   - url : `http://127.0.0.1:5000/api/v1/like`
   - Methode : `GET`
   - Params : 
      - `author`
      - `timestamp`

- dislike
   - url : `http://127.0.0.1:5000/api/v1/dislike`
   - Methode : `GET`
   - Params : 
      - `author`
      - `timestamp`

- retweet
   - url : `http://127.0.0.1:5000/api/v1/retweet`
   - Methode : `GET`
   - Params : 
      - `author`
      - `timestamp`

- retweet
   - url : `http://127.0.0.1:5000/api/v1/disretweet`
   - Methode : `GET`
   - Params : 
      - `author`
      - `timestamp`

- search
   - url : `http://127.0.0.1:5000/api/v1/search`
   - Methode : `GET`
   - Params : 
      - `author`
      - `value`

