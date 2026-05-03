import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Lexer } from './lexer';

describe('Lexer', () => {
  let component: Lexer;
  let fixture: ComponentFixture<Lexer>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Lexer],
    }).compileComponents();

    fixture = TestBed.createComponent(Lexer);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
