import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-check-bootstrap',
  templateUrl: './check-bootstrap.component.html',
  styleUrls: ['./check-bootstrap.component.css']
})
export class CheckBootstrapComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  model = {
    left: true,
    middle: false,
    right: false
  };
}
