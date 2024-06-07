import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { DataService } from '../data.service';

@Component({
  selector: 'app-list-events',
  templateUrl: './list-events.component.html',
  styleUrls: ['./list-events.component.css'], // Corrected property name
})
export class ListEventsComponent {
  events: any;

  constructor(private dataservice: DataService) {}

  ngOnInit(): void {
    /* this.fetchEvents(); */
  }

  /* deleteEvent(id: any): void {
    this.dataservice.delEvent(id).subscribe(() => {
      this.events = this.events.filter((event: any) => event.id !== id);
    });
  }

  updateEvent(id: any, eventData: any) {
    this.dataservice.updateEvent(id, eventData).subscribe(() => {
      this.fetchEvents();
    });
  }

  fetchEvents() {
    this.dataservice.listEvents().subscribe((data) => {
      this.events = data;
    });
  } */
}
