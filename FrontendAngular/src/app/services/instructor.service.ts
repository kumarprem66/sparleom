import { JsonPipe } from '@angular/common';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InstructorService {

  baseUrl = "http://127.0.0.1:8000/sparleom/instructors/"
  constructor(private http:HttpClient) { }


  getAllInstructor(){
    return this.http.get<any[]>(this.baseUrl)
  }

  createInstructor(data:any):Observable<any>{

    const headers = new HttpHeaders({
      "Content-Type":"application/json"
    })
    return this.http.post(this.baseUrl+"create",JSON.stringify(data),{headers})
  }

  

}
