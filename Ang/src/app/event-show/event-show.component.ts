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
    if (this.event.id === 0) {
      this.event.tag = parseFloat(this.event.tag)
      this.event.type = parseFloat(this.event.type)
      this.event.location = parseFloat(this.event.location)
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
