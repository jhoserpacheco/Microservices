package com.previo.servicio.loker.models.entity;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "codigoQr")
public class CodigoQr implements Serializable{
	
	private static final long serialVersionUID = 1L;


	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "id")
	private Long idCodigoQr;
	
	
	@Column(name = "solicitud")
	private boolean solicitud;
	
	@Column(name = "value")
	private String value = "Base64";//base64
	
	@OneToMany(mappedBy = "idCodigoQr",cascade = CascadeType.ALL)
	private List<Solicitud> ListaSolicitudes = new ArrayList<Solicitud>();

}
