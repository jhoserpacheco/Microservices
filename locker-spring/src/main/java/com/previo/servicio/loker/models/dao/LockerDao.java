package com.previo.servicio.loker.models.dao;

import java.util.List;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.previo.servicio.loker.models.entity.Locker;

@Repository
public interface LockerDao extends CrudRepository<Locker, Long> {
	
	@Query(nativeQuery = false, value = "SELECT c FROM Locker c WHERE c.estado = :estado")
	public List<Locker> findByEstadoLocker(@Param("estado") int estado);

}
