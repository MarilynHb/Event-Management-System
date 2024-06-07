import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EventTypeShowComponent } from './event-type-show.component';

describe('EventTypeShowComponent', () => {
  let component: EventTypeShowComponent;
  let fixture: ComponentFixture<EventTypeShowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EventTypeShowComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EventTypeShowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
