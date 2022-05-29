package com.previo.servicio.loker.models.service.interfaces;

import java.util.ArrayList;
import java.util.List;

public interface IService<T>{

	public List<T> findAll();
	public T findById(Long id);
	
	public T save(T objeto);
	public void saveAll(ArrayList<T> objetos);
	
	public void deleteById(Long id);
	public void delete(T entity);
	
	
	
	
}
