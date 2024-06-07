import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EventTagShowComponent } from './event-tag-show.component';

describe('EventTagShowComponent', () => {
  let component: EventTagShowComponent;
  let fixture: ComponentFixture<EventTagShowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EventTagShowComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EventTagShowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
