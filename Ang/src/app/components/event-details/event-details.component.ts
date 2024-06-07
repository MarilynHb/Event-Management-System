import { Component, OnInit } from '@angular/core';
import { DataService } from '../../data.service';
import { ActivatedRoute, Router } from '@angular/router';
import { response } from 'express';

interface Event {
  id: string;
  title: string;
  description: string;
}

@Component({
  selector: 'app-event-details',
  templateUrl: './event-details.component.html',
  styleUrl: './event-details.component.css'
})
export class EventDetailsComponent implements OnInit {
  currentEvent = null;
  message = '';

constructor(
  private dataService: DataService,
  private route: ActivatedRoute,
  private router: Router
){}

ngOnInit(): void{
  this.message = '';
  this.getEvent(this.route.snapshot.paramMap.get('id'));
}

getEvent(id:any): void{
  this.dataService.get(id).subscribe(data => {
    this.currentEvent = data;
    console.log(data);
  },
  error => {
    console.log(error);
  });
}


}
