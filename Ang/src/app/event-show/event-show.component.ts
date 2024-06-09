import { Component } from '@angular/core';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-event-show',
  templateUrl: './event-show.component.html',
  styleUrl: './event-show.component.css'
})
export class EventShowComponent {
  EventList: any[] = [];
  EventTags: any[] = [];
  EventTypes: any[] = [];
  EventLocations: any[] = [];
  modalTitle: string = '';
  ActivateAddEditComp: boolean = false;
  event: any;

  constructor(private service: SharedService) {}

  ngOnInit(): void {
    this.refreshIndList();
  }

  refreshIndList(): void {
    this.service.getEventList().subscribe(data => {
      this.EventList = data;
    });
    this.service.getETgList().subscribe(data => {
      this.EventTags = data;
    });
    this.service.getETList().subscribe(data => {
      this.EventTypes = data;
    });
    this.service.getIndList().subscribe(data => {
      this.EventLocations = data;
    });
  }

  addClick() {
    this.event = {
      id: 0,
      title: '',
      description: '',
      eventType: { id: 0, name: '' },
      eventTag: { id: 0, description: '' },
      link: '',
      startDate: '',
      endDate: '',
      likes: '',
      location: { id: 0, description: ''}
    };
    this.modalTitle = "Add Event";
    this.ActivateAddEditComp = true;
}

  editClick(item: any) {
    this.event = item;
    this.event.location = item.location?.id
    this.event.tag = item.tag?.id
    this.event.type = item.type?.id
    this.event.start_date = this.formatDate(new Date(this.event.start_date));
    this.event.end_date = this.formatDate(new Date(this.event.end_date));
    this.modalTitle = "Edit Event";
    this.ActivateAddEditComp = true;
  }

  deleteClick(item: any) {
    if (confirm('Are you sure?')) {
      this.service.deleteEvent(item.id).subscribe(data => {
        alert(data.toString());
        this.refreshIndList();
      });
    }
  }

  closeClick() {
    this.ActivateAddEditComp = false;
    this.refreshIndList();
  }

  saveClick() {
    var error = ''

    if (!this.event.tag) error = 'Event, '

    if (!this.event.location) error = error + 'Location, '

    if (!this.event.type) error = error + 'Type, '

    if (this.event.title == '') error = error + 'Title, '

    if (this.event.description == '') error = error + 'Description, '

    if (this.event.link == '') error = error + 'Link, '

    if (error != '') alert(error + ' fields are required!')
    else {
      this.event.tag = {
        id: parseFloat(this.event.tag),
        description: this.EventTags.find((el) => el.id == this.event.tag)?.description
      }
      this.event.type = {
        id: parseFloat(this.event.type),
        name: this.EventTypes.find((el) => el.id == this.event.type)?.name
      }
      this.event.location = {
        id: parseFloat(this.event.location),
        description: this.EventLocations.find((el) => el.id == this.event.location)?.description
      }

      if (this.event.id === 0) {
        this.service.addEvent(this.event).subscribe(data => {
          alert(data.toString());
          this.closeClick();
        });
      } else {
        this.service.updateEvent(this.event).subscribe(data => {
          alert(data.toString());
          this.closeClick();
        });
      }
    }
  }

  formatDate(date: Date) {
    let month = '' + (date.getMonth() + 1);
    let day = '' + date.getDate();
    let year = date.getFullYear();
  
    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;
  
    return [year, month, day].join('-');
  }
}
