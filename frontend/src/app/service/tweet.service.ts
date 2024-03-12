import { Injectable} from '@angular/core';
import { HttpClient, HttpParams} from '@angular/common/http';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
  
})
export class TweetService {

  URL_API = "http://localhost:5000/api/"

  constructor(private httpClient: HttpClient) { }

  tweet(data: any): Observable<any>{
    return this.httpClient.post(this.URL_API+"tweet",data)
  }

  allTweet(): Observable<any>{
    return this.httpClient.get(this.URL_API+"alltweet")
  }

  allSubject(): Observable<any>{
    return this.httpClient.get(this.URL_API+"allsubject")
  }

  tweetOfSubject(username: string, subject: string): Observable<any>{
    return this.httpClient.get(this.URL_API+"tweetofsubject", {params: new HttpParams().set('subject', subject).set('author', username)})
  }
}
