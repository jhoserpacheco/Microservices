package com.previo.servicio.loker.util;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class LockerExeptionModel {

	private String mensaje;
	private int estado;
	
	public LockerExeptionModel() {
	}
	
	public static LockerExeptionModel builder(Exception exception, int estado) {
		return new LockerExeptionModel(exception.getMessage(),estado);
		
	}
	
	
	
}
