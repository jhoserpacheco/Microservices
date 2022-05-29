package com.previo.servicio.loker.models.service.interfaces;

import java.text.ParseException;
import java.util.Date;
import java.util.List;

import com.previo.servicio.loker.models.entity.Solicitud;

public interface ISolicitudService extends IService<Solicitud>{

	 List<Solicitud> findAllByRangeDate(String fechaInicio,String fechaFin) throws ParseException;
	 public void liberarLocker(Solicitud objeto);
	
}
