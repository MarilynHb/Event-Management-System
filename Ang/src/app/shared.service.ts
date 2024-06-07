import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  getJobApplications() {
    throw new Error('Method not implemented.');
  }
  readonly APIUrl = "http://127.0.0.1:8000";
  readonly PhotoUrl = "http://127.0.0.1:8000/media/";

  constructor(private http: HttpClient) { }

  getIndList(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/location/');
  }

  addLocation(val: any): Observable<any> {
    return this.http.post(this.APIUrl + '/location/', val);
  }

  updateLocation(val: any): Observable<any> {
    return this.http.put(this.APIUrl + '/location/' + val.id + '/', val);
  }

  deleteLocation(id: any): Observable<any> {
    return this.http.delete(this.APIUrl + '/location/' + id + '/');
  }

  getETList(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/eventType/');
  }

  addEventType(val: any): Observable<any> {
    return this.http.post(this.APIUrl + '/eventType/', val);
  }

  updateEventType(val: any): Observable<any> {
    return this.http.put(this.APIUrl + '/eventType/' + val.id + '/', val);
  }

  deleteEventType(id: any): Observable<any> {
    return this.http.delete(this.APIUrl + '/eventType/' + id + '/');
  }

  getETgList(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/eventTag/');
  }

  addEventTag(val: any): Observable<any> {
    return this.http.post(this.APIUrl + '/eventTag/', val);
  }

  updateEventTag(val: any): Observable<any> {
    return this.http.put(this.APIUrl + '/eventTag/' + val.id + '/', val);
  }

  deleteEventTag(id: any): Observable<any> {
    return this.http.delete(this.APIUrl + '/eventTag/' + id + '/');
  }
}
