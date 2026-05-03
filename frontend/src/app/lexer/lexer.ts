import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { LexerService, Token } from '../services/lexer';

@Component({
  selector: 'app-lexer',
  imports: [CommonModule, FormsModule],
  templateUrl: './lexer.html',
  styleUrl: './lexer.css'
})
export class LexerComponent {
  codigo: string = '';
  tokens: Token[] = [];
  cargando: boolean = false;
  error: string = '';

  constructor(private lexerService: LexerService) {}

  analizar() {
    if (!this.codigo.trim()) {
      this.error = 'Por favor ingresa código fuente';
      return;
    }
    this.cargando = true;
    this.error = '';
    this.tokens = [];

    this.lexerService.tokenizar(this.codigo).subscribe({
      next: (res) => {
        this.tokens = res.tokens;
        this.cargando = false;
      },
      error: (err) => {
        this.error = 'Error al conectar con el servidor';
        this.cargando = false;
      }
    });
  }

  getColor(tipo: string): string {
    const colores: Record<string, string> = {
      'RESERVADA':     '#569cd6',  // azul
      'IDENTIFICADOR': '#4ec94e',  // verde
      'DECIMAL':       '#ce9178',  // naranja
      'LOGICO':        '#c586c0',  // morado
      'ARITMETICO':    '#dcdcaa',  // amarillo
      'INVALIDO':      '#f44747',  // rojo
      'ESPACIO':       'transparent'
    };
    return colores[tipo] || 'white';
  }

  getTokensValidos(): Token[] {
    return this.tokens.filter(t => t.valido && t.tipo !== 'ESPACIO');
  }

  getTokensInvalidos(): Token[] {
    return this.tokens.filter(t => !t.valido);
  }
}