import { Component, OnInit, inject } from '@angular/core';
import { NgFor, NgIf } from '@angular/common';
import { AuthService } from '../service/auth.service';
import { Router } from '@angular/router';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { TweetService } from '../service/tweet.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [NgIf, NgFor, FormsModule, ReactiveFormsModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {

  constructor(private authService: AuthService, private tweetService: TweetService, private router: Router){}

  islike: boolean = false
  islikeSearch: boolean = false
  isSelectSubject: boolean = false
  isSelectTweetFind: boolean = false
  email: string = ''
  tweets: any
  subjects: any

  username = localStorage.getItem('username')

  tweetForm = new FormGroup({
    "author": new FormControl(),
    "subject": new FormControl(),
    "message": new FormControl()
  })

  ngOnInit(): void {
    this.getAllSubject()
    this.onInitForm();
    this.getAllTweet()
  }

  getAllTweet(){
    this.tweetService.allTweet().subscribe(res => {
      console.log(res)
      this.tweets = res[0]
    })
  }

  getAllSubject(){
    this.tweetService.allSubject().subscribe(res => {
      console.log(res)
      this.subjects = res[0]
    })
  }

  onInitForm(){
    this.tweetForm.setValue({author: this.authService.user['username'], subject:"", message:""})
  }

  onClickHome(){}

  onclickLogout(){
    this.router.navigate(['login'])
    this.authService.isLoggedIn = false
  }

  onClickTweet(){
    this.tweetForm.value.subject = "#"+this.tweetForm.value.subject
    this.tweetService.tweet(this.tweetForm.value).subscribe(res => {
      if(res[1] == 200){
        console.log(res)
        this.onInitForm()
        this.getAllTweet()
      }
    })
  }

}
