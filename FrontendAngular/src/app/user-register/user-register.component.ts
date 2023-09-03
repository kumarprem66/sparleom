import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { RegisterService } from '../services/register.service';
import { arLocale } from 'ngx-bootstrap/chronos';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-register',
  templateUrl: './user-register.component.html',
  styleUrls: ['./user-register.component.css']
})
export class UserRegisterComponent implements OnInit{

  userData:FormGroup
  constructor(private fb:FormBuilder,private regSer:RegisterService,private router:Router){
    this.userData = this.fb.group({
      user_name : ['',Validators.required],
      user_email : ['',Validators.required],
      user_password: ['',Validators.required]
    })
  }
  ngOnInit(): void {
    
    

  }

  userRegister(){
    console.log("premrfm")
   if(this.userData.valid){
    const uservalue = this.userData.value
    this.regSer.userRegister(uservalue).subscribe((response)=>{
      alert("Registered")
      // localStorage.setItem('sparleom-user',JSON.stringify(uservalue))
      this.router.navigate(['login'])
      console.log(uservalue)
    })
   }else{
    alert("every field need valid data")
   }
  }

  




}
