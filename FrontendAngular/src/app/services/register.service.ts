import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RegisterService {

   baseUrl = "http://127.0.0.1:8000/sparleom/"
  constructor(private http:HttpClient) { }

  userRegister(data:any):Observable<any>{

    const headers = new HttpHeaders({
      "Content-Type":"application/json"
    })
    return this.http.post(this.baseUrl+"userregis",JSON.stringify(data),{headers})
  }

  allUsers():Observable<any[]>{
    return this.http.get<any[]>(this.baseUrl+"users")
  }


}
