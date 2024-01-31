import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) { }

  public login(nombre_usuario:string, contrasenia: string):Observable<any> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
    });

    const data = {
      "nombre_usuario": nombre_usuario,
      "contrasenia": contrasenia
    }

    return this.http.post('http://127.0.0.1:5000/login/', data, {headers})
  }
}
