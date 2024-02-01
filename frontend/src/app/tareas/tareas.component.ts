import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Tarea } from './Tarea'
import { TareasService } from './tareas.service';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import { CategoriasService } from '../categorias/categorias.service';
import { Categoria } from '../categorias/Categoria';

@Component({
  selector: 'app-tareas',
  templateUrl: './tareas.component.html',
  styleUrls: ['./tareas.component.css']
})
export class TareasComponent implements OnInit {
  tareas: Array<Tarea>;
  categorias: Array<Categoria>;

  constructor(private cdr: ChangeDetectorRef,
    private tareasService: TareasService,
    private categoriasService: CategoriasService,
    private cookieService: CookieService,
    private router: Router) { }

  getTareasUsuario() {
    this.tareasService.getTareasUsuario(this.cookieService.get('token_de_acceso')).subscribe(ts => {
      this.tareas = ts;
      this.tareas.forEach(tarea => {
        switch (tarea.estado.valor) {
          case 1:
            tarea.estado_display = "Sin empezar"
            break;
          case 2:
            tarea.estado_display = "Empezada"
            break;
          case 3:
            tarea.estado_display = "Finalizada"
            break;
        }
      });
    })
    this.categoriasService.getCategorias(this.cookieService.get('token_de_acceso')).subscribe(cs => {
      this.categorias = cs;
      this.tareas.forEach(tarea => {
        const categoriaAsociada = this.categorias.find(categoria => categoria.id === tarea.categoria);
        tarea.categoria_display = categoriaAsociada ? categoriaAsociada.nombre : 'Sin categoría';
      });
    })
  }

  ngOnInit() {
    if(this.cookieService.get('token_de_acceso') === "") {
      this.router.navigate(['/login']);
    } else {
      this.getTareasUsuario()
    }
  }
}
