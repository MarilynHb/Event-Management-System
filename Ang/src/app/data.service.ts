import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
// import { Users } from './users';  // Ensure this model is correctly defined
// import { Events } from './events';  // Ensure this model is correctly defined

const API_URL_EVENTS = 'http://127.0.0.1:8000/api/events';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private API_URL_USERS = 'http://127.0.0.1:8000/api/users';

  constructor(private http: HttpClient) { }

  getAll(): Observable<any> {
    return this.http.get(API_URL_EVENTS);
  }

  get(id:string): Observable<any> {
    return this.http.get(`${API_URL_EVENTS}/${id}`);
  }

  create(data:any): Observable<any> {
    return this.http.post(API_URL_EVENTS, data);
  }

  update(id:string, data:any): Observable<any> {
    return this.http.put(`${API_URL_EVENTS}/${id}`, data);
  }

  delete(id:string): Observable<any> {
    return this.http.delete(`${API_URL_EVENTS}/${id}`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(API_URL_EVENTS);
  }
}
