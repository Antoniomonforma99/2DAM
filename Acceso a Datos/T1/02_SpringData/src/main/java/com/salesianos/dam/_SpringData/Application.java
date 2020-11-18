package com.salesianos.dam._SpringData;

import model.Alumno;
import model.AlumnoRepos;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

	@Bean
	public CommandLineRunner init(AlumnoRepos repo){
		return args ->  {
			Alumno a = Alumno.builder()
					.nombre("Antonio")
					.apellidos("Montero garcía")
					.direccion("Condes de Bustillo 17")
					.poblacion("Sevilla")
				.build();
			repo.save(a);
		};
	}


}
