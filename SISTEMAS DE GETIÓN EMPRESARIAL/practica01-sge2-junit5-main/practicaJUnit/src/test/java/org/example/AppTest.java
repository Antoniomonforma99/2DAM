package org.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

public class AppTest {
    @Test
   void depositoPositivo(){
        CuentaCorriente cc=new CuentaCorriente("cpp");
        boolean resultado=cc.deposit(7f);
        assertEquals(true,resultado);
    }
    @Test
    void depositoNegativo(){
        CuentaCorriente cc=new CuentaCorriente("cpp");
        boolean resultado=cc.deposit(-7f);
        assertEquals(false,resultado);
    }
    @Test
    void withdrawTrue(){
        CuentaCorriente cc=new CuentaCorriente("cpp",83264L,560f);
        boolean resultado=cc.withdraw(500f,15f);
        assertEquals(true,resultado);
    }
    @Test
    void withdrawFalseAmountMenorCero(){
        CuentaCorriente cc=new CuentaCorriente("cpp",83264L,560f);
        boolean resultado=cc.withdraw(-500f,15f);
        assertEquals(false,resultado);
    }
    @Test
    void withdrawFalseFeeMenorCero(){
        CuentaCorriente cc=new CuentaCorriente("cpp",83264L,560f);
        boolean resultado=cc.withdraw(500f,-15f);
        assertEquals(false,resultado);
    }

}
