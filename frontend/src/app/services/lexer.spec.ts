import { TestBed } from '@angular/core/testing';

import { Lexer } from './lexer';

describe('Lexer', () => {
  let service: Lexer;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Lexer);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
