import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Token {
  lexema: string;
  tipo: string;
  valido: boolean;
  inicio: number;
  fin: number;
}

@Injectable({
  providedIn: 'root'
})
export class LexerService {
  private apiUrl = 'http://localhost:5000/api';

  constructor(private http: HttpClient) {}

  tokenizar(codigo: string): Observable<{ tokens: Token[] }> {
    return this.http.post<{ tokens: Token[] }>(`${this.apiUrl}/tokenizar`, { codigo });
  }
}