import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-hero-section2',
  templateUrl: './hero-section2.component.html',
  styleUrls: ['./hero-section2.component.css','./slide.scss']
})
export class HeroSection2Component implements OnInit{

  main_heading = "The World's largest selection of courses"
  second_heading = "Choose from 130,000 online video courses with new additions published every month"




  constructor(){

  }
  ngOnInit(): void {
    

  }



}
