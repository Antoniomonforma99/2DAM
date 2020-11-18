package com.ejemplo1.demo;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Ejemplo1Application {

	public static void main(String[] args) {
		SpringApplication.run(Ejemplo1Application.class, args);
	}


	public CommandLineRunner runMe (Saludator saludator) {
		return args -> {
			String msg = saludator.sayHello();
			System.out.println(msg);
		};
	}

}
