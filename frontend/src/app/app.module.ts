import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    RouterModule.forRoot([]) // Ensure you have imported RouterModule.forRoot and pass your routes array here if you have defined any
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
