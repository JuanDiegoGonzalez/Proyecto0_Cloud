import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  nombre_usuario: string;

  constructor(private cookieService: CookieService,
    private router: Router) { }

  cerrarSesion(): void {
    this.cookieService.set('token_de_acceso', '');
    this.cookieService.set('nombre_usuario', '');
    this.router.navigate(['/login']);
  }

  ngOnInit() {
    this.nombre_usuario = this.cookieService.get('nombre_usuario');
  }

}
