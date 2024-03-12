import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable, Subject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  URL_API = "http://localhost:5000/api/v1/"
  user : any = {}

  constructor(private httpClient: HttpClient) { }

  // private newUser = new Subject<any>();

  // sendNewUser(user: any){
  //   this.newUser.next(user)
  // }

  // receiveNewUser(): Observable<any>{
  //   return this.newUser.asObservable()
  // }

  login(data: any): Observable<any>{
    return this.httpClient.post(this.URL_API+"login",data)
  }

  register(data: any): Observable<any>{
    return this.httpClient.post(this.URL_API+"register",data)
  }
}
