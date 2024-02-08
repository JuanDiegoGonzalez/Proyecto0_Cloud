import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Categoria } from './Categoria';

@Injectable({
  providedIn: 'root'
})
export class CategoriasService {

  constructor(private http: HttpClient) { }

  public getCategorias(token:string) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token,
    });

    return this.http.get<Categoria[]>(`http://127.0.0.1:5000/categorias/`, {headers})
  }

  public createCategoria(nuevaCategoria: Categoria, token:string) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token,
    });

    return this.http.post('http://127.0.0.1:5000/categorias/', nuevaCategoria, {headers})
  }

  public deleteCategoria(categoria: Categoria, token:string) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token,
    });

    return this.http.delete('http://127.0.0.1:5000/categorias/' + categoria.id + '/', {headers})
  }
}
