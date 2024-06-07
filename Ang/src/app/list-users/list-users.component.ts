import { DataService } from './../data.service';
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-list-users',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './list-users.component.html',
  styleUrl: './list-users.component.css'
})
export class ListUsersComponent implements OnInit{
  users:any
  constructor(private dataservice:DataService){ }

  ngOnInit(): void{
    this.fetchUsers();
  }

  deleteUser(id:any){
    this.dataservice.delUser(id).subscribe((data)=>{
      this.fetchUsers();
    })
  }

  updateUser(id: any, userData: any) {
    this.dataservice.updateUser(id, userData).subscribe((data) => {
      this.fetchUsers();
    });
  }

  fetchUsers(){
    this.dataservice.listUsers().subscribe((data)=>{
      this.users = data;
    })
  }
  
}
