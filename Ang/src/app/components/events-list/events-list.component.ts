import { Component, OnInit } from '@angular/core';
import { DataService } from '../../data.service';

@Component({
  selector: 'app-events-list',
  templateUrl: './events-list.component.html',
  styleUrl: './events-list.component.css'
})
export class EventsListComponent implements OnInit {
  events: any;
  currentEvent = null;
  currentIndex = -1;
  title = '';

  constructor(private dataService: DataService){ }

  ngOnInit(): void {
      this.retrieveEvents();
  }

  retrieveEvents(): void{
    this.dataService.getAll().subscribe(
      data => {
        this.events = data;
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

  refreshList(): void {
    this.retrieveEvents();
    this.currentEvent = null;
    this.currentIndex = -1;
  }

  setActiveEvent(event:any, index:any): void {
    this.currentEvent = event;
    this.currentIndex = index;
  }

  removeAllEvents(): void {
    this.dataService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.retrieveEvents();
        },
        error => {
          console.log(error);
        });
  }
}
