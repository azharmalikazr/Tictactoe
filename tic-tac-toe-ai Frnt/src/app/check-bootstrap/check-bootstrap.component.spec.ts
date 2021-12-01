import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CheckBootstrapComponent } from './check-bootstrap.component';

describe('CheckBootstrapComponent', () => {
  let component: CheckBootstrapComponent;
  let fixture: ComponentFixture<CheckBootstrapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CheckBootstrapComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CheckBootstrapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
