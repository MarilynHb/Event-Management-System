import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListUsersComponent } from './list-users/list-users.component';
import { ListEventsComponent } from './list-events/list-events.component';
import { EventsListComponent } from './components/events-list/events-list.component';
import { EventDetailsComponent } from './components/event-details/event-details.component';
import { AddEventComponent } from './components/add-event/add-event.component';
import { LocationShowComponent } from './location-show/location-show.component';
import { EventTypeShowComponent } from './event-type-show/event-type-show.component';
import { EventTagShowComponent } from './event-tag-show/event-tag-show.component';

const routes: Routes = [
  { path: '', redirectTo: '/industry', pathMatch: 'full' }, // Default route
  { path: 'list-users', component: ListUsersComponent },
  { path: 'list-events', component: ListEventsComponent },
  { path: 'events', component: EventsListComponent },
  { path: 'events/:id', component: EventDetailsComponent },
  { path: 'add', component: AddEventComponent },
  { path: 'location', component: LocationShowComponent },
  { path: 'eventType', component: EventTypeShowComponent },
  { path: 'eventTag', component: EventTagShowComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
