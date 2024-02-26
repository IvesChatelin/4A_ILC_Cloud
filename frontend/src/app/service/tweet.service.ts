import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class TweetService {

  URL_API = "http://localhost:5000/api/"

  constructor(private httpClient: HttpClient) { }

  createTweet(tweet: any): Observable<any>{
    return this.httpClient.post("",tweet)
  }
}