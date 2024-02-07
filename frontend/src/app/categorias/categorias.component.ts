import { Component, OnInit } from '@angular/core';
import { CategoriasService } from './categorias.service';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import { Categoria } from './Categoria';
import { Tarea } from '../tareas/Tarea';
import { TareasService } from '../tareas/tareas.service';

@Component({
  selector: 'app-categorias',
  templateUrl: './categorias.component.html',
  styleUrls: ['./categorias.component.css']
})
export class CategoriasComponent implements OnInit {
  categorias: Array<Categoria>;
  nuevaCategoria: Categoria = {
    nombre: '',
    descripcion: '',
    tareas: [],
    id: 0
  }
  mostrarFormularioNuevaCategoria = false;

  constructor(private categoriasService: CategoriasService,
    private cookieService: CookieService,
    private router: Router) { }

  getCategorias() {
    this.categoriasService.getCategorias(this.cookieService.get('token_de_acceso')).subscribe(cs => {
      this.categorias = cs;
    })
  }

  toggleFormulario() {
    this.mostrarFormularioNuevaCategoria = !this.mostrarFormularioNuevaCategoria;
  }

  textoBoton() {
    return this.mostrarFormularioNuevaCategoria ? 'Cancelar' : 'Agregar Categoria';
  }

  agregarCategoria() {
    this.categoriasService.createCategoria(this.nuevaCategoria, this.cookieService.get('token_de_acceso')).subscribe(cs => {
    })
  }

  ngOnInit() {
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
        this.getCategorias();
      }
    }
  }

}
