import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TicTacToeServerService {
  readonly APIUrl = "http://172.17.0.5:9090/";
  readonly APIUrll = "http://172.17.0.2:8080/";

  constructor(private http:HttpClient) { }

  getWebsiteList():Observable<any[]>{
    return this.http.get<any>(this.APIUrl + '/findMove');
  }
  addWebsite(val:any){
    return this.http.post(this.APIUrl + '/findMove', val);
  }
  updateWebsite(val:any){
    return this.http.put(this.APIUrl + '/findMove', val);
  }
  deleteWebsite(val:any){
    return this.http.delete(this.APIUrl + '/findMove',{body:val});
  }
  

  getAllWebsiteNames():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/findMove');
  }
}