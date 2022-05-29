package com.previo.servicio.loker.util;

import java.io.Serializable;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class LockerDate implements Serializable{

	private static final long serialVersionUID = 1L;
	
	
	public String formatToDateTime(Date date, String format) {
		if(date != null) {
			if(!Common.isChain(format)) {
				format = LockerVariable.PASTLEY_DATE_TIME_FORMAT;
			}
			DateFormat f = new SimpleDateFormat(format);
			System.out.println("Este es mi formato" + f.format(date));
			return f.format(date);
		}
		return null;
	}
	
	
	/**
	 * Method that converts a date.
	 * @param date, Represents the convert date.
	 * @return the converted date.
	 * @throws ParseException The error presented.
	 */
	public Date convertToDate(String date) throws ParseException {
		 SimpleDateFormat dt = new SimpleDateFormat(LockerVariable.PASTLEY_DATE_FORMAT_DATE);
	     return (Date) dt.parse(date);
	}
	
}
