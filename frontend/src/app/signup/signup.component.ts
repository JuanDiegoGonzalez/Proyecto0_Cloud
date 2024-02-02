import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { SignupService } from './signup.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {
  signUpForm: FormGroup;

  constructor(private fb: FormBuilder,
    private signupService: SignupService,
    private cookieService: CookieService,
    private router: Router) {
    this.signUpForm = this.fb.group({
      nombre_usuario: ['', Validators.required],
      contrasenia: ['', Validators.required],
      confirmar_contrasenia: ['', Validators.required],
    });
  }

  signUp(): void {
    const usernameControl = this.signUpForm.get('nombre_usuario');
    const passwordControl = this.signUpForm.get('contrasenia');
    const confirmPasswordControl = this.signUpForm.get('confirmar_contrasenia');

    if (usernameControl && passwordControl && confirmPasswordControl) {
      const username = usernameControl.value;
      const password = passwordControl.value;
      const confirmPassword = confirmPasswordControl.value;

      if (password.length < 8) {
        this.signUpForm.get('contrasenia')!.setErrors({ 'tooShortPassword': true });        
        return;
      }

      if (password !== confirmPassword) {
        this.signUpForm.get('confirmar_contrasenia')!.setErrors({ 'passwordMismatch': true });        
        return;
      }

      this.signupService.signup(username, password).subscribe(ss => {
        if ('error' in ss) {
          this.signUpForm.get('nombre_usuario')!.setErrors({ 'usernameAlreadyExists': true });        
        } else {
        this.cookieService.set('token_de_acceso', ss.token_de_acceso);
        this.cookieService.set('nombre_usuario', ss.usuario.nombre_usuario);
        this.router.navigate(['/tareas']);
        }
      })
    }
  }

  login() {
    this.router.navigate(['/login']);
  }

  ngOnInit(): void {
    if(this.cookieService.get('token_de_acceso') !== "") {
      this.router.navigate(['/tareas']);
    }
  }
}