import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-location-list',
  templateUrl: './location-list.component.html',
  styleUrls: ['./location-list.component.css']
})
export class LocationListComponent implements OnInit {
  locations: any = [];

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getLocations().subscribe(data => {
      this.locations = data;
    });
  }
}
