import { Component, OnInit } from '@angular/core';
import { CourseService } from '../services/course.service';
import { LecturesService } from '../services/lectures.service';
import { Router } from '@angular/router';
// import { DatePipe } from '@angular/common';
// import { DatePipe } from '@angular/common';
// import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-admin-dashboard',
  templateUrl: './admin-dashboard.component.html',
  styleUrls: ['./admin-dashboard.component.css']
})
export class AdminDashboardComponent implements OnInit{


  option_courses:any[] = []

  letures_data:any[] = []

  selectedValue:number = 2

  constructor(private cour_ser:CourseService,private lec_ser:LecturesService,private router:Router
    ){


  }

  onSelectChange(event:any){
    this.selectedValue = event.target.value
    
    this.getLectureOfCourse(Number(this.selectedValue))
  }


  ngOnInit(): void {
    
    this.getCourses()
    // this.getAllLectureOfCourse()
    this.getLectureOfCourse(this.selectedValue)
  }

  getCourses(){
    this.cour_ser.getcourses().subscribe((response:any)=>{
      const courses = response.results
      // console.log(courses)
      courses.forEach((element :any) => {
        this.option_courses.push({value:element.id,text:element.course_name})
      });
    
    })
  }


  getLectureOfCourse(c_id:number){
    this.lec_ser.getLectureOfCourse(c_id).subscribe((response:any)=>{
      this.letures_data = response


      this.letures_data.forEach((ele:any)=>{



        const datetime = new Date(ele.timing)
        // const formattedDate = this.datePipe.transform(datetime,'yyyy-MM-dd')
        // const formattedTime = this.datePipe.transform(datetime,'HH:mm:ss')


        // console.log(formattedDate)
        // console.log(formattedTime)
      })
      // console.log(this.letures_data)
    })
  }


  updateLecture(id:number){

    const dataToPass = {
     
      "lect_id":id

    }
    this.router.navigate(['admin-create-lecture'],{queryParams:dataToPass})
  }

  deleteLecture(id:number){

    this.lec_ser.deleteLecture(id).subscribe((response)=>{
      alert("Deleted")
    })
  }

  convertDate(timing_value:any):string{

    const lectureTiming = new Date(timing_value); 
      let formattedTiming = lectureTiming.toISOString(); // "yyyy-MM-ddThh:mm:ss.SSSZ"

      // Remove seconds and milliseconds
      formattedTiming = formattedTiming.slice(0, 10); // "yyyy-MM-dd"

      return formattedTiming;
  }

  convertDateInTime(timing_value:any):string{
    const lectureTiming = new Date(timing_value); 
    let formattedTiming = lectureTiming.toISOString(); // "yyyy-MM-ddThh:mm:ss.SSSZ"

    formattedTiming = formattedTiming.slice(11, 16); // "hh:mm"

    return formattedTiming;
  }

}
