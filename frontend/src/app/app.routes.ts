import { Routes } from '@angular/router';
import { Dashboard } from './components/dashboard/dashboard';
import { Statistics } from './components/statistics/statistics';

export const routes: Routes = [
  { path: 'dashboard', component: Dashboard },
  { path: 'statistics', component: Statistics },
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' }
];
