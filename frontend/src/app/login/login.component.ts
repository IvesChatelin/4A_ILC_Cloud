import { Component, OnInit } from '@angular/core';
import { NgIf } from '@angular/common';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { TweetService } from '../service/tweet.service';
import { Router } from '@angular/router';
import { AuthService } from '../service/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [NgIf, FormsModule, ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent implements OnInit {

  constructor(private tweetService: TweetService, private authService: AuthService, private router: Router) { }
  
  ngOnInit(): void {
    
  }

  signUp: boolean = false
  userNotFound: boolean = false

  loginForm = new FormGroup({
    "username": new FormControl(''),
    "email": new FormControl(''),
    "password": new FormControl('')
  })

  onClickSignIn(){
    this.authService.login(this.loginForm.value).subscribe(res => {
      if(res[1] != 200){
        localStorage.setItem("isLoggedIn", 'false');
        this.userNotFound = true
      }else{
        localStorage.setItem("username", res[0]['username'])
        localStorage.setItem("isLoggedIn", 'true');
        this.router.navigate(['home'])
      }
      console.log(res)
    })
  }

  onClickSignUp(){
    this.authService.register(this.loginForm.value).subscribe(res => {
      if(res[1] == 200){
        this.signUp = false
      }
      console.log(res)
    })
  }

}
