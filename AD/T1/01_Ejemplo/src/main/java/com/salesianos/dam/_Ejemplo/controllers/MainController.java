package com.salesianos.dam._Ejemplo.controllers;


import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.time.LocalDateTime;

@Controller
public class MainController {

    @GetMapping("/")
    public String welcome(Model model) {

        model.addAttribute("mensaje", "Los alumnos de 2 dam");

        return "index";
        // return "/src/main/resources/templates/index.html"
    }
    @GetMapping("/now")
    public String now(Model model) {
        model.addAttribute("fecha", LocalDateTime.now() );
        return "fecha";
    }
}
