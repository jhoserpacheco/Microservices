package com.previo.servicio.loker.models.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.previo.servicio.loker.models.dao.CodigoQrDao;
import com.previo.servicio.loker.models.entity.CodigoQr;
import com.previo.servicio.loker.models.service.interfaces.ICodigoQrService;
import com.previo.servicio.loker.util.LockerException;

/**
Implementation to get QRCODE microservice on language programing JAVA
 */

@Service
public class CodigoQrServiceImpl implements ICodigoQrService {
	
	@Autowired
	private CodigoQrDao codigoQrDao;

	@Override
	@Transactional(readOnly = true)
	public List<CodigoQr> findAll() {
		return (List<CodigoQr>) codigoQrDao.findAll();
	}

	@Override
	@Transactional(readOnly = true)
	public CodigoQr findById(Long id) {
		return codigoQrDao.findById(id).orElseThrow(()->new LockerException("No existe ningun codigoQr con este id"));
	}

	@Override
	public CodigoQr save(CodigoQr objeto) {
		return codigoQrDao.save(objeto);

	}

	@Override
	public void saveAll(ArrayList<CodigoQr> objetos) {
		codigoQrDao.saveAll(objetos);

	}

	@Override
	public void deleteById(Long id) {
		codigoQrDao.deleteById(id);
	}

	@Override
	public void delete(CodigoQr entity) {
		codigoQrDao.delete(entity);
		}

}
