import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-event-type-show',
  templateUrl: './event-type-show.component.html',
  styleUrl: './event-type-show.component.css'
})
export class EventTypeShowComponent implements OnInit {
  EventTypeList: any[] = [];
  modalTitle: string = '';
  ActivateAddEditComp: boolean = false;
  eventType: any;

  constructor(private service: SharedService) {}

  ngOnInit(): void {
    this.refreshIndList();
  }

  refreshIndList(): void {
    this.service.getETList().subscribe(data => {
      this.EventTypeList = data;
    });
  }

  addClick() {
    this.eventType = {
      id: 0,
      name: ''
    };
    this.modalTitle = "Add Event Type";
    this.ActivateAddEditComp = true;
  }

  editClick(item: any) {
    this.eventType = item;
    this.modalTitle = "Edit Event Type";
    this.ActivateAddEditComp = true;
  }

  deleteClick(item: any) {
    if (confirm('Are you sure?')) {
      this.service.deleteEventType(item.id).subscribe(data => {
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
    if (this.eventType.id === 0) {
      this.service.addEventType(this.eventType).subscribe(data => {
        alert(data.toString());
        this.closeClick();
      });
    } else {
      this.service.updateEventType(this.eventType).subscribe(data => {
        alert(data.toString());
        this.closeClick();
      });
    }
  }
}
