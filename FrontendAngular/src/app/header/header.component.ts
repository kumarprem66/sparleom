import { Component,HostListener, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css','./headers.scss']
})
export class HeaderComponent implements OnInit{

  navbarIsSticky = false
  menuType: string = 'default'
  current_user = "Login"


  activeItem:string = "Home"

  constructor(private router:Router){

    

  }


  setActiveItem(itemName: string) {
    this.activeItem = itemName;
  }

  @HostListener('window.scroll',[])
  onWindowScroll(){

    // console.log("scrolll")
    this.navbarIsSticky = window.pageYOffset >= 70
  }

  ngOnInit(): void {
    // if(this.menuType == 'admin'){

    //   this.router.navigate(['/admin-dashboard'])
    // }

    const local_user = localStorage.getItem("sparleom_user")
    if(local_user != null){

      this.current_user = local_user;
      if(this.current_user.startsWith("admin")){

        this.current_user = this.current_user.substring(5)

        this.menuType = 'admin'

        this.router.navigate(['/admin-dashboard'])


      }else if(this.current_user.startsWith("instructor")){

        this.current_user = this.current_user.substring(10)

        this.menuType = 'instructor'

        this.router.navigate(['/instructor-dashboard'])

      }else if(this.current_user.startsWith("student")){
        this.current_user = this.current_user.substring(7)
        this.menuType = 'student'

        this.router.navigate(['/student-dashboard'])
      }
      console.log(this.current_user)
    }
  }

}
