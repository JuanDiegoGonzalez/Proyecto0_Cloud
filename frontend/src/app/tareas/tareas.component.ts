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
  nuevaTarea: Tarea;
  mostrarFormularioNuevaTarea = false;

  constructor(private tareasService: TareasService,
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
      this.categoriasService.getCategorias(this.cookieService.get('token_de_acceso')).subscribe(cs => {
        this.categorias = cs;
        this.tareas.forEach(tarea => {
          const categoriaAsociada = this.categorias.find(categoria => categoria.id === tarea.categoria);
          tarea.categoria_display = categoriaAsociada ? categoriaAsociada.nombre : 'Sin categoría';
        });
      })
    })
  }
  
  getToday(): string {
    const today = new Date();
    const year = today.getFullYear();
    const month = (today.getMonth() + 1).toString().padStart(2, '0');
    const day = today.getDate().toString().padStart(2, '0');
    return `${year}-${month}-${day}`;
  }

  inicializarNuevaTarea() {
    this.nuevaTarea = {
      id: 0,
      texto: '',
      fecha_creacion: new Date(),
      fecha_tentativa_finalizacion: new Date(),
      estado: undefined,
      estado_display: '',
      usuario: 0,
      categoria: 0,
      categoria_display: ''
    }
  }

  agregarTarea() {
    this.tareasService.createTarea(this.nuevaTarea, this.cookieService.get('token_de_acceso')).subscribe(ts => {
      this.inicializarNuevaTarea();
      this.toggleFormulario();
      this.getTareasUsuario();
    })
  }

  editarTarea(tarea: Tarea) {
    this.tareasService.createTarea(this.nuevaTarea, this.cookieService.get('token_de_acceso')).subscribe(ts => {
      this.getTareasUsuario();
    })
  }

  borrarTarea(tarea: Tarea) {
    this.tareasService.deleteTarea(tarea, this.cookieService.get('token_de_acceso')).subscribe(ts => {
      this.getTareasUsuario();
    })
  }

  toggleFormulario() {
    this.mostrarFormularioNuevaTarea = !this.mostrarFormularioNuevaTarea;
  }

  textoBoton() {
    return this.mostrarFormularioNuevaTarea ? 'Cancelar' : 'Agregar Tarea';
  }

  ngOnInit(): void {
    const token_de_acceso = this.cookieService.get('token_de_acceso');

    if (token_de_acceso === "") {
      this.router.navigate(['/login']);
    } else {
      const payloadBase64 = token_de_acceso.split('.')[1];
      const decodedPayload = JSON.parse(window.atob(payloadBase64));

      if (decodedPayload.exp < Date.now() / 1000) {
        this.cookieService.set('token_de_acceso', "");
        this.router.navigate(['/login']);
      } else {
        this.inicializarNuevaTarea();
        this.getTareasUsuario();
      }
    }
  }
}
