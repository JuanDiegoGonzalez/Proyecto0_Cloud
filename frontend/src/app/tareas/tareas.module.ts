import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TareasComponent } from './tareas.component';
import { CookieService } from 'ngx-cookie-service';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [TareasComponent],
  exports: [TareasComponent],
  providers: [CookieService]
})
export class TareasModule { }
