import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LoginModule } from './login/login.module';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { TareasModule } from './tareas/tareas.module';
import { HeaderModule } from './header/header.module';
import { FooterModule } from './footer/footer.module';

@NgModule({
    declarations: [
      AppComponent
    ],
    imports: [
      BrowserModule,
      AppRoutingModule,
      LoginModule,
      HttpClientModule,
      TareasModule,
      HeaderModule,
      FooterModule
    ],
    providers: [],
    bootstrap: [AppComponent]
  })
  export class AppModule { }
  