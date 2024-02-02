import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { LoginService } from './login.service';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm: FormGroup;

  constructor(private fb: FormBuilder,
    private loginService: LoginService,
    private cookieService: CookieService,
    private router: Router) {
    this.loginForm = this.fb.group({
      nombre_usuario: ['', Validators.required],
      contrasenia: ['', Validators.required]
    });
  }

  createAccount() {
    this.router.navigate(['/signup']);
  }

  login() {
    const usernameControl = this.loginForm.get('nombre_usuario');
    const passwordControl = this.loginForm.get('contrasenia');
    
    if (usernameControl && passwordControl) {
      const username = usernameControl.value;
      const password = passwordControl.value;

      this.loginService.login(username, password)
      .subscribe(ls => {
        if ('error' in ls) {
          this.loginForm.get('nombre_usuario')!.setErrors({ 'wrongUsernameOrPassword': true });        
        } else {
          this.cookieService.set('token_de_acceso', ls.token_de_acceso);
          this.cookieService.set('nombre_usuario', ls.usuario.nombre_usuario);
          this.router.navigate(['/tareas']);
        }
      })
    }
  }

  ngOnInit() {
    if(this.cookieService.get('token_de_acceso') !== "") {
      this.router.navigate(['/tareas']);
    }
  }
}
