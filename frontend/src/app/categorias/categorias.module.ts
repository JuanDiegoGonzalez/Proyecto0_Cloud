import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CategoriasComponent } from './categorias.component';
import { CookieService } from 'ngx-cookie-service';
import { HeaderModule } from "../header/header.module";
import { FormsModule } from '@angular/forms';

@NgModule({
    declarations: [CategoriasComponent],
    exports: [CategoriasComponent],
    providers: [CookieService],
    imports: [
        CommonModule,
        HeaderModule,
        FormsModule
    ]
})
export class CategoriasModule { }
