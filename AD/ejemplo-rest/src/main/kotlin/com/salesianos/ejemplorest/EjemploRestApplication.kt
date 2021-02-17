package com.salesianos.ejemplorest

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RestController

@SpringBootApplication
class EjemploRestApplication

fun main(args: Array<String>) {
	runApplication<EjemploRestApplication>(*args)
}

/*
data class Message(val id : Int, val text : String , val idioma : String)

@RestController
class MainController{

	private var datos = listOf(
			Message(1, "hola", "español"),
			Message(2, "hello", "inglés"),
			Message(3, "hola dola", "húngaro")
	)

	@GetMapping("/")
	fun getAll() : List<Message> = datos

	/*
	@GetMapping("/{id}")
	fun getById(@PathVariable id : Int) : Message? {
		var result : Message? = null
		try {
			result = datos.first() { it.id == id }
		} catch (ex : NoSuchElementException) {
			result = Message(0, "Error", "Error")
		}
		return result
	}
	*/

	@GetMapping("/{id}")
	fun getById(@PathVariable id : Int) : ResponseEntity<Message> {
		var result : Message? = null

		try {
			result = datos.first() { it.id == id}
			return ResponseEntity.ok(result)
		} catch (ex : NoSuchElementException){
			return ResponseEntity.status(404).body(
					Message(id, "No existe mensaje con id ${id}", "Error")
			)
		}

	}

}

 */
