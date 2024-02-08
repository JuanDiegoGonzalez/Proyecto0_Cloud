import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Tarea } from './Tarea';

@Injectable({
  providedIn: 'root'
})
export class TareasService {

  constructor(private http: HttpClient) { }

  public getTareasUsuario(token:string) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token,
    });

    return this.http.get<Tarea[]>(`http://127.0.0.1:5000/tareas/usuario/`, {headers})
  }

  public createTarea(nuevaTarea: Tarea, token:string) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token,
    });

    return this.http.post('http://127.0.0.1:5000/tareas/', nuevaTarea, {headers})
  }

  public deleteTarea(tarea: Tarea, token:string) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token,
    });

    return this.http.delete('http://127.0.0.1:5000/tareas/' + tarea.id + '/', {headers})
  }
}