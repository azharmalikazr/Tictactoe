import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CheckBootstrapComponent } from './check-bootstrap/check-bootstrap.component';
import { GameComponent } from './game/game.component';
import { RegisterUserComponent } from './register-user/register-user.component';

const routes: Routes = [
  {path: 'game', component: GameComponent},
  {path: "register", component: RegisterUserComponent},
  {path: "bootstrap", component: CheckBootstrapComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

export const routingComponent = [GameComponent,RegisterUserComponent,CheckBootstrapComponent]