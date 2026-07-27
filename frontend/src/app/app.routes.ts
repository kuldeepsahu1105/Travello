import { Routes } from '@angular/router';
import { LayoutComponent } from './components/layout/layout.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { TripListComponent } from './components/trip-list/trip-list.component';
import { TripDetailComponent } from './components/trip-detail/trip-detail.component';
import { TripFormComponent } from './components/trip-form/trip-form.component';

export const routes: Routes = [
  {
    path: '',
    component: LayoutComponent,
    children: [
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
      { path: 'dashboard', component: DashboardComponent },
      { path: 'trips', component: TripListComponent },
      { path: 'trips/new', component: TripFormComponent },
      { path: 'trips/:id', component: TripDetailComponent },
      { path: 'trips/:id/edit', component: TripFormComponent },
    ],
  },
];
