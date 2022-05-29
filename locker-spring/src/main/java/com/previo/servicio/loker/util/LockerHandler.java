package com.previo.servicio.loker.util;

import java.util.HashMap;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.method.ControllerAdviceBean;

@ControllerAdvice

public class LockerHandler {

	private static final Map<String, Integer> estado = new HashMap<>();

	
    @ExceptionHandler(LockerException.class)
	public ResponseEntity<LockerExeptionModel> lockerException(HttpServletRequest request, Exception e) {

		ResponseEntity<LockerExeptionModel> response = null;

		Integer estado = getStatus(e);
		response = new ResponseEntity<>(new LockerExeptionModel(e.getMessage(), estado), HttpStatus.valueOf(estado));
		return response;
	}

	private Integer getStatus(Exception e) {
		if (e instanceof LockerException) {
			LockerException ex = (LockerException) e;
			if (ex.getEstado() != null) {
				return ex.getEstado().value();
			}
		}
		return estado.get(e.getClass().getSimpleName());
	}

}
