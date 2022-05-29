package com.previo.servicio.loker.models.entity;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.persistence.UniqueConstraint;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "locker",uniqueConstraints = {@UniqueConstraint(columnNames = {"nombre"})})
public class Locker implements Serializable{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	/**
	 * 
	 */

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "id")
	private Long idLocker;
	
	@Column(name = "nombre")
	private String nombre;
	
	@Column(name = "estado")
	private int estado;
	
	
	
	@OneToMany(mappedBy = "idLocker",cascade = CascadeType.ALL)
	private List<Solicitud> listaSolicitudes = new ArrayList<Solicitud>();

}
