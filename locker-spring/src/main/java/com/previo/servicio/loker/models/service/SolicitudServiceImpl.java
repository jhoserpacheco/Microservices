package com.previo.servicio.loker.models.service;

import java.util.ArrayList;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.RequestMapping;

import com.previo.servicio.loker.models.dao.CodigoQrDao;
import com.previo.servicio.loker.models.dao.LockerDao;
import com.previo.servicio.loker.models.dao.SolicitudDao;
import com.previo.servicio.loker.models.entity.CodigoQr;
import com.previo.servicio.loker.models.entity.Locker;
import com.previo.servicio.loker.models.entity.Solicitud;
import com.previo.servicio.loker.models.service.interfaces.ISolicitudService;
import com.previo.servicio.loker.util.Common;
import com.previo.servicio.loker.util.LockerDate;
import com.previo.servicio.loker.util.LockerException;



@Service
@RequestMapping("/api/solicitud")
public class SolicitudServiceImpl implements ISolicitudService {

	@Autowired
	private SolicitudDao solicitudDao;

	@Autowired
	private LockerDao lockerDao;

	@Autowired
	private CodigoQrDao codigoQrDao;

	@Override
	@Transactional(readOnly = true)
	public List<Solicitud> findAll() {
		return (List<Solicitud>) solicitudDao.findAll();
	}

	@Override
	@Transactional(readOnly = true)
	public Solicitud findById(Long id) {

		if (!Common.isLong(id))
			throw new LockerException("El id de la solicitud no es valido.");
		return solicitudDao.findById(id).get();

	}

	@Override
	public Solicitud save(Solicitud objeto) {

		CodigoQr codigoQr = codigoQrDao.findById(objeto.getIdCodigoQr())
				.orElseThrow(() -> new LockerException("No existe ningun codigoQr con este id"));
		System.out.println(codigoQr.isSolicitud());
		if (codigoQr.isSolicitud()) {
			throw new LockerException("Este usuario con este codigo Qr ya tiene un locker asignado");
		}

		List<Locker> lockersDisponibles = lockerDao.findByEstadoLocker(0);

		if (lockersDisponibles.isEmpty()) {
			throw new LockerException("No existe ningun locker disponible");
		}

		codigoQr.setSolicitud(true);
		codigoQrDao.save(codigoQr);
		Locker locker = lockersDisponibles.get(0);
		locker.setEstado(1);
		lockerDao.save(locker);
		objeto.setIdLocker(locker.getIdLocker());
		return solicitudDao.save(objeto);

	}

	@Override
	public void liberarLocker(Solicitud objeto) {

		CodigoQr codigoQr = codigoQrDao.findById(objeto.getIdCodigoQr())
				.orElseThrow(() -> new LockerException("No existe ningun codigoQr con este id"));
		if (codigoQr.isSolicitud()) {

			// se cambia el valor del locker
			codigoQr.setSolicitud(false);
			codigoQrDao.save(codigoQr);
			// se cambia el estado de solicitud del codigo qr
			Locker locker = lockerDao.findById(objeto.getIdLocker()).get();
			locker.setEstado(0);
			lockerDao.save(locker);

			throw new LockerException("Este usuario con este codigo Qr ya tiene un locker asignado");
		}

	}

	@Override
	public void saveAll(ArrayList<Solicitud> objetos) {
		solicitudDao.saveAll(objetos);
	}

	@Override
	public void deleteById(Long id) {
		solicitudDao.deleteById(id);

	}

	@Override
	public void delete(Solicitud entity) {
		solicitudDao.delete(entity);

	}

	@Override
	public List<Solicitud> findAllByRangeDate(String fechaInicio, String fechaFin) {
		
		if (Common.isChain(fechaInicio) && Common.isChain(fechaFin)) {
			return solicitudDao.findByFechaPrestamo(fechaInicio,fechaFin);
		} else {
			throw new LockerException(HttpStatus.NOT_FOUND, "No se ha recibido la fecha inicio o la fecha fin.");
		}
		
		
	}

}
