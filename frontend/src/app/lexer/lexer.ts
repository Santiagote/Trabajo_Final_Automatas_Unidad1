import { Component, ChangeDetectorRef } from '@angular/core';
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

  constructor(private lexerService: LexerService, private cdr: ChangeDetectorRef) {}

  analizar() {
    if (!this.codigo.trim()) {
      this.error = 'Por favor ingresa código fuente';
      return;
    }
    this.cargando = true;
    this.error = '';

    this.lexerService.tokenizar(this.codigo).subscribe({
      next: (res) => {
        this.tokens = [...res.tokens];
        this.cargando = false;
        this.cdr.detectChanges();
      },
      error: (err) => {
        this.error = 'Error al conectar con el servidor';
        this.cargando = false;
        this.cdr.detectChanges();
      }
    });
  }

  getColor(tipo: string): string {
    const colores: Record<string, string> = {
      'RESERVADA':     '#569cd6',
      'IDENTIFICADOR': '#4ec94e',
      'DECIMAL':       '#ce9178',
      'LOGICO':        '#c586c0',
      'ARITMETICO':    '#dcdcaa',
      'INVALIDO':      '#f44747',
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