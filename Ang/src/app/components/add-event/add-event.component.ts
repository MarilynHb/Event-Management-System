import { Component, OnInit } from '@angular/core';
import { DataService } from '../../data.service';
import { response } from 'express';

@Component({
  selector: 'app-add-event',
  templateUrl: './add-event.component.html',
  styleUrl: './add-event.component.css'
})
export class AddEventComponent implements OnInit {
  event = {
    title: '',
    description: ''
  };
  submitted = false;

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
     
  }

  saveEvent():void {
    const data = {
      title: this.event.title,
      decription: this.event.description
    };

    this.dataService.create(data).subscribe(
      response => {
        console.log(response);
        this.submitted = true;
      },
      error => {
        console.log(error);
      }
    );
  }

  newEvent(): void {
    this.submitted = false;
    this.event = {
      title: '',
      description: ''
    };
  }
}
