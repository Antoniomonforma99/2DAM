package model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
@Data
@NoArgsConstructor @AllArgsConstructor
@Builder
public class Alumno {

    @Id
    @GeneratedValue
    private long id;


    private String nombre;
    private String apellidos;
    private String direccion;
    private String poblacion;
}
