package com.previo.servicio.loker.util;

import org.springframework.http.HttpStatus;

import lombok.Data;

@Data
public class LockerException extends RuntimeException{

	private HttpStatus estado;

	public LockerException(HttpStatus estado) {
		this.estado = estado;
	}
	
	
	public LockerException(HttpStatus estado, String mensaje) {
		super(mensaje);
		this.estado = estado;
	}
	
	public LockerException(String mensaje) {
		this(HttpStatus.NOT_FOUND, mensaje);
	}
	
	
	
}
