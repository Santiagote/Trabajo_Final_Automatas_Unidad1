import { Component } from '@angular/core';
import { LexerComponent } from './lexer/lexer';

@Component({
  selector: 'app-root',
  imports: [LexerComponent],
  template: `<app-lexer />`
})
export class AppComponent {}