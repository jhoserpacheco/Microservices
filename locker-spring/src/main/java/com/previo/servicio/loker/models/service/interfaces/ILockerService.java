package com.previo.servicio.loker.models.service.interfaces;

import java.util.List;


import com.previo.servicio.loker.models.entity.Locker;

public interface ILockerService extends IService<Locker>{
	
	public List<Locker> findByEstadoLocker(int estado);

}
