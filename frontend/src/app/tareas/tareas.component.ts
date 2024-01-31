import { Component, OnInit } from '@angular/core';
import { Tarea } from './Tarea'
import { TareasService } from './tareas.service';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-tareas',
  templateUrl: './tareas.component.html',
  styleUrls: ['./tareas.component.css']
})
export class TareasComponent implements OnInit {
  tareas: Array<Tarea>;

  constructor(private tareasService: TareasService,
    private cookieService: CookieService) { }

  getTareasUsuario() {
    this.tareasService.getTareasUsuario(this.cookieService.get('token_de_acceso')).subscribe(ts => {
      console.log(ts)
      this.tareas = ts;
    })
  }

  ngOnInit() {
    this.getTareasUsuario()
  }

}
