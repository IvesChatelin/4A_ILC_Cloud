import { Component, OnInit } from '@angular/core';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [NgIf],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {

  islike: boolean = false
  islikeSearch: boolean = false
  isSelectSubject: boolean = false
  isSelectTweetFind: boolean = false

  ngOnInit(): void {
  }

  onClickHome(){}

  onclickLogout(){}

}
