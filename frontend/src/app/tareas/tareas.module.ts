import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TareasComponent } from './tareas.component';
import { CookieService } from 'ngx-cookie-service';
import { HeaderModule } from "../header/header.module";
import { FormsModule } from '@angular/forms';

@NgModule({
    declarations: [TareasComponent],
    exports: [TareasComponent],
    providers: [CookieService],
    imports: [
        CommonModule,
        HeaderModule,
        FormsModule
    ]
})
export class TareasModule { }
