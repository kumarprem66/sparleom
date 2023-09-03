import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-admin-auth',
  templateUrl: './admin-auth.component.html',
  styleUrls: ['./admin-auth.component.css']
})
export class AdminAuthComponent implements OnInit{

  adminForm:FormGroup

  admin_ids:string[] = ["admin-prem-kumar","admin-kumar-prem"]

  constructor(private fb:FormBuilder,private router:Router){
    this.adminForm = this.fb.group({
      admin_id : ['',Validators.required]
    })
  }
  ngOnInit(): void {
    
  }

  adminSubmit(){

    const admin_id_value = this.adminForm.value
    console.log(admin_id_value)

    this.admin_ids.forEach(admin=>{
      if(admin.includes(admin_id_value.admin_id)){
        alert("success")
        const id = admin_id_value.admin_id
        localStorage.setItem("sparleom_user",id)
        this.router.navigate(['admin-dashboard'])

      }
    })
  }



}
