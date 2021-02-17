package com.salesianos.ejemplorest

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*
import org.springframework.web.server.ResponseStatusException

@RestController
@RequestMapping("/message")
class Controller {

    @Autowired
    private lateinit var repositorio : MessageRepository

    @GetMapping("/")
    fun getAll() : ResponseEntity<List<Message>> {
        val result = repositorio.findAll()

        if(!result.isEmpty()){
            return ResponseEntity.ok(result)
        } else {
            throw ResponseStatusException(
                    HttpStatus.NOT_FOUND, "No hay mensajes"
            )
        }

    }

    @GetMapping("/{id}")
    fun getById(@PathVariable id : Long) =
            repositorio.findById(id)
                    .orElseThrow(){
                        ResponseStatusException(
                                HttpStatus.NOT_FOUND,
                                "No hay mensajes con id: ${id}"
                        )
                    }

    @PostMapping("/")
    fun create (@RequestBody msg : Message) :
            ResponseEntity<Message> =
                ResponseEntity
                        .status(HttpStatus.CREATED)
                        .body(repositorio.save(msg))


    @PutMapping("/{id}")
    fun edit (@PathVariable id : Long,
              @RequestBody edited : Message)
                : ResponseEntity<Message> = repositorio.findById(id)
                        .map {
                            msg ->
                            msg.text = edited.text
                            ResponseEntity.ok(repositorio.save(msg))
                        }.orElseThrow() {
                            ResponseStatusException(
                            HttpStatus.NOT_FOUND,
                            "No hay mensajes con id: ${id}")
                        }


    @DeleteMapping("/{id}")
    fun delete (@PathVariable id : Long) : ResponseEntity<Any> {
        if (repositorio.existsById(id))
            repositorio.deleteById(id)
        return ResponseEntity.noContent().build()
    }

}