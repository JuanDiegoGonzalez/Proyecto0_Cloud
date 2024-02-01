import { Component, OnInit } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  nombre_usuario: string;

  constructor(private cookieService: CookieService) { }

  ngOnInit() {
    this.nombre_usuario = this.cookieService.get('nombre_usuario');
  }

}
