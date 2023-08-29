import { Component,HostListener } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css','./headers.scss']
})
export class HeaderComponent {

  navbarIsSticky = false

  @HostListener('window.scroll',[])
  onWindowScroll(){

    // console.log("scrolll")
    this.navbarIsSticky = window.pageYOffset >= 70
  }

}
