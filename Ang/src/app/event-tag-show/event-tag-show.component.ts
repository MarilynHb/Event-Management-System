import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-event-tag-show',
  templateUrl: './event-tag-show.component.html',
  styleUrl: './event-tag-show.component.css'
})
export class EventTagShowComponent implements OnInit{
  EventTagList: any[] = [];
  modalTitle: string = '';
  ActivateAddEditComp: boolean = false;
  eventTag: any;

  constructor(private service: SharedService) {}

  ngOnInit(): void {
    this.refreshIndList();
  }

  refreshIndList(): void {
    this.service.getETgList().subscribe(data => {
      this.EventTagList = data;
    });
  }

  addClick() {
    this.eventTag = {
      id: 0,
      name: ''
    };
    this.modalTitle = "Add Event Tag";
    this.ActivateAddEditComp = true;
  }

  editClick(item: any) {
    this.eventTag = item;
    this.modalTitle = "Edit Event Tag";
    this.ActivateAddEditComp = true;
  }

  deleteClick(item: any) {
    if (confirm('Are you sure?')) {
      this.service.deleteEventTag(item.id).subscribe(data => {
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
    if (this.eventTag.id === 0) {
      this.service.addEventTag(this.eventTag).subscribe(data => {
        alert(data.toString());
        this.closeClick();
      });
    } else {
      this.service.updateEventTag(this.eventTag).subscribe(data => {
        alert(data.toString());
        this.closeClick();
      });
    }
  }
}
