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
  displayTweetOfSubject: boolean = false
  displayAllTweet: boolean = true
  subjectClicked: string = ''
  tweetOfSubject: any
  mytweet: boolean = false
  allMyTweet: any

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

  getMyTweet(){
    this.displayAllTweet = false
    this.displayTweetOfSubject = false
    this.mytweet = true
    this.tweetService.mytweet(this.username!).subscribe(res => {
      console.log(res)
      this.allMyTweet = res[0]
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

  onClickHome(){
    this.displayAllTweet = true
    this.displayTweetOfSubject = false
    this.mytweet = false
  }

  onClickSubject(subject: string){
    this.subjectClicked = subject
    this.displayAllTweet = false
    this.mytweet = false
    this.displayTweetOfSubject = true
    this.tweetService.tweetOfSubject(this.username!,subject).subscribe(res => {
      this.tweetOfSubject = res[0]
    })
  }

  onclickLogout(){
    this.tweets = null
    this.subjects = null
    localStorage.setItem("isLoggedIn", 'false');
    localStorage.setItem("username", 'null');
    this.router.navigate(['login'])
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

  onClickLike(tweet: any){
    if(tweet['liked']){
      this.tweetService.dislike(this.username!, tweet['timestamp']).subscribe(res => {
        if(res[1] == 200){
          this.getAllTweet()
          if(this.displayTweetOfSubject){
            this.onClickSubject(this.subjectClicked)
          }
          if(this.mytweet){
            this.getMyTweet()
          }
        }
      })
    }else{
      this.tweetService.like(this.username!, tweet['timestamp']).subscribe(res => {
        if(res[1] == 200){
          this.getAllTweet()
          if(this.displayTweetOfSubject){
            this.onClickSubject(this.subjectClicked)
          }
          if(this.mytweet){
            this.getMyTweet()
          }
        }
      })
    }
  }

  onClickRetweet(tweet: any){
    if(tweet['retweeted']){
      this.tweetService.disretweet(this.username!, tweet['timestamp']).subscribe(res => {
        if(res[1] == 200){
          this.getAllTweet()
          if(this.displayTweetOfSubject){
            this.onClickSubject(this.subjectClicked)
          }
          if(this.mytweet){
            this.getMyTweet()
          }
        }
      })
    }else{
      this.tweetService.retweet(this.username!, tweet['timestamp']).subscribe(res => {
        if(res[1] == 200){
          this.getAllTweet()
          if(this.displayTweetOfSubject){
            this.onClickSubject(this.subjectClicked)
          }
          if(this.mytweet){
            this.getMyTweet()
          }
        }
      })
    }
  }

}
