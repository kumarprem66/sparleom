import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HeroSectionComponent } from './hero-section/hero-section.component';
import { HeroSection2Component } from './hero-section2/hero-section2.component';
import { MyswiperComponent } from './myswiper/myswiper.component';
import { IonicModule } from '@ionic/angular';
import { HeroSection3Component } from './hero-section3/hero-section3.component';
import { BestSellingComponent } from './best-selling/best-selling.component';
import { StudentSaysComponent } from './student-says/student-says.component';
import { CategoriesComponent } from './categories/categories.component';
import { HeroInstructorComponent } from './hero-instructor/hero-instructor.component';
import { FooterComponent } from './footer/footer.component'

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HeroSectionComponent,
    HeroSection2Component,
    MyswiperComponent,
    HeroSection3Component,
    BestSellingComponent,
    StudentSaysComponent,
    CategoriesComponent,
    HeroInstructorComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    
    IonicModule.forRoot(),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
