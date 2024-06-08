import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-location-show',
  templateUrl: './location-show.component.html',
  styleUrls: ['./location-show.component.css']
})
export class LocationShowComponent implements OnInit {
  LocationList: any[] = [];
  modalTitle: string = '';
  ActivateAddEditComp: boolean = false;
  location: any;

  constructor(private service: SharedService) {}

  ngOnInit(): void {
    this.refreshIndList();
  }

  refreshIndList(): void {
    this.service.getIndList().subscribe(data => {
      this.LocationList = data;
    });
  }

  addClick() {
    this.location = {
      id: 0,
      name: ''
    };
    this.modalTitle = "Add Location";
    this.ActivateAddEditComp = true;
  }

  editClick(item: any) {
    this.location = item;
    this.modalTitle = "Edit Location";
    this.ActivateAddEditComp = true;
  }

  deleteClick(item: any) {
    if (confirm('Are you sure?')) {
      this.service.deleteLocation(item.id).subscribe(data => {
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
    if (!this.location.description || this.location.description == '') {
      alert('Description is required!');
    }
    else {
      if (this.location.id === 0) {
        this.service.addLocation(this.location).subscribe(data => {
          alert(data.toString());
          this.closeClick();
        });
      } else {
        this.service.updateLocation(this.location).subscribe(data => {
          alert(data.toString());
          this.closeClick();
        });
      }
    }
  }
}