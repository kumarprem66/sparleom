import { Component, OnInit } from '@angular/core';
import { CourseService } from '../services/course.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-courses-all',
  templateUrl: './courses-all.component.html',
  styleUrls: ['./courses-all.component.css','./courseAll.scss']
})
export class CoursesAllComponent implements OnInit{

  main_heading = "The World's largest selection of courses"
  second_heading = "Choose from 130,000 online video courses with new additions published every month"

  all_courses:any[] = []
  constructor(private course_ser:CourseService,private router:Router){

  }

  ngOnInit(): void {
    
    this.getAllCourses()

  }


  getAllCourses(){
    this.course_ser.getcourses().subscribe((response:any)=>{
      console.log(response)

      this.all_courses = response.results
    })
  }

  show_course_details(id:number){

    const datatopass = {
      "course_id":id
    }

    this.router.navigate(['course-detail'],{queryParams:datatopass})
    
  }

  edit_course(id:number){

    console.log(id)
    this.course_ser.getCourseById(id).subscribe((resolve)=>{

      const datatopass  = {

        "course_id":id
      }
      this.router.navigate(['admin-add-course'],{queryParams:datatopass})
      
    })

  
  }

  delete_course(id:number){

    const aggreed_delete = confirm("are you sure to delete?")
    if(aggreed_delete){
      this.course_ser.deleteCourse(id).subscribe((response)=>{
        console.log(response)
        alert("deleted Successfully")
        this.getAllCourses()
      })
    }

  }
}
