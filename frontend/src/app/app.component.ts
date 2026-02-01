import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface PlayerStat {
  id: number;
  player_name: string;
  event_type: string;
  data: string;
  timestamp: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: []
})
export class AppComponent implements OnInit {
  title = 'pz-stats-frontend';
  stats: PlayerStat[] = [];
  // Note: we use a relative URL because Nginx proxies /api to the backend.
  apiUrl = '/api/stats';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.fetchStats();
  }

  fetchStats() {
    this.http.get<PlayerStat[]>(this.apiUrl).subscribe({
      next: (data) => this.stats = data,
      error: (err) => console.error('Error fetching stats:', err)
    });
  }
}
