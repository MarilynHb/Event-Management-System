import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router'; 
import { LocationShowComponent } from './location-show/location-show.component';
import { EventTypeShowComponent } from './event-type-show/event-type-show.component';
import { EventTagShowComponent } from './event-tag-show/event-tag-show.component';
import { EventShowComponent } from './event-show/event-show.component';

const routes: Routes = [
  { path: '', redirectTo: '/industry', pathMatch: 'full' }, // Default route
  { path: 'location', component: LocationShowComponent },
  { path: 'eventType', component: EventTypeShowComponent },
  { path: 'eventTag', component: EventTagShowComponent },
  { path: 'event', component: EventShowComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
