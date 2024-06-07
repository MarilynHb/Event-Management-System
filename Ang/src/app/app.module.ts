import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddUsersComponent } from './add-users/add-users.component';
import { AddEventComponent } from './components/add-event/add-event.component';
import { EventDetailsComponent } from './components/event-details/event-details.component';
import { EventsListComponent } from './components/events-list/events-list.component';
import { LocationShowComponent } from './location-show/location-show.component';
import { EventTypeShowComponent } from './event-type-show/event-type-show.component';
import { EventTagShowComponent } from './event-tag-show/event-tag-show.component';

@NgModule({
  declarations: [
    AppComponent,
    AddUsersComponent,
    AddEventComponent,
    EventDetailsComponent,
    EventsListComponent,
    LocationShowComponent,
    EventTypeShowComponent,
    EventTagShowComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
