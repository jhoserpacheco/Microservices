package com.previo.servicio.loker.models.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.previo.servicio.loker.models.dao.LockerDao;
import com.previo.servicio.loker.models.entity.Locker;
import com.previo.servicio.loker.models.service.interfaces.ILockerService;
import com.previo.servicio.loker.util.LockerException;

@Service
public class LockerServiceImpl implements ILockerService{
	
	
	@Autowired
	private LockerDao lockerDao;

	@Override
	@Transactional(readOnly = true)
	public List<Locker> findAll() {
		return (List<Locker>) lockerDao.findAll();
	}

	@Override
	@Transactional(readOnly = true)
	public Locker findById(Long id) {
		//no registratrar elemenos sin que los otros existan
		return lockerDao.findById(id).orElseThrow(()->new LockerException("No existe ningun locker con este id"));
	}

	@Override
	public Locker save(Locker objeto) {
		objeto.setEstado(0);
		return lockerDao.save(objeto);
	}

	@Override
	public void saveAll(ArrayList<Locker> objetos) {
		lockerDao.saveAll(objetos);
	}

	@Override
	public void deleteById(Long id) {
		lockerDao.deleteById(id);
		
	}

	@Override
	public void delete(Locker entity) {
		lockerDao.delete(entity);
		
	}

	@Override
	public List<Locker> findByEstadoLocker(int estado) {
		return lockerDao.findByEstadoLocker(estado);
	}
	
	

}
